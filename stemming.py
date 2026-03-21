words=["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized"]

# Porter Stemmer
from nltk.stem import PorterStemmer
# stemming=PorterStemmer()
for word in words:
    print(word+"---->"+PorterStemmer().stem(word))

print(PorterStemmer().stem("Congratulations"))
"""
Output: 'congratul', Incorrect output
"""

# RegexpStemmer
from nltk.stem import RegexpStemmer

reg_stemmer=RegexpStemmer('ing$|s$|e$|able$', min=4)
print(reg_stemmer.stem('eating'))
print(reg_stemmer.stem('ingeating'))   # Didn't interpret correctly

# SnowballStemmer

from nltk.stem import SnowballStemmer

snowball_stemmer=SnowballStemmer('english')   # Argument: Specific Language
for word in words:
    print(word+"-->"+snowball_stemmer.stem(word))

"""
All of these Stemming techniques do not interpret correctly or 
that accurate. So we can go for different techniques.
"""