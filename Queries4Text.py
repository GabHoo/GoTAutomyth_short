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

def textGeneration_Event1_1(story):
    texts = []
    text1 = story.query("""
    SELECT ?Event_01 WHERE 
    {  
    ns2:Event_01 ns1:hasActor ?Hero.

    ?Hero  rdfs:label ?HeroName.
    ns2:Event_01 ns2:hasOccupation ?Job.
    ?Job   rdfs:label ?HeroJob.
    ns2:Event_01 ns2:hasTitle ?Title.
    ?Title rdfs:label ?TitleLabel.
    ns2:Event_01 ns2:hasHouse ?Family.
    ?Family rdfs:label ?FamilyLabel.
    { SELECT ?Hero WHERE {
     {?Hero a ns2:Female.
     ?Title a ns2:Female}
     UNION
     {?Hero a ns2:Male.
     ?Title a ns2:Male}
      }
     }.
    ns2:Event_01 ns1:hasPlace ?Loc1.
    ?Loc1 rdfs:label ?LocLabel1.

    BIND(CONCAT('Once upon a time, in ',?LocLabel1 ,' there was a ',?HeroJob,' whose name was ', ?HeroName,'. ', ?HeroName, ' was a ', ?TitleLabel,' from the ', ?FamilyLabel,'. ' ) AS ?Event_01).
    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text1)
    return (text1)


# It was ',?TimeLabel1,' when this story begins.


def textGeneration_Event1_2(story):
    texts = []
    text12 = story.query("""
        SELECT ?Event_01 WHERE 
    {  
    ns2:Event_01 ns1:hasActor ?Hero.

    ?Hero  rdfs:label ?HeroName.
    ns2:Event_01 ns2:hasOccupation ?Job.
    ?Job   rdfs:label ?HeroJob.
    ns2:Event_01 ns2:hasTitle ?Title.
    ?Title rdfs:label ?TitleLabel.
    ns2:Event_01 ns2:hasHouse ?Family.
    ?Family rdfs:label ?FamilyLabel.
    { SELECT ?Hero WHERE {
     {?Hero a ns2:Female.
     ?Title a ns2:Female}
     UNION
     {?Hero a ns2:Male.
     ?Title a ns2:Male}
      }
     }.

    ns2:Event_01 ns1:hasPlace ?Loc1.
    ?Loc1 rdfs:label ?LocLabel1.

    BIND(CONCAT(' In ', ?LocLabel1, ' ', ?HeroName, ' was a  ' ,?TitleLabel,' from the ', ?FamilyLabel ,  ' and worked as a ',?HeroJob ,' . ') AS ?Event_01).
      }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text12)
    return (text12)
    # 'It was ',?TimeLabel1,
    # ns2:Event_01 ns1:hasTime ?Time1.
    # ?Time1 rdfs:label ?TimeLabel1.


def textGeneration_Event1_3(story):
    texts = []
    text13 = story.query("""
        SELECT ?Event_01 WHERE 
    {  
    ns2:Event_01 ns1:hasActor ?Hero.

    ?Hero  rdfs:label ?HeroName.
    ns2:Event_01 ns2:hasOccupation ?Job.
    ?Job   rdfs:label ?HeroJob.
    ns2:Event_01 ns2:hasTitle ?Title.
    ?Title rdfs:label ?TitleLabel.
    ns2:Event_01 ns2:hasHouse ?Family.
    ?Family rdfs:label ?FamilyLabel.
    { SELECT ?Hero WHERE {
     {?Hero a ns2:Female.
     ?Title a ns2:Female}
     UNION
     {?Hero a ns2:Male.
     ?Title a ns2:Male}
      }
     }.

    ns2:Event_01 ns1:hasPlace ?Loc1.
    ?Loc1 rdfs:label ?LocLabel1.


    BIND(CONCAT('' ,?LocLabel1,' was the place where ',?HeroName, ', the ' ,?TitleLabel,' of ',?FamilyLabel, ' used to live. ' ,?HeroName,' was also known around ',?LocLabel1, ' as a great ',?HeroJob,' . ') AS ?Event_01). 

    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text13)
    return (text13)
    # It was ',?TimeLabel1,' when this story takes place.'


def textGeneration_Event2_1(story):
    texts = []
    text = story.query("""
        SELECT ?Event_02 WHERE 
    {  
    ns2:Event_02 ns1:hasActor ?Hero.
    ?Hero  rdfs:label ?HeroName.
    ns2:Event_02 ns2:Threatens ?el.
    ?el   rdfs:label ?ElementLabel.
    ns2:Event_02 ns2:villain ?villain.
    ?villain rdfs:label ?VillainLabel.

    ns2:Event_02 ns1:hasTime ?Time2.
    ?Time2 rdfs:label ?TimeLabel2.
    ns2:Event_02 ns1:hasPlace ?Loc2.
    ?Loc2 rdfs:label ?LocLabel2.

    BIND(CONCAT('It was ',?TimeLabel2, ' in ' ,?LocLabel2,' when ', ?VillainLabel ,  ' threatened the  ',?ElementLabel, ' of ', ?HeroName,' . ' ) AS ?Event_02).

    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text)
    return (text)


def textGeneration_Event2_2(story):
    texts = []
    text = story.query("""
        SELECT ?Event_02 WHERE 
    {  
    ns2:Event_02 ns1:hasActor ?Hero.
    ?Hero  rdfs:label ?HeroName.
    ns2:Event_02 ns2:Threatens ?el.
    ?el   rdfs:label ?ElementLabel.
    ns2:Event_02 ns2:villain ?villain.
    ?villain rdfs:label ?VillainLabel.

    ns2:Event_02 ns1:hasTime ?Time2.
    ?Time2 rdfs:label ?TimeLabel2.
    ns2:Event_02 ns1:hasPlace ?Loc2.
    ?Loc2 rdfs:label ?LocLabel2.

    BIND(CONCAT('It was known that ', ?VillainLabel ,' wanted the  ',?ElementLabel, '  that belonged to ', ?HeroName, '. It was ',?TimeLabel2, ' in ' ,?LocLabel2,'  when ', ?VillainLabel ,'  threatened the ',?ElementLabel, ' of ', ?HeroName ,' . ') AS ?Event_02).

    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text)
    return (text)


def textGeneration_Event2_3(story):
    texts = []
    text = story.query("""
        SELECT ?Event_02 WHERE 
    {  
    ns2:Event_02 ns1:hasActor ?Hero.
    ?Hero  rdfs:label ?HeroName.
    ns2:Event_02 ns2:Threatens ?el.
    ?el   rdfs:label ?ElementLabel.
    ns2:Event_02 ns2:villain ?villain.
    ?villain rdfs:label ?VillainLabel.

    ns2:Event_02 ns1:hasTime ?Time2.
    ?Time2 rdfs:label ?TimeLabel2.
    ns2:Event_02 ns1:hasPlace ?Loc2.
    ?Loc2 rdfs:label ?LocLabel2.

    BIND(CONCAT('' ,?HeroName,' really cared about the ',?ElementLabel, ' . It was ',?TimeLabel2, ' in ' ,?LocLabel2,'  when  ', ?VillainLabel , ' threatened the  ',?ElementLabel, ' of ', ?HeroName,' . ' ) AS ?Event_02).

    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text)
    return (text)




def textGeneration_Event3_1(story):
    texts = []
    text = story.query("""
        SELECT ?Event_03 WHERE 
    {  
    ns2:Event_03 ns1:hasActor ?Hero.
    ?Hero  rdfs:label ?HeroName.
    ns2:Event_03 ns2:scaredOf ?EnemyPower.
    ?EnemyPower rdfs:label ?EnemyPowerLabel.
    ns2:Event_03 ns2:refusesToFight ?villain.
    ?villain rdfs:label ?VillainLabel

    BIND(CONCAT(?HeroName, ' was scared of the ' ,?EnemyPowerLabel,' power of ', ?VillainLabel ,  ' and refused to fight back. ') AS ?Event_03).

    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text)
    return (text)



def textGeneration_Event4_1(story):
    texts = []
    text = story.query("""
        SELECT ?Event_04 WHERE 
    {  
        ns2:Event_04 ns1:hasActor ?Hero.
    ?Hero  rdfs:label ?HeroName.
    ns2:Event_04 ns2:meetsMentor ?mentor.
    ?mentor rdfs:label ?MentorLabel.
    ns2:Event_04 ns2:powerLearned ?power.
    ?power rdfs:label ?HeroPowerLabel.


    ns2:Event_04 ns1:hasTime ?Time4.
    ?Time4 rdfs:label ?TimeLabel4.
    ns2:Event_04 ns1:hasPlace ?Loc4.
    ?Loc4 rdfs:label ?LocLabel4


    BIND(CONCAT('It was ',?TimeLabel4, ' in ', ?LocLabel4, ' when ', ?HeroName, ' met ', ?MentorLabel,' . ',' From ', ?MentorLabel,' ', ?HeroName ,' learnt the power of ', ?HeroPowerLabel,'. ') AS ?Event_04).


    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text)
    return (text)



def textGeneration_Event5_1(story):
    texts = []
    text = story.query("""
        SELECT ?Event_05 WHERE 
    {  
       ns2:Event_05 ns1:hasActor ?Hero.
    ?Hero  rdfs:label ?HeroName.
    ns2:Event_05 ns2:travelsTo ?place.
    ?place rdfs:label ?PlaceLabel.

    ns2:Event_05 ns1:hasTime ?Time.
    ?Time rdfs:label ?TimeLabel


    BIND(CONCAT('It was ',?TimeLabel,' when ', ?HeroName, ' finally gatherered the  courage to travel to ', ?PlaceLabel, '. ' )
        AS ?Event_05).

    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text)
    return (text)


def textGeneration_Event6_1(story):
    texts = []
    text = story.query("""
        SELECT ?Event_06 WHERE 
    {  
    ns2:Event_06 ns1:hasActor ?Hero.
	?Hero  rdfs:label ?HeroName.
	ns2:Event_06 ns2:meetsAlly ?ally.
	?ally rdfs:label ?allyLabel.
	ns2:Event_06 ns2:faces ?enemyally.
	?enemyally rdfs:label ?enemyallyLabel.

	ns2:Event_06 ns2:victory ?bool.

 	OPTIONAL { FILTER (?bool = true)
    	BIND("Victory" AS ?v)}

       OPTIONAL { FILTER (?bool = false)
    	BIND("Loss" AS ?v)}



	ns2:Event_06 ns1:hasTime ?Time6.
	?Time6 rdfs:label ?TimeLabel6.
	ns2:Event_06 ns1:hasPlace ?Loc6.
	?Loc6 rdfs:label ?LocLabel6


	BIND(CONCAT(' ', ?HeroName, ' met ',?allyLabel, '.',' Together they formed an alliance and fought against ',?enemyallyLabel,'. It resulted in an epic ', ?v, '. ') AS ?Event_06).


    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text)
    return (text)



def textGeneration_Event7_1(story):
    texts = []
    text = story.query("""
        SELECT ?Event_07 WHERE 
    {  
    ns2:Event_07 ns1:hasActor ?Hero.
	?Hero  rdfs:label ?HeroName.

	ns2:Event_07 ns2:feeling ?feeling.
	?feeling rdfs:label ?FeelingLabel.

	ns2:Event_07 ns1:hasTime ?Time7.
	?Time7 rdfs:label ?TimeLabel7.
	ns2:Event_07 ns1:hasPlace ?Loc7.
	?Loc7 rdfs:label ?LocLabel7.


	BIND(CONCAT('At ',?TimeLabel7, ' in ', ?LocLabel7, ', ', ?HeroName, ' felt ',?FeelingLabel, ' there was soon going to be another clash. ').
  
    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text)
    return (text)


def textGeneration_Event8_1(story):
    texts = []
    text = story.query("""
        SELECT ?Event_08 WHERE 
    {  
        ns2:Event_08 ns1:hasActor ?Hero.
	?Hero  rdfs:label ?HeroName.

	ns2:Event_08 ns2:enemyusespower ?po.
	?po rdfs:label ?poLabel.

	ns2:Event_08 ns2:herofights ?villain .
	?villain rdfs:label ?viLabel.

	ns2:Event_08 ns2:herousespower ?poH .
	?poH rdfs:label ?poHLabel.

	ns2:Event_08 ns2:herogetsinjured ?v8 .

 	OPTIONAL { FILTER (?v8 = true)
    	BIND("Injured" AS ?str)}

       OPTIONAL { FILTER (?v8 = false)
    	BIND("Safe" AS ?str)}



	ns2:Event_08 ns1:hasTime ?Time8.
	?Time8 rdfs:label ?TimeLabel8.
	ns2:Event_08 ns1:hasPlace ?Loc8.
	?Loc8 rdfs:label ?LocLabel8


	BIND(CONCAT('It was ',?TimeLabel8, ' in ', ?LocLabel8, ' when  ', ?HeroName,' faced ', ?viLabel,'. ', ?HeroName, ' used the power of ', ?poHLabel,' , but ',?viLabel, ' used '    , ?poLabel,'. Our hero was ', ?str, '. ' ) as ?Event_08).

    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text)
    return (text)


def textGeneration_Event9_1(story):
    texts = []
    text = story.query("""
        SELECT ?Event_09 WHERE 
    {  
    ns2:Event_09 ns1:hasActor ?Hero.
	?Hero  rdfs:label ?HeroName.

	ns2:Event_09 ns2:saves ?target.
	?target rdfs:label ?targetLabel.

	BIND(CONCAT('After a bloody fight, ',?HeroName,' finally saved ', ?targetLabel, '. ') as ?Event_09).


    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text)
    return (text)
#	ns2:Event_09 ns1:hasTime ?Time9.
#	?Time9 rdfs:label ?TimeLabel9.
#	ns2:Event_09 ns1:hasPlace ?Loc9.
#	?Loc9 rdfs:label ?LocLabel9

def textGeneration_Event10_1(story):
    texts = []
    text = story.query("""
        SELECT ?Event_10 WHERE 
    {  
    ns2:Event_10 ns1:hasActor ?Hero.
    ?Hero  rdfs:label ?HeroName.

	ns2:Event_10 ns2:chasedBy ?vil.
	?vil rdfs:label ?vilLabel.




	BIND(CONCAT('Soon after ',?vilLabel, ' was hungry for revenge and chased down ', ?HeroName, '. ') as ?Event_10).

    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text)
    return (text)

#	ns2:Event_10 ns1:hasTime ?Time10.
#	?Time10 rdfs:label ?TimeLabel10.
#	ns2:Event_10 ns1:hasPlace ?Loc10.
#?Loc10 rdfs:label ?LocLabel10

def textGeneration_Event11_1(story):
    texts = []
    text = story.query("""
        SELECT ?Event_11 WHERE 
    {  
    ns2:Event_11 ns1:hasActor ?Hero.
	?Hero  rdfs:label ?HeroName.

	ns2:Event_11 ns2:against ?vil.
	?vil rdfs:label ?vilLabel.

	ns2:Event_11 ns2:killsVillain ?v11 .

 	OPTIONAL { FILTER (?v11 = true)
    	BIND(" won the duel and took the life of the villain" AS ?str11)}

       OPTIONAL { FILTER (?v11 = false)
    	BIND(" won the duel but spared the life of the villain" AS ?str11)}


	ns2:Event_11 ns1:hasTime ?Time11.
	?Time11 rdfs:label ?TimeLabel11.
	ns2:Event_11 ns1:hasPlace ?Loc11.
	?Loc11 rdfs:label ?LocLabel11


	BIND(CONCAT('It was ',?TimeLabel11, ' in ', ?LocLabel11, ',  when our hero met ' ,?vilLabel, ' again, and they fought in the final battle. ',?HeroName,  ?str11, '. ') as ?Event_11).

    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text)
    return (text)


def textGeneration_Event12_1(story):
    texts = []
    text = story.query("""
        SELECT ?Event_12 WHERE 
    {  
      ns2:Event_12 ns1:hasActor ?Hero.
	?Hero  rdfs:label ?HeroName.

	ns2:Event_12 ns2:celebratesvictory ?cel.
	?cel rdfs:label ?celLabel.

	ns2:Event_12 ns2:partywith ?friend.
	?friend rdfs:label ?friendLabel.



	ns2:Event_12 ns1:hasTime ?Time12.
	?Time12 rdfs:label ?TimeLabel12.
	ns2:Event_12 ns1:hasPlace ?Loc12.
	?Loc12 rdfs:label ?LocLabel12


	BIND(CONCAT('Finally it was ',?TimeLabel12, ' in ', ?LocLabel12, ' when ', ?HeroName, ' was finally safe, and celebrated with ' , ?friendLabel , ' by '  , ?celLabel, '. ') as ?Event_12).


    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text)
    return (text)




'''
def Graph_Generator_types(story):
    texts = []
    text = story.query("""
  CONSTRUCT { ?s a ?o . } 
  WHERE {?s a ?o}
    """)
    texts.append(text)

    return text

'''

'''
def Graph_Generator_types(story):
    texts = []
    text = story.query("""
  CONSTRUCT { ?s ?p ?o . } 
  WHERE { {VALUES ?p {rdf:type rdfs:subClassOf} ?s ?p ?o} FILTER { ?o !=  {RDFS.Resource ns1.Core ns1.Authority}}}

    """, initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/'})
    texts.append(text)

    return text
'''

def Graph_Generator_types(story):
    texts = []
    text = story.query("""
  CONSTRUCT { ?s a ?o . } 
  WHERE {?s a ?o.  FILTER(?o != ns1:Core). FILTER(?o != rdfs:Resource) }

    """, initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/'})
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


def Graph_Generator_baseline_instances(story):
    texts = []
    text = story.query("""
  CONSTRUCT { ?herolabel ns2:hasTitle ?titlelabel.
  ?herolabel ns2:hasHouse ?houselabel.
  ?herolabel ns2:hasOccupation ?joblabel.
  
  ?villainlabel ns2:Threatens ?targetlabel.
  
  ?herolabel ns2:meetsMentor ?mentorlabel.
  ?herolabel ns2:powerLearned ?powerlabel.
  
  ?herolabel ns2:Place4 ?labelplace4.
  ?herolabel ns2:Time4 ?labeltime4.
  ?herolabel ns2:meetsAlly ?allylabel4.
    

  ?herolabel ns2:Place5 ?place5label.
  ?herolabel ns2:Time5 ?time5label.
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
  
 
  ns2:Event_05 ns1:hasPlace ?place5.
  ?place5 rdfs:label ?place5label.  
  ns2:Event_05 ns1:hasTime ?time5.
  ?time5 rdfs:label ?time5label.
  
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
    #for s,p,o in text:
        #print(s,p,o)
    if len(texts) == 0:
        print("WRONG smth in the query I am in q4text line 597")
    return text

def Graph_Generator_baseline_classes(story):
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