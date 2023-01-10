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



def textGeneration_Event1_3_NEW(story):
    res = story.query("""
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
    
   
    BIND(CONCAT(  'A long time ago ', ?HeroName,' , ', ?TitleLabel,' from the ', ?FamilyLabel,', was known to be very good as a ',?HeroJob,'.' ) AS ?Event_01).
    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    # SO THING IS: STORY.QUERY returns a sparqlRESULTObject.
    # If the query was with select, sparqlResultObject is an interables of resultRow object.
    # ResultRow is a touple and our sententce is a literal in the first term.
    # Dus we do [0] to get the first element of list then [0] to get first element of a tuple
    # THne we do toPython() which a method of the class rdflib.term.Literal and this returns a string
    return list(res)[0][0].toPython()


# It was ',?TimeLabel1,' when this story begins.

def textGeneration_Event2_3_NEW(story):
    res = story.query("""
        SELECT ?Event_02 WHERE 
    {  
    ns2:Event_02 ns1:hasActor ?Hero.
    ?Hero  rdfs:label ?HeroName.
    ns2:Event_02 ns2:Threatens ?el.
    ?el   rdfs:label ?ElementLabel.
    ns2:Event_02 ns2:villain ?villain.
    ?villain rdfs:label ?VillainLabel.

   
    BIND(CONCAT( '', ?HeroName,' was having an happy and peaceful life when ', ?VillainLabel, ' threatened  ',?ElementLabel, ' of ', ?HeroName,' . ') AS ?Event_02).

    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    return list(res)[0][0].toPython()


def textGeneration_Event2_4_NEW(story):
    res = story.query("""
        SELECT ?Event_02 WHERE 
    {  
    ns2:Event_02 ns1:hasActor ?Hero.
    ?Hero  rdfs:label ?HeroName.
    ns2:Event_02 ns2:Threatens ?el.
    ?el   rdfs:label ?ElementLabel.
    ns2:Event_02 ns2:villain ?villain.
    ?villain rdfs:label ?VillainLabel.


    BIND(CONCAT('',?HeroName,' realized that their beloved ', ?ElementLabel, ' was in danger of being taken away by ' , ?VillainLabel,' . ' ) AS ?Event_02).

    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    return list(res)[0][0].toPython()


def textGeneration_Event3_3_NEW(story):
    res = story.query("""
        SELECT ?Event_03 WHERE 
    {  
        ns2:Event_03 ns1:hasActor ?Hero.
    ?Hero  rdfs:label ?HeroName.
    ns2:Event_03 ns2:meetsMentor ?mentor.
    ?mentor rdfs:label ?MentorLabel.
    ns2:Event_03 ns2:powerLearned ?power.
    ?power rdfs:label ?HeroPowerLabel.


    

    
    BIND(CONCAT('Our hero was not ready to fight for it, but with the help of  ', ?MentorLabel, ', ', ?HeroName,' learnt the power of ', ?HeroPowerLabel  ,'. ') AS ?Event_03).


    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    return list(res)[0][0].toPython()


def textGeneration_Event4_3_NEW(story):
    res = story.query("""
        SELECT ?Event_04 WHERE 
    {  
        ns2:Event_04 ns1:hasActor ?Hero.
    ?Hero  rdfs:label ?HeroName.
    ns2:Event_04 ns2:meetsAlly ?ally.
    ?ally rdfs:label ?AllyLabel.
   

    
    ns2:Event_04 ns1:hasTime ?Time4.
    ?Time4 rdfs:label ?TimeLabel4.
    ns2:Event_04 ns1:hasPlace ?Loc4.
    ?Loc4 rdfs:label ?LocLabel4.

    

    BIND(CONCAT(    'In ', ?LocLabel4 ,' at ',?TimeLabel4,',    ',?HeroName,' met ',?AllyLabel,' and they formed an alliance.') AS ?Event_04).



    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    return list(res)[0][0].toPython()




def textGeneration_Event5_3_NEW(story):
    res = story.query("""
        SELECT ?Event_05 WHERE 
    {  
        ns2:Event_05 ns1:hasActor ?Hero.
	?Hero  rdfs:label ?HeroName.

	ns2:Event_05 ns2:helpedBy ?ally.
	?ally rdfs:label ?AllyLabel.

	ns2:Event_05 ns2:herofights ?villain .
	?villain rdfs:label ?VillainLabel.

	ns2:Event_05 ns2:usepower ?poH .
	?poH rdfs:label ?poHLabel.

    ns2:Event_05 ns1:hasTime ?Time5.
    ?Time5 rdfs:label ?TimeLabel5.
    ns2:Event_05 ns1:hasPlace ?Loc5.
    ?Loc5 rdfs:label ?LocLabel5.

   
    BIND(CONCAT( 'Finally in ', ?LocLabel5 ,' at ', ?TimeLabel5 ,' , ' , ?HeroName, ' faced ', ?VillainLabel ,' . With the help of ', ?AllyLabel,' and thanks to the learnt power of ', ?poHLabel,' , the alliance scared away  ', ?VillainLabel ,' .') AS ?Event_05).

   

    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    return list(res)[0][0].toPython()


def textGeneration_Event6_3_NEW(story):
    res = story.query("""
        SELECT ?Event_06 WHERE 
    {  
      ns2:Event_06 ns1:hasActor ?Hero.
	?Hero  rdfs:label ?HeroName.

	ns2:Event_06 ns2:celebratesvictory ?cel.
	?cel rdfs:label ?celLabel.

	ns2:Event_06 ns2:partywith ?friend.
	?friend rdfs:label ?friendLabel.
	
	ns2:Event_06 ns2:saves ?obj.
	?obj rdfs:label ?savedobjLabel.
	
	
	ns2:Event_06 ns1:hasPlace ?Loc12.
	?Loc12 rdfs:label ?LocLabel6.

 
     BIND(CONCAT('This is how ', ?HeroName, ' managed to save ',?savedobjLabel,' and in ', ?LocLabel6, ' celebrated with  ',?friendLabel , ' by ' ,?celLabel, ' .'  ) as ?Event_06).


    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    return list(res)[0][0].toPython()



def textGeneration_Event5_1_NEW(story):
    res = story.query("""
        SELECT ?Event_05 WHERE 
    {  
        ns2:Event_05 ns1:hasActor ?Hero.
	?Hero  rdfs:label ?HeroName.

	ns2:Event_05 ns2:helpedBy ?ally.
	?ally rdfs:label ?AllyLabel.

	ns2:Event_05 ns2:herofights ?villain .
	?villain rdfs:label ?VillainLabel.

	ns2:Event_05 ns2:usepower ?poH .
	?poH rdfs:label ?poHLabel.

    ns2:Event_05 ns1:hasTime ?Time5.
    ?Time5 rdfs:label ?TimeLabel5.
    ns2:Event_05 ns1:hasPlace ?Loc5.
    ?Loc5 rdfs:label ?LocLabel5.

     BIND(CONCAT('At ', ?TimeLabel5 ,' in ', ?LocLabel5 ,', ' , ?HeroName, ' meets ', ?VillainLabel ,
      'and it is a bloody fight. Luckily ', ?AllyLabel,' is there to help. ', ?HeroName, ' uses ', ?poHLabel,' to scare away ', ?VillainLabel ,'.') AS ?Event_05).

   

    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    return list(res)[0][0].toPython()





