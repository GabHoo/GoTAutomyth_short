from ast import arg
from rdflib import Graph, RDFS, RDF, URIRef, Namespace, Literal, XSD
from owlrl import DeductiveClosure, RDFS_Semantics
import random, sys
import sys
import os
import pandas as pd
from string import Template
import networkx as nx
import networkx.algorithms.community as nxcom
import re
import json
from StoryKG_generator import *
import StoryKG_generator
from Queries4Text import *
import Queries4Text
# import SPARQLWrapper

from scipy import rand

def clean_triples(s,p,o):
    triples_clean = ""
    triples_clean += (
        (str(s).split('/')[-1] + " - " + str(p).split("/")[-1] + " - " + str(o).split("/")[-1] + " | "))
    triples_clean = re.sub('22-rdf-syntax-ns#', '', triples_clean)
    triples_clean = re.sub('rdf-schema##', '', triples_clean)
    triples_clean = re.sub('owl#', '', triples_clean)
    triples_clean = re.sub('rdf-schema#', '', triples_clean)
    triples_clean = re.sub('XMLSchema#', '', triples_clean)
    return triples_clean

def clear(story,semantic_given):
    HERO = Namespace("http://hero_ontology/")
    sem = Namespace("http://semanticweb.cs.vu.nl/2009/11/sem/")
    triples_clean = ""

    if semantic_given=='types':
        for s, p, o in story.triples((None, None, None)):
            if o==RDFS.Class or o==RDFS.Resource or o==sem.Core or p==HERO.journeyStage or p==RDFS.range or p==HERO.hasTitle or p==HERO.hasHouse or p==HERO.hasOccupation or p==sem.hasActor or p==sem.hasPlace or p==sem.hasTime or p==RDFS.label:
                continue
            triples_clean += clean_triples(s,p,o)

    if semantic_given=='event':
        for s, p, o in story.triples((None, None, None)):
            if o==RDFS.Resource or o==sem.Core or p==RDFS.range or p==RDFS.label:
                continue
            triples_clean += clean_triples(s,p,o)


    if semantic_given=='range':
        for s, p, o in story.triples((None, None, None)):
            if o == RDFS.Resource or o == sem.Core or p == RDFS.label:
                continue
            triples_clean += clean_triples(s,p,o)


    return triples_clean

def random_formulation(story):
    x=random.randint(1,3)
    t1 = globals()[f"textGeneration_Event1_{x}"](story)
    y = random.randint(1, 3)
    t2 = globals()[f"textGeneration_Event2_{y}"](story)
    t1 = str(list(t1))
    t1 = t1.replace("[(rdflib.term.Literal('", "").replace("'),)]", "")
    t2 = str(list(t2))
    t2 = t2.replace("[(rdflib.term.Literal('", "").replace("'),)]", "")
    return t1 + t2




def main(argv, arc):
    if arc!=4 or argv[1] not in ["community","relation","random"] or argv[2] not in ['types','event','range']:
        print("Error! Please enter a (valid) charachter picking method. (community,relation,random)")
        exit()
    method_generation = argv[1]
    semantic_given = argv[2]
    n_kg_generated = int(argv[3])

    data = []
    count = 0
    count_KG = 0


    while count<n_kg_generated:
        dict = {}
        print("genrating1")
        story=gen_story(method_generation)

        text_try = list(Queries4Text.textGeneration_Event1_1(story))

        if text_try != []: #check if text coherent
            count += 1
            triples_list = clear(story, semantic_given)
            dict['Knowledge Graph'] = triples_list

            dict['story'] = random_formulation(story)


            with open(f'generated_output/try_{method_generation}_{semantic_given}.json', 'w', encoding='utf-8') as f:
                json.dump(dict, f, ensure_ascii=False, indent="")






if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
