import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
words = ["act","acted","smiles","smile"]
for word in words:
    lemma = wordnet_lemmatizer.lemmatize(word)
print(lemma)