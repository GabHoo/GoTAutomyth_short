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
    ns2:Event_02 ns2:ThreatenedElement ?el.
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
    ns2:Event_02 ns2:ThreatenedElement ?el.
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
    ns2:Event_02 ns2:ThreatenedElement ?el.
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