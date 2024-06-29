import nltk
text = "This is a very useful book for NLP in Engligh by Usman Malik"
tokens = nltk.word_tokenize(text)
nltk.pos_tag(tokens)