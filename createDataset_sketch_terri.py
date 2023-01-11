from StoryKG_gen_reborn import *
import StoryKG_generator
#from Queries4Text import *
from Queries4LinearizedGraph import *
import Queries4Text
# import SPARQLWrapper
from collections import Counter
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
    texto = ""
    choice = []
    for e in range(1, 7):
        r = random.randint(1, 3)
        f = getattr(Queries4Text, f'textGeneration_Event{e}_{r}')
        combination = int(str(e)+str(r))
        choice.append(combination)
        result = f(story)

        if result == "":
            raise "Excpetion event story text failed check testin.ttl"

        texto += result
  
    return texto,choice



def main(argv, arc):
    if arc!=4:
        raise ValueError("nr of Parameters is incorrect! NOTE FOR TERESA THERE IS ALSO NAME OF THE OUTPUT FOLDER TO ADD")

    if argv[1] not in ["community","relation","random"] :
        raise ValueError("Error! Please enter a (valid) charachter picking method. (community,relation,random)")

    method = argv[1]
    heros=[]
    what = argv[2]
    outputfolder=argv[3]

    if what == 'train':
        n_kg_generated = 500

    if what =='test':
        n_kg_generated = 50

    if what =='val':
        n_kg_generated = 50

    if what =='try':
        n_kg_generated = 3

    directory = f"{outputfolder}_events_new_ontology{method}"
  
       # Parent Directory path
    parent_dir = "generated_output"
    path = os.path.join(parent_dir, directory)
    if os.path.exists(path)==False:
        os.mkdir(path)


    with open(f'generated_output/{directory}/{method}_{what}.json', 'w', encoding='utf-8') as f:
        

        f.write('[')
        for i in range(n_kg_generated):

            current_graph = {}
            story,hero = gen_story(method)

            heros.append(hero)
            story = story.serialize("./TESTING.ttl")

            #Generates the text
            label,choice = random_formulation(story)
            choice = str(choice)
            with open(f'generated_output/{directory}/{method}_{what}_choice.txt', 'a', encoding='utf-8') as s:
                s.write(choice)


            current_graph["story"]=label


            #Creating the linearizations

            current_graph['Instances Knowledge Graph'] = clear1(Graph_Generator_baseline_instances(story))
            current_graph['Class Knowledge Graph'] = clear1(Graph_Generator_baseline_class(story))
            current_graph['Types Knowledge Graph'] = clear1(Graph_Generator_types(story))
            current_graph['Range Knowledge Graph'] = clear1(Graph_Generator_range(story))
            current_graph['Event Knowledge Graph'] = clear1(Graph_Generator_event(story))
            #current_graph['Ontology Knowledge Graph'] = clear1(Graph_Generator_baseline_class(story)) + clear1(Graph_Generator_baseline_instances(story)) + clear1(Graph_Generator_types(story))
            current_graph['Ontology Knowledge Graph'] = clear1(Graph_Generator_baseline_class(story)) +  clear1(Graph_Generator_types(story))
            json.dump(current_graph, f, ensure_ascii=False, indent="")
            if i != n_kg_generated-1:
                f.write(',')
        f.write(']')

    herostats = Counter(heros)
    with open(f'generated_output/{directory}/herocounter_{what}.json', 'w', encoding='utf-8') as f:
        f.write(str(herostats))


    print(herostats)



if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
