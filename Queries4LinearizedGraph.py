from ast import arg
from rdflib import Graph, RDFS, RDF, URIRef, Namespace, Literal, XSD
from owlrl import DeductiveClosure, RDFS_Semantics
import random, sys
import sys
import os
import pandas as pd
from string import Template
import re
import json


def Graph_Generator_baseline_instances(story):
    texts = []
    text = story.query("""
  CONSTRUCT { ?herolabel ns2:hasTitle ?titlelabel.
  ?herolabel ns2:hasHouse ?houselabel.
  ?herolabel ns2:hasOccupation ?joblabel.

  ?villainlabel ns2:Threatens ?targetlabel.

  ?herolabel ns2:meetsMentor ?mentorlabel.
  ?herolabel ns2:powerLearned ?powerlabel.

  ?event4label ns2:Place4 ?labelplace4.
  ?event4label ns2:Time4 ?labeltime4.
  ?herolabel ns2:meetsAlly ?allylabel4.


  ?event5label ns2:Place5 ?place5label.
  ?event5label ns2:Time5 ?time5label.
  ?herolabel ns2:fights ?labelvillain5.
  ?herolabel ns2:helpedby ?labelally5.
  ?herolabel ns2:usespower ?labelpower.

  ?herolabel ns2:saves ?target6label.
  ?herolabel ns2:celebratesvictory ?celebrationlabel.
  ?herolabel ns2:partywith ?labelally6.



   } 
  WHERE {ns2:Event_01 ns2:hasTitle ?title.
  ?title rdfs:label ?titlelabel.
  ns2:Event_01 ns1:hasActor ?hero.
  ?hero rdfs:label ?herolabel.
  ns2:Event_01 ns2:hasHouse ?house.
  ?house rdfs:label ?houselabel.
  ns2:Event_01 ns2:hasOccupation ?job.
  ?job rdfs:label ?joblabel.

  ns2:Event_02 ns2:villain ?villain.
  ?villain rdfs:label ?villainlabel.
  ns2:Event_02 ns2:Threatens ?target.
  ?target rdfs:label ?targetlabel.

  ns2:Event_03 ns2:meetsMentor ?mentor.
  ?mentor rdfs:label ?mentorlabel.
  ns2:Event_03 ns2:powerLearned ?power.
  ?power rdfs:label ?powerlabel.


  ns2:Event_04 ns2:meetsAlly ?ally4.
  ?ally4 rdfs:label ?allylabel4.
  ns2:Event_04 ns1:hasPlace ?place4.
  ?place4 rdfs:label ?labelplace4. 
  ns2:Event_04 ns1:hasTime ?time4.
  ?time4 rdfs:label ?labeltime4.
  ns2:Event_04 rdfs:label ?event4label.


  ns2:Event_05 ns1:hasPlace ?place5.
  ?place5 rdfs:label ?place5label.  
  ns2:Event_05 ns1:hasTime ?time5.
  ?time5 rdfs:label ?time5label.
  ns2:Event_05 rdfs:label ?event5label.


  ns2:Event_05 ns2:herofights ?villain5.
  ?villain5 rdfs:label ?labelvillain5.
  ns2:Event_05 ns2:helpedBy ?ally5.
  ?ally5 rdfs:label ?labelally5.
  ns2:Event_05 ns2:usepower ?power.
  ?power rdfs:label ?labelpower.

  ns2:Event_06 ns2:saves ?target6.
  ?target rdfs:label ?target6label.
  ns2:Event_06 ns2:celebratesvictory ?celebration.
  ?celebration rdfs:label ?celebrationlabel.
  ns2:Event_06 ns2:partywith ?ally6.
  ?ally6 rdfs:label ?labelally6.


  }
    """, initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text)
    # for s,p,o in text:
    # print(s,p,o)
    if len(texts) == 0:
        print("WRONG smth in the query I am in q4text line 597")
    return text




#FROM HERE ON CONSTRUCTS NEED TO BE FIXED BASED ON NEW SHORT STORY


#ok but time and place is a problem :=)
def Graph_Generator_baseline_class(story):
    texts = []
    text = story.query("""
  CONSTRUCT { ?classhero ns2:hasTitle ?classtitle.
  ?classhero ns2:hasHouse ?classhouse.
  ?classhero ns2:hasOccupation ?classjob.

  ?villainlabel ns2:Threatens ?classtarget.

  ?classhero ns2:meetsMentor ?classmentor.
  ?classhero ns2:powerLearned ?classpowerlearnt.
  
  ?classhero ns2:meetsAlly ?allylabel4.




  ?classhero ns2:fights ?classvillain5.
  ?classhero ns2:helpedby ?classally5.
  ?classhero ns2:usespower ?classpower.

  ?classhero ns2:saves ?classtarget6.
  ?classhero ns2:celebratesvictory ?classcelebration.
  ?classhero ns2:partywith ?classally6.



   } 
  WHERE { ns2:hasTitle rdfs:range ?classtitle.
  ns1:hasActor rdfs:range ?classhero.
  ns2:hasHouse rdfs:range ?classhouse.
  ns2:hasOccupation rdfs:range ?classjob.

  ns2:villain rdfs:range  ?villainlabel.
  ns2:Threatens rdfs:range  ?classtarget.

  ns2:meetsMentor rdfs:range  ?classmentor.
  ns2:powerLearned rdfs:range  ?classpowerlearnt.


  ns2:meetsAlly rdfs:range ?allylabel4.





  ns2:herofights rdfs:range  ?classvillain5.
  ns2:helpedBy rdfs:range  ?classally5.
  ns2:usepower rdfs:range ?classpower.

  ns2:saves rdfs:range ?classtarget6.
  ns2:celebratesvictory  rdfs:range  ?classcelebration.
  ns2:partywith rdfs:range  ?classally6.


  }
    """, initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text)
    # for s,p,o in text:
    # print(s,p,o)
    if len(texts) == 0:
        print("WRONG smth in the query I am in q4text line 597")
    return text


def Graph_Generator_types(story):
    texts = []
    text = story.query("""
  CONSTRUCT { ?s ?p ?o . } 
  WHERE { {VALUES ?p {rdf:type rdfs:subClassOf} ?s ?p ?o} FILTER { ?o !=  {RDFS.Resource ns1.Core ns1.Authority}}}

    """, initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/'})
    texts.append(text)

    return text


def Graph_Generator_types(story):
    texts = []
    text = story.query("""
  CONSTRUCT { ?s a ?o . } 
  WHERE {?s a ?o.  FILTER(?o != ns1:Core). FILTER(?o != rdfs:Resource). FILTER(?o != ns2:Male) . FILTER(?o != ns2:Female) . FILTER(?o != owl:Class) . FILTER(?o != ns1:Event)}

    """, initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/','ns2': 'http://hero_ontology/','owl':'http://www.w3.org/2002/07/owl/'})
    texts.append(text)

    return text

def Graph_Generator_event(story):
    texts = []
    text = story.query("""
  CONSTRUCT { ?s ?p ?o . } 
  WHERE {VALUES ?s { ns2:Event_01 ns2:Event_02 ns2:Event_03 ns2:Event_04 ns2:Event_05 ns2:Event_06 ns2:Event_08 ns2:Event_09 ns2:Event_10 ns2:Event_11 ns2:Event_12 } ?s ?p ?o.
  FILTER(?o != ns1:Core). FILTER(?o != rdfs:Resource) }
    """, initNs={'ns2': 'http://hero_ontology/','ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/'})
    texts.append(text)

    return text


def Graph_Generator_range(story):
    texts = []
    text = story.query("""
  CONSTRUCT { ?s ?p ?o . } 
  WHERE {{VALUES ?s { ns2:Event_01 ns2:Event_02 ns2:Event_03 ns2:Event_04 ns2:Event_05 ns2:Event_06 ns2:Event_08 ns2:Event_09 ns2:Event_010
   ns2:Event_11 ns2:Event_12 } ?s ?p ?o } UNION {VALUES ?p { rdf:type rdfs:range} ?s ?p ?o. 
   }  FILTER(?o != ns1:Core). FILTER(?o != rdfs:Resource)}
    """, initNs={'ns2': 'http://hero_ontology/','ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/'})
    texts.append(text)

    return text



#https://networkedplanet.com/blog/2015/10/16/sparql-construct-101.html resource to understand CONSTRUCT
def Graph_Generator_baseline_instances_old(story):
    texts = []
    text = story.query("""
  CONSTRUCT { ?herolabel ns2:hasTitle ?titlelabel.
  ?herolabel ns2:hasHouse ?houselabel.
  ?herolabel ns2:hasOccupation ?joblabel.
  ?villainlabel ns2:Threatens ?targetlabel.
  ?herolabel ns2:refusesToFight ?villainlabel.
  ?herolabel ns2:scaredOf ?enemypowerlabel.
  ?herolabel ns2:meetsMentor ?mentorlabel.
  ?herolabel ns2:powerLearned ?heropowerlabel.
  ?herolabel ns2:travelsTo ?place5label.
  ?herolabel ns2:meetsAlly ?allylabel.
  ?allylabel ns2:faces ?villainallylabel.
  ?herolabel ns2:faces ?villainallylabel.
  ?herolabel ns2:herofights ?villainlabel.
  
  ?herolabel ns2:herousespower ?heropowerlabel.
  ?villainlabel ns2:enemyusespower ?enemypowerlabel.
  
  ?herolabel ns2:saves ?targetlabel.
  ?herolabel ns2:chasedby ?villainlabel.
  ?herolabel ns2:celebratesvictory ?celebrationlabel.
  ?herolabel ns2:partywith ?allylabel.


   } 
  WHERE {ns2:Event_01 ns2:hasTitle ?title.
  ?title rdfs:label ?titlelabel.
  ns2:Event_01 ns1:hasActor ?hero.
  ?hero rdfs:label ?herolabel.
  ns2:Event_01 ns2:hasHouse ?house.
  ?house rdfs:label ?houselabel.
  ns2:Event_01 ns2:hasOccupation ?job.
  ?job rdfs:label ?joblabel.
  ns2:Event_02 ns2:villain ?villain.
  ?villain rdfs:label ?villainlabel.
  ns2:Event_02 ns2:Threatens ?target.
  ?target rdfs:label ?targetlabel.
  ns2:Event_03 ns2:scaredOf ?enemypower.
  ?enemypower  rdfs:label ?enemypowerlabel.
  ns2:Event_04 ns2:meetsMentor ?mentor.
  ?mentor rdfs:label ?mentorlabel.
  ns2:Event_04 ns2:powerLearned ?heropower.
  ?heropower rdfs:label ?heropowerlabel.
  ns2:Event_05 ns2:travelsTo ?place5.
  ?place5 rdfs:label ?place5label.
  ns2:Event_06 ns2:meetsAlly ?ally.
  ?ally rdfs:label ?allylabel.
  ns2:Event_06 ns2:faces ?villainally.
  ?villainally rdfs:label ?villainallylabel.
  ns2:Event_06 ns2:faces ?villainally.
  ?villainally rdfs:label ?villainallylabel.
  ns2:Event_12 ns2:celebratesvictory ?celebration.
  ?celebration rdfs:label ?celebrationlabel.

  }
    """, initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/','ns2': 'http://hero_ontology/'})
    texts.append(text)
    print(text)
    if len(texts)==0:
        print("WRONG smth in the query I am in q4text line 597")
    return text



def Graph_Generator_baseline_classes_old(story):
    texts = []
    text = story.query("""
  CONSTRUCT { 
  ?classhero ns2:hasTitle ?classtitle.
  ?classhero ns2:hasHouse ?classhouse.
  ?classhero ns2:hasOccupation ?classoccupation.
  ns2:Event_01 ns1:hasTime ?classtime.
  ns2:Event_01 ns1:hasPlace ?classplace.
  ?classvillain ns2:Threatens ?classtarget.
  ?classhero ns2:refusesToFight ?classvillain.
  ?classhero ns2:scaredOf ?classenemypower.
  ?classhero ns2:meetsMentor ?classmentor.
  ?classhero ns2:powerLearned ?classheropower.
  ?classhero ns2:travelsTo ?classplace5.
  ?classhero ns2:meetsAlly ?classally.
  ?classally ns2:faces ?classvillainally.
  ?classhero ns2:faces  ?classvillainally.
  ?classhero ns2:herofights ?classvillain.
  ?classhero ns2:herousespower ?classheropower.
  ?classvillain ns2:enemyusespower ?classenemypower.
  ?classhero ns2:saves ?classtarget.
  ?classhero ns2:chasedby ?classvillain.
  ?classhero ns2:celebratesvictory ?classcelebration.
  ?classhero ns2:partywith ?classally.

  
   } 
  WHERE {
  ns1:hasActor rdfs:range ?classhero .
  ns2:hasTitle rdfs:range ?classtitle .
  ns2:hasHouse rdfs:range ?classhouse .
  ns2:hasOccupation rdfs:range ?classoccupation .
  ns1:hasPlace rdfs:range ?classplace.
  ns1:hasTime rdfs:range ?classtime.
  ns2:Threatens rdfs:range ?classtarget.
  ns2:villain rdfs:range ?classvillain.
  ns2:refusesToFight rdfs:range ?classvillain.
  
  ns2:scaredOf rdfs:range ?classenemypower.
  ns2:meetsMentor rdfs:range ?classmentor.
  ns2:powerLearned rdfs:range ?classheropower.
  ns2:travelsTo rdfs:range ?classplace5.
  ns2:meetsAlly rdfs:range ?classally.
  ns2:faces rdfs:range ?classvillainally.
  ns2:faces rdfs:range ?classvillainally.
  ns2:herofights rdfs:range ?classvillain.
  
  ns2:celebratesvictory rdfs:range ?classcelebration.
  

   
  
  

  }
    """, initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/','ns2': 'http://hero_ontology/'})
    texts.append(text)

    return text