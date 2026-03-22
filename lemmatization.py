from nltk.stem import WordNetLemmatizer

'''
pos:
Noun-n
verb-v
adjective-a
adverb-r
Default pos= 'n'
These 'pos' value converts the words according to the pos setting.
'''

words=["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized"]

lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize('walking',pos='v'))

for word in words:
    print(word+"-->"+lemmatizer.lemmatize(word))

for word in words:
    print(word+"-->"+lemmatizer.lemmatize(word,pos='v'))