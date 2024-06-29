from pywsd import disambiguate
from nltk import sent_tokenize
text = "I live on the bank of a river"
text2 = "I withdrew some money from my bank"
for sent in sent_tokenize(text):
    print(disambiguate(sent, prefersNone = True))
for sent in sent_tokenize(text2):
    print(disambiguate(sent, prefersNone=True))