paragraph="""
We used ‘Google Colab’ for data cleaning and preparation purpose where we imported the necessary libraries and the main dataset taken from the source website as ‘news_popularity’. To understand the dataset, we checked with the first 10 rows and checked the dimension of the dataset. To check the quality of the data we went through all the variables of the dataset and we consider variable ‘url’ is not required for our analysis, hence, we removed this specific variable from the dataset and now the dataset contains 60 variables. All the rest variables are in a numeric format which means they are continuous variables. But as many of these variables seem to have binary values which signifies that these are categorical variables in the form of numeric. 
In the data profiling process, which involves examining the data to identify any issues or inconsistencies, such as missing values, duplicate records, or data that is out of range, we applied relevant codes to inspect and we found no such missing values in the dataset. 
"""
# print(paragraph)

from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

# Step 1: Tokenize the corpus into sentences
sentences=sent_tokenize(paragraph)
# print(sentences)

# Stop words
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

#  Check Stopwords provided by NLTK

stop_words=stopwords.words('english')
# print(stop_words)
stop_words_german=stopwords.words('german')
# print(stop_words_german)

# Remove stop words and lemmatize the words from the given paragraph

for i in range(len(sentences)):
    words=word_tokenize(sentences[i])
    words=[WordNetLemmatizer().lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=" ".join(words)
print(sentences)