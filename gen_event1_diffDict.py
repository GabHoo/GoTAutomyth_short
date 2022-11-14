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
# import SPARQLWrapper

from scipy import rand


def random_pick(ist_class):
    if ist_class == URIRef("http://www.w3.org/2001/XMLSchema#boolean"):
        print("considering boooolean")
        return (random.choice([Literal("true", datatype=XSD.boolean), Literal("false", datatype=XSD.boolean)]))

    g = Graph()
    g.parse("./ontology_event1.ttl")
    g.parse("./got_instances.ttl")

    list_e = []

    class_node = URIRef(str(ist_class))

    for e in g.subjects(RDF.type, class_node):
        list_e.append(e)

    # THis is because Mentor for example is a subclass of actor. Since there are no instance directly for mentor we look for its super class (Actor) and pick instance of it.
    while (not list_e):
        # print("EMPTY LIST for", class_node)
        class_node = g.value(predicate=RDFS.subClassOf, subject=class_node, any=False)
        # print("new super class ", class_node)
        for e in g.subjects(RDF.type, class_node):
            list_e.append(e)

    # print("\nclass is ",class_node," list is of possible is : ",list_e)
    return (random.choice(list_e))


def add_labels(g,story):  # This methods add to our output story graph all the labels of the instances involved in the story. They are necessary for the visualization!
    sem = Namespace("http://semanticweb.cs.vu.nl/2009/11/sem/")
    event_inst = []
    for s, p, o in story.triples((None, RDF.type, sem.Event)):
        event_inst.append(s)
    # p
    for e in event_inst:
        for s, o, p in story.triples((e, None, None)):
            g.remove((None, None, RDFS.Resource))
            g.remove((None, None, sem.Core))
            g.remove((None, None, sem.Authority))

    for e in event_inst:
        for s, o, p in story.triples((e, None, None)):
            story += g.triples((p, RDF.type, None))
            story += g.triples((p, RDFS.label, None))

    return story

    # print("Adding necessary labels of every intence")


def domain_range(g, story):
    for s, p, o in g.triples((None, None, None)):
        #    story += g.triples((None,RDFS.domain,None))
        story += g.triples((None, RDFS.range, None))
    return story
    # print('domain-range')


main_characters = {"Jon_Snow": "Q3183235",
                   "Daenerys_Targaryen": "Q2708078",
                   "Arya_Stark": "Q3624677",
                   "Bran_Stark": "Q3643599",
                   "Cersei_Lannister": "Q3665163",
                   "Tyrion_Lannister": "Q2076759",
                   "Margaery_Tyrell": "Q12900933",
                   "Robert_Baratheon": "Q13634885"}


def find_communities(weighted_input):
    df = pd.read_csv(weighted_input, sep=",")
    df['char1'] = [i[-1] for i in df['char1'].str.split("/")]
    df['char2'] = [i[-1] for i in df['char2'].str.split("/")]

    tuples_lst = [(x[1]['char1'], x[1]['char2'], x[1]['valueSum']) for x in df.iterrows()]
    G = nx.Graph()
    G.add_weighted_edges_from(tuples_lst)

    communities = sorted(nxcom.greedy_modularity_communities(G), key=len, reverse=True)

    communities_dict = {}
    for com in communities:
        for mc in main_characters.keys():
            if mc in list(com):
                com_copy = list(com)
                com_copy.remove(mc)
                communities_dict[mc] = com_copy

    return communities_dict


def comm_based_pick(ist_class, communities=None, hero=None, char_type=None, villain=None):
    category = ist_class.split("/")[-1]
    if category == "Actor":
        hero = hero.split("/")[-1]

        if char_type == "Ally":
            return URIRef('http://hero_ontology/' + random.choice(list(communities[hero])))
        elif char_type == "Villain":
            enemy_comms = {}
            for k in communities.keys():
                if (not hero in communities[k] and k != hero):
                    enemy_comms[k] = communities[k]
            return URIRef('http://hero_ontology/' + random.choice(list(enemy_comms.keys())))
        if char_type == "Villain_Ally":
            villain = villain.split("/")[-1]
            return URIRef('http://hero_ontology/' + random.choice(list(communities[villain])))

    return random_pick(ist_class)


def read_network_data():
    edges = pd.read_csv("Network_of_Thrones/edges_subset.csv")
    nodes = pd.read_csv("Network_of_Thrones/nodes_subset.csv")
    return nodes, edges


def relation_based_pick(edges, related_to_char, n):
    related_to_char = related_to_char.split("/")[-1]
    so = edges[edges.Source == related_to_char][["Target", "weight"]].rename({'Target': 'Relation'}, axis=1)
    ta = edges[edges.Target == related_to_char][["Source", "weight"]].rename({'Source': 'Relation'}, axis=1)
    relations = pd.concat([so, ta]).sort_values(by="weight", ascending=False)[:n]
    # relations = so.append(ta).sort_values(by="weight", ascending=False)[:n]
    related_character = random.choices(list(relations["Relation"]), weights=list(relations["weight"]))
    return URIRef('http://hero_ontology/' + related_character[0])


def textGeneration_Event1(story):
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
    ns2:Event_01 ns1:hasTime ?Time1.
    ?Time1 rdfs:label ?TimeLabel1.
    ns2:Event_01 ns1:hasPlace ?Loc1.
    ?Loc1 rdfs:label ?LocLabel1.

    BIND(CONCAT('Once upon a time, in ',?LocLabel1 ,' there was a ',?HeroJob,' whose name was ', ?HeroName,'. ', ?HeroName, ' was a ', ?TitleLabel,' from the ', ?FamilyLabel,'. It was ',?TimeLabel1,' when this story begins.' ) AS ?Event_01).
    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text1)
    return (text1)


def textGeneration_Event12(story):
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
    ns2:Event_01 ns1:hasTime ?Time1.
    ?Time1 rdfs:label ?TimeLabel1.
    ns2:Event_01 ns1:hasPlace ?Loc1.
    ?Loc1 rdfs:label ?LocLabel1.

    BIND(CONCAT('It was ',?TimeLabel1, ' in ', ?LocLabel1, '. ', ?HeroName, ' was a  ' ,?TitleLabel,' from the ', ?FamilyLabel ,  ' and worked as a ',?HeroJob ) AS ?Event_01).
      }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text12)
    return (text12)


def textGeneration_Event13(story):
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
    ns2:Event_01 ns1:hasTime ?Time1.
    ?Time1 rdfs:label ?TimeLabel1.
    ns2:Event_01 ns1:hasPlace ?Loc1.
    ?Loc1 rdfs:label ?LocLabel1.


    BIND(CONCAT('' ,?LocLabel1,' was the place where the ',?HeroName, ',' ,?TitleLabel,' of ',?FamilyLabel, 'used to live. ' ,?HeroName,' was also known around ',?LocLabel1, ' as a great ',?HeroJob,' . It was ',?TimeLabel1,' when this story takes place.') AS ?Event_01). 

    }""", initNs={'ns1': 'http://semanticweb.cs.vu.nl/2009/11/sem/', 'ns2': 'http://hero_ontology/'})
    texts.append(text13)
    return (text13)


def gen_story(method):
    g = Graph(base="http://test.com/ns#")
    g.parse("./ontology_event1.ttl")
    g.parse("./got_instances.ttl")

    HERO = Namespace("http://hero_ontology/")
    sem = Namespace("http://semanticweb.cs.vu.nl/2009/11/sem/")
    DeductiveClosure(RDFS_Semantics).expand(g)

    if method == "community":
        communities = find_communities("query-result.csv")
    elif method == "relation":
        nodes, edges = read_network_data()
        n = 3

    # getting the list of all properties that main class EVENT has. properties is a list of a basic properties
    properties = []  # list of tuples, bc we need its range too
    for s, p, o in g.triples((None, RDFS.domain, sem.Event)):
        range_p = g.value(predicate=RDFS.range, subject=s,
                          any=False)  # HOPEFULLY THERE IS NOT MROE THAN ONE RANGE FOR THOSE
        properties.append((s, range_p))

    # Getting all subclasses, which are all the specific events
    subEvents = []
    for s, p, o in g.triples((None, RDFS.subClassOf, sem.Event)):
        subEvents.append(s)

    story = Graph()  # creates the graph of the story
    story.namespace_manager.bind('HERO', URIRef('http://hero_ontology/'))
    story.namespace_manager.bind('sem', URIRef('http://semanticweb.cs.vu.nl/2009/11/sem/'))

    fixed = {}
    fixed["Hero"] = random_pick("http://hero_ontology/Hero")

    if method == "community":
        fixed["Villain"] = comm_based_pick("http://semanticweb.cs.vu.nl/2009/11/sem/Actor", communities, fixed["Hero"],
                                           "Villain")
        fixed["HeroAlly"] = comm_based_pick("http://semanticweb.cs.vu.nl/2009/11/sem/Actor", communities, fixed["Hero"],
                                            "Ally")
        fixed["VillainAlly"] = comm_based_pick("http://semanticweb.cs.vu.nl/2009/11/sem/Actor", communities,
                                               fixed["Hero"], "Villain_Ally", fixed["Villain"])
        # instantiate_ordinary_world(g, fixed)
    elif method == "relation":
        fixed["Villain"] = relation_based_pick(edges, fixed["Hero"], 10)
        fixed["HeroAlly"] = relation_based_pick(edges, fixed["Hero"], n)
        fixed["VillainAlly"] = relation_based_pick(edges, fixed["Villain"], n)
        # instantiate_ordinary_world(g, fixed)

    elif method == "random":
        fixed["Villain"] = random_pick("http://hero_ontology/Villain")
        fixed["HeroAlly"] = random_pick("http://hero_ontology/HeroAlly")
        fixed["VillainAlly"] = random_pick("http://hero_ontology/VillainAlly")

    # print("list of subevents is:", subEvents)
    for i in subEvents:
        # print("Considering event", i)
        # NOW we are considering one subevent at a time

        # FIRST ADD THE ALREADY EXISTING INSTANCE TO THE STORY AND ITS TRIPLES(EVENT_N)
        instance_i = g.value(predicate=RDF.type, object=i, any=False)
        # print("found istance of ", i, ": ", instance_i)
        story += g.triples((instance_i, None, None))

        # THAN WE INSTANCIATE AND ADD TO STORY those that are common to every event
        for (p, r) in properties:  # property and range
            #print(p)
            range_str = r.split('/')[-1]
            if (range_str in fixed):
                #print(range_str, "is in fixed dic?")
                story.add((instance_i, p, fixed[range_str]))
            else:
                story.add((instance_i, p, random_pick(r)))

        # THIS IS TO INSTANCIATE AND ADD TO STORY THE TRIPLES SPECIFIC OF THAT EVENT i
        for s, p, o in g.triples((None, RDFS.domain, i)):  # takiing all the specific event properties
            # print("       considering", s)
            allranges = []  # THIS IS THO HANDLE MULTIPLE RANGES, SEE THRETENEDELEMENT (CALL TO ADVENTURE) EXAMPLE TO UNDERSTAND
            for s1, p1, o1 in g.triples((s, RDFS.range, None)):
                # print("       range: ", o1)
                allranges.append(o1)
            rand_range = (random.choice(allranges))
            range_str = rand_range.split('/')[-1]  # pick one from the possible ranges
            if (range_str in fixed):
                # print(range_str, "is in fixed dic")
                story.add((instance_i, s, fixed[range_str]))
            else:
                story.add((instance_i, s, random_pick(rand_range)))

    # HERE WE FIND A WAY TO DO THE SPARQL QUERY AND GET THE TEXT
    story = add_labels(g, story)
    story = domain_range(g, story)

    return story

def clear(story):
    HERO = Namespace("http://hero_ontology/")
    sem = Namespace("http://semanticweb.cs.vu.nl/2009/11/sem/")
    #story = gen_story(method)
    triples_clean = ""

    #story = story.serialize(f"./story_a_{method}.ttl")
    for s, p, o in story.triples((HERO.Event_01, None, None)):
        story.remove((None, None, RDFS.Resource))
        story.remove((None, None, sem.Core))
        # story.remove((None, RDFS.label, None))

    for s, p, o in story.triples((None, None, None)):
        triples_clean += (
            (str(s).split('/')[-1] + " - " + str(p).split("/")[-1] + " - " + str(o).split("/")[-1] + " | "))
        triples_clean = re.sub('22-rdf-syntax-ns#', '', triples_clean)
        triples_clean = re.sub('rdf-schema##', '', triples_clean)
        triples_clean = re.sub('owl#', '', triples_clean)
        triples_clean = re.sub('rdf-schema#', '', triples_clean)
        triples_clean = re.sub('XMLSchema#', '', triples_clean)

    triples_list = [triples_clean]

    return triples_list





def create_dict(method):
    story_try = gen_story(method)
    triples_list_try = clear(story_try)
    text_try = list(textGeneration_Event1(story_try))
    if text_try != []:
        #print(text_try)
        #story = gen_story(method)
        story = story_try
        triples_list = triples_list_try
        text1 = text_try


        text2 = list(textGeneration_Event12(story))
        text3 = list(textGeneration_Event13(story))
        #print(type(text1))

        dict = {}
        dict['Event_11'] = text1
        dict['Event_12'] = text2
        dict['Event_13'] = text3
        dict['Knowledge Graph'] = triples_list

    if text_try == []:
        dict = {}


    return dict



def main(argv, arc):
    data = []
    count = 0
    count_KG = 0

    for i in range(1000):
        dict = {}
        story_try = gen_story('relation')
        triples_list_try = clear(story_try)
        text_try = list(textGeneration_Event1(story_try))
        if text_try != []:

            # print(text_try)
            # story = gen_story(method)
            story = story_try
            triples_list = triples_list_try
            text1 = text_try

            dict['index'] = count
            count += 1
            dict['story'] = text1
            dict['KG index'] = count_KG
            dict['Knowledge Graph'] = triples_list
            data.append(dict)
            dict = {}
            dict['index'] = count
            count += 1
            dict['story'] = list(textGeneration_Event12(story))
            dict['KG index'] = count_KG
            dict['Knowledge Graph'] = triples_list
            data.append(dict)
            dict = {}
            dict['index'] = count
            count += 1
            dict['story'] = list(textGeneration_Event13(story))
            dict['KG index'] = count_KG
            dict['Knowledge Graph'] = triples_list
            data.append(dict)

            count_KG += 1
        #if dict != {} :
            #data.append(dict)
        print(len(data))
        #print(data)
        if len(data)==500:

            break







            #text2 = list(textGeneration_Event12(story))
            #text3 = list(textGeneration_Event13(story))
            # print(type(text1))

            #dict = {}
            #dict['Event_11'] = text1
            #dict['Event_12'] = text2
            #dict['Event_13'] = text3
            #dict['Knowledge Graph'] = triples_list

        #if text_try == []:
        #    dict = {}

        #inst = create_dict('relation')  # story is a dictionary with triples and text


       # if inst != {}:
       #     count +=1
        #    inst['index']=count
            #print(inst)
            #print(type(inst))
            #data[i] = story
        #    data.append(inst)
        #print(len(data))
        #if len(data)==5:
        #    break
    # data = {val for key, val in data.items() if val}
    #new_dict = {key: val for key,val in data.items() if val != {}}

    #if len(data)!=500:
    #print(len(data))

    with open('generated_output/train_data_event1.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent="")

    # for s,p,o in story.triples((HERO.Event_04, None , None)):
    #    print(s,p,o)
    # story = story.serialize(f"./story_a_{method}.ttl")
    # AND HERE WE TRY TO PUT EVERYTHING INTO ONE JSON
    # print(f"\n{method} based story has been generated succesfully! Check ./story_{method}.ttl ")


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
    # main('community',2)

#   x = main_run(argv, arc)
#   x1 = json.loads(x)
#   y = main_run(argv, arc)
#  y1 = json.loads(y)
# z = json.loads(x)
#   x1.update(y1)