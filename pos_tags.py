"""
Get pre-defined pos(part of speech) tags for any words in a 
sentence/paragraph.
"""
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
import nltk
nltk.download('averaged_perceptron_tagger') 

paragraph="""Prior to the research aspect, it’s essential to get some terminologies and notions. This insight will improve our comprehension of the current study. As we already mentioned about EEG signals in our literature review. But how the signal data gets stored and accessed, we have to understand first. """

# Tokenization to sentences
sentences=sent_tokenize(paragraph)
# print(sentences)
for i in range(len(sentences)):
    words=word_tokenize(sentences[i])
    words=[word for word in words if word not in set(stopwords.words('english'))]
    # It's optional to remove stop words
    posTags=pos_tag(words)
    print(posTags)

"""
By Pos tags, we can understand each words grammatical role.
"""