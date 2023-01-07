from StoryKG_gen_reborn import *
import StoryKG_generator
from Queries4Text import *
from Queries4LinearizedGraph import *
import Queries4Text
# import SPARQLWrapper

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

    for i in [1,2,3,4,5,6,8,9,10,11,12]:
        t = globals()[f"textGeneration_Event{i}_{x}"](story)
        t = str(list(t))
        t = t.replace("[(rdflib.term.Literal('", "").replace("'),)]", "")
        t = t.replace('[(rdflib.term.Literal("','').replace('"),)]', '')
        #print(t)
        result += t
    #print(result)

    return result



def main(argv, arc):
    if arc!=3:
        raise ValueError("nr of Parameters is incorrect!")

    if argv[1] not in ["community","relation","random"] :
        #or argv[2] not in ['types','event','range', 'baseline_instances','baseline_classes']:
        raise ValueError("Error! Please enter a (valid) charachter picking method. (community,relation,random)")

    method = argv[1]
    heros=[]
    n = int(argv[2])
    for i in range(n):
        story,hero = gen_story(method)
        heros.append(hero)
        print(hero)
        story = story.serialize("./TESTING.ttl")

        #Creating the linearizations

            #Instance baseline
        linearized_baseline = Graph_Generator_baseline_instances(story)
        text_baseline = clear1(linearized_baseline)



        #Creating text
        event1str=textGeneration_Event1_1_NEW(story)
        print("TExt event 1:\n",event1str)





        if text_baseline == "":
            print("YOO")
            story = story.serialize(f"./TESTING_wrong{i}.ttl", )
        #print("\n final: \n",text_baseline)
    return None



"""def main(argv, arc):
    if arc!=4 or argv[1] not in ["community","relation","random"] :
            #or argv[2] not in ['types','event','range', 'baseline_instances','baseline_classes']:
        print("Error! Please enter a (valid) charachter picking method. (community,relation,random)")
        exit()
    method= argv[1]
    #semantic_given = argv[2]
    #n_kg_generated = int(argv[3])
    nr_inst = argv[3]


    data = []
    count = 0
    count_KG = 0
    #path = f'/Users/teresa/Documents/GitHub/GoTAutomyth_short/generated_output/events_{method_generation}'
    path = f'/GoTAutomyth_short/generated_output/events_{method_generation}'
    if os.path.exists(path)==False:
        os.mkdir(path)


    with open(f'generated_output/events_{method_generation}/{what}_events_{method_generation}.json', 'w', encoding='utf-8') as f:
        f.write('[')
        while count<n_kg_generated:
            dict = {}
            story=gen_story(method_generation)
            #print(type(story))

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
"""





if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
