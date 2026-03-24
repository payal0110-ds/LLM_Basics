import nltk
nltk.download('words')
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')

sentence="The Eiffel Tower was built from 1887 to 1889 by Gustave Eiffel, whose company specialized in building metal frameworks and structures."
words=nltk.word_tokenize(sentence)
tags=nltk.pos_tag(words)
print(tags)

# Diagram Draw
nltk.ne_chunk(tags).draw()

