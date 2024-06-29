from nltk.stem import PorterStemmer
words = ["Compute", "Computer","Computing","Computed","Computes"]
ps = PorterStemmer()

for word in words:
    stem = ps.stem(word)
    print(stem)