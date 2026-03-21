# Convert Paragraph/corpus to sentences
from nltk import sent_tokenize

paragraph="""My name is Payal. I'm a Data Scientist and currently working 
in GA as a Data Scientist. My responsibilities are advance analysis, 
creating predictive models, developing NLP such as Chatbot, RAG models."""

sentences=sent_tokenize(paragraph)
print(sentences)
print(len(sentences))

# Convert paragraph to words

from nltk import word_tokenize

words=word_tokenize(paragraph)
print(words)
print(len(words))