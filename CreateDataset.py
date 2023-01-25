from StoryKG_generator import *
#from Queries4Text import *
from Queries4LinearizedGraph import *
import Queries4Text
# import SPARQLWrapper
from collections import Counter
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from rephrasingModule import rephrase
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






def random_formulation(story,tokenizer,model):
    texto = ""
    choice = []
    for e in range(1, 7):
        r = random.randint(1, 3)
        f = getattr(Queries4Text, f'textGeneration_Event{e}_{r}')
        combination = str(e)+str(r)
        choice.append(combination)
        result = f(story)
        #print(result)
        paraphrased_result=rephrase(result,tokenizer,model)
        #print(paraphrased_result)
        if result == "":
            raise "Excpetion event story text failed check testin.ttl"

        if e<6:
            paraphrased_result+=" "
        texto += paraphrased_result
  
    return texto,choice



def main(argv, arc):
    if arc!=4:
        raise ValueError("nr of Parameters is incorrect! NOTE FOR TERESA THERE IS ALSO NAME OF THE OUTPUT FOLDER TO ADD")

    if argv[1] not in ["community","relation","random"] :
        raise ValueError("Error! Please enter a (valid) charachter picking method. (community,relation,random)")

    method = argv[1]
    what = argv[2]
    outputfolder=argv[3]

    if what == 'train':
        n_kg_generated = 1000

    if what =='test':
        n_kg_generated = 100

    if what =='val':
        n_kg_generated = 100

    if what =='try':
        n_kg_generated = 1

    directory = f"{outputfolder}_events_new_ontology{method}"
  
       # Parent Directory path
    parent_dir = "generated_output"
    path = os.path.join(parent_dir, directory)
    if os.path.exists(path)==False:
        os.mkdir(path)

    heros = []
    choices = []
    tokenizer = AutoTokenizer.from_pretrained("./models/tokenizer/")
    model = AutoModelForSeq2SeqLM.from_pretrained("./models/Parahpraser")


    with open(f'generated_output/{directory}/{method}_{what}.json', 'w', encoding='utf-8') as f:
        

        f.write('[')
        for i in range(n_kg_generated):

            current_graph = {}
            story,hero = gen_story(method)

            heros.append(hero)
            story = story.serialize("./TESTING.ttl")

            #Generates the text
            label,choice = random_formulation(story,tokenizer,model)

            choices.append(choice)

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
    f.close()



    with open(f'generated_output/{directory}/{method}_{what}_choice.txt', 'a', encoding='utf-8') as s:
                    s.write(str(choices))



    herostats = Counter(heros)
    with open(f'generated_output/{directory}/herocounter_{what}.json', 'w', encoding='utf-8') as f:
        f.write(str(herostats))


    #print(herostats)
    print(f"Everything generated in generated_output/{directory}/{method}_{what}")



if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
