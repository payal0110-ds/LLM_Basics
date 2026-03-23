'''
 We can create custom stop words along with the pre-defined stop words 
 given by NLTK.
'''
from nltk.corpus import stopwords

base_stop_words=set(stopwords.words('english'))
custom_words={"model","data","science","model"}

custom_stop_words=base_stop_words.union(custom_words)
print(len(base_stop_words))
print(custom_stop_words)
print(len(custom_stop_words))

# Reset to original NLTK stop words
final_stop_words_1=custom_stop_words-custom_words

# OR
final_stop_words_2=stopwords.words('english') 
