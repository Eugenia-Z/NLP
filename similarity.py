import spacy
nlp = spacy.load("en_core_web_sm")
doc1 = nlp("Cricket is a sport where a team has 11 players")
doc2 = nlp("A football team consists of 11 players")
doc1.similarity(doc2)