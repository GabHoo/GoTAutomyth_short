import json
import os

def create_linearized_KG(data): 
    """
    This function creates a linearized KG from the KG in the json file
    """
    concept_text = dict() #dictionary that maps the concept to the text
    #KG = []
    str = '' #string that contains the linearized KG
    for i in range(len(data['concepts'])): #for each concept in the KG we create a dictionary that maps the concept to the text
        if 'text' in data['concepts'][i]:
            concept_text[data['concepts'][i]['concept']] = data['concepts'][i]['text']
        elif 'link' in data['concepts'][i]: #if the concept is a link we map it to the link
            concept_text[data['concepts'][i]['concept']] = data['concepts'][i]['link']
        else:    #if the concept is not a link and it doesn't have text we map it to an empty string
            concept_text[data['concepts'][i]['concept']] = ''
            
    for i,j in zip(range(len(data['relations'])),range(len(concept_text))):
        str += concept_text[data['relations'][i]['s']]+' - '+data['relations'][i]['p']+' - '+concept_text[data['relations'][i]['o']]+' | '
        #KG.append(concept_text[data['relations'][i]['s']]+' - '+data['relations'][i]['p']+' - '+concept_text[data['relations'][i]['o']] )

    return str


def create_experiment_linearized(data): 
    """
    This function creates a dictionary that contains the story and the linearized KG
    """
    dict = {}
    dict['story'] = data['content'] 
    dict['Instances Knowledge Graph'] = create_linearized_KG(data)
    return dict


def dict_into_json(data):
    """
    This function creates a json file from a dictionary
    """
    with open('new_data.json', 'a') as f:

        new_KG = create_experiment_linearized(data)
        
        json.dump(new_KG, f, indent="")
        #f.write(',\n')

def main():
    """
    This function creates a json file that contains the linearized KG and the story
    """

    directory = 'data/annos_with_content/'
    with open('new_data.json', 'w') as f:
        f.write('[')
        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)



            with open(path) as g:
                try:
                    data = json.load(g) 
                    new_KG = create_experiment_linearized(data)
                    json.dump(new_KG, f, indent="") 
                    f.write(',\n')

                except BaseException as e:
                    print('The file contains invalid JSON')
                    print(path)
        f.write(']')
        f.close()

if __name__ == "__main__":
    main()