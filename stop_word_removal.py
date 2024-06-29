from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
text = "Hello, this is a very useful book for deep learning"
words_tokens = word_tokenize(text)
text_without_stopwords = [word for word in word_tokens if not word in stopwords.words()]
print("".join(text_without_stopwords))

