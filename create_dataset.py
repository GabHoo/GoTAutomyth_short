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
'''
def clear(story,semantic_given):
    HERO = Namespace("http://hero_ontology/")
    sem = Namespace("http://semanticweb.cs.vu.nl/2009/11/sem/")
    triples_clean = ""

    if semantic_given=='types':
        for s, p, o in story.triples((None, None, None)):
            if o==RDFS.Class or o==RDFS.Resource or o==sem.Core or  p == HERO.villain or p == HERO.ThreatenedElement or p==HERO.journeyStage or p==RDFS.range or p==HERO.hasTitle or p==HERO.hasHouse or p==HERO.hasOccupation or p==sem.hasActor or p==sem.hasPlace or p==sem.hasTime or p==RDFS.label:
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
'''
def clear1(story):
    result = ""
    for i in story:
        s = i[0]
        p = i[1]
        o = i[2]
        triples_clean = ""
        triples_clean += (
            (str(s).split('/')[-1] + " - " + str(p).split("/")[-1] + " - " + str(o).split("/")[-1] + " | "))
        triples_clean = re.sub('22-rdf-syntax-ns#', '', triples_clean)
        triples_clean = re.sub('rdf-schema##', '', triples_clean)
        triples_clean = re.sub('owl#', '', triples_clean)
        triples_clean = re.sub('rdf-schema#', '', triples_clean)
        triples_clean = re.sub('XMLSchema#', '', triples_clean)
        result += triples_clean
    return result





def random_formulation(story):
    #x=random.randint(1,3)
    # y = random.randint(1, 3)
    x = y = 1
    result = ''

    for i in [1,2,3,4]:
        t = globals()[f"textGeneration_Event{i}_{x}"](story)
        t = str(list(t))
        t = t.replace("[(rdflib.term.Literal('", "").replace("'),)]", "")
        t = t.replace('[(rdflib.term.Literal("','').replace('"),)]', '')
        print(t)
        result += t
    print(result)

    return result




def main(argv, arc):
    if arc!=4 or argv[1] not in ["community","relation","random"] or argv[2] not in ['types','event','range', 'baseline_instances','baseline_classes']:
        print("Error! Please enter a (valid) charachter picking method. (community,relation,random)")
        exit()
    method_generation = argv[1]
    semantic_given = argv[2]
    #n_kg_generated = int(argv[3])
    what = argv[3]

    if what == 'train':
        n_kg_generated = 500

    if what =='test':
        n_kg_generated = 50

    if what =='val':
        n_kg_generated = 50

    if what =='try':
        n_kg_generated = 1

    data = []
    count = 0
    count_KG = 0
    path = f'/Users/teresa/Documents/GitHub/GoTAutomyth_short/generated_output/events_{method_generation}_{semantic_given}'
    if os.path.exists(path)==False:
        os.mkdir(path)


    with open(f'generated_output/events_{method_generation}_{semantic_given}/{what}_events_yo_{method_generation}_{semantic_given}.json', 'w', encoding='utf-8') as f:
        f.write('[')
        while count<n_kg_generated:
            dict = {}
            story=gen_story(method_generation)
            print(type(story))

            text_try = list(Queries4Text.textGeneration_Event1_1(story))
            text_try2 = list(Queries4Text.textGeneration_Event2_1(story))

            if text_try2 == []: print(f'wrong {clear1(story)}')
            if text_try != [] and text_try2 != []: #check if text coherent

                #triples_list = clear(story, semantic_given)
                #print(story.triples)
                #triples = globals()[f"Graph_Generator_{semantic_given}"](story)
                #triples= Queries4Text.Graph_Generator(story)
                triples_classes = globals()[f"Graph_Generator_baseline_classes"](story)
                dict['Class Knowledge Graph'] = clear1(triples_classes)
                triples_inst = globals()[f"Graph_Generator_baseline_instances"](story)
                dict['Instances Knowledge Graph'] = clear1(triples_inst)
                triples_type = globals()[f"Graph_Generator_types"](story)
                dict['Types Knowledge Graph'] = clear1(triples_type)
                triples_event = globals()[f"Graph_Generator_event"](story)
                dict['Event Knowledge Graph'] = clear1(triples_event)
                triples_range = globals()[f"Graph_Generator_range"](story)
                dict['Range Knowledge Graph'] = clear1(triples_range)




                dict['story'] = random_formulation(story)
                #dict['story'] = dict['story'].replace("[(rdflib.term.Literal('", "").replace("'),)]", "")

                print(f'Generated story n {count}')
                count += 1
                json.dump(dict, f, ensure_ascii=False, indent="")
                story = story.serialize(f"./story_a_{method_generation}_{count}.ttl")
                #story.parse("http://www.w3.org/People/Berners-Lee/card")
                story.serialize(format="xml")
                if count != n_kg_generated:
                    f.write(',')
        f.write(']')

           # with open(f'generated_output/try_{method_generation}_{semantic_given}.json', 'w', encoding='utf-8') as f:
            #    json.dump(dict, f, ensure_ascii=False, indent="")






if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
