def Graph_Generator(story):
    texts = []
    text = story.query("""
  CONSTRUCT { ?s ?p ?o . } 
  WHERE { VALUES ?p { rdf:type} ?s ?p ?o }
    }""")
    texts.append(text)
    return (text)

Graph_Generator(story_a_community_1.ttl)