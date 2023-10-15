import gensim.downloader as api
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string

import numpy as np

model = KeyedVectors.load_word2vec_format('./models/glove.6B.50d.txt', binary=False, no_header=True)
stop_words = stopwords.words('english')

def phrase_finder(text, words_list):
    
    # Prepare the text: tokenize into words, remove punctuation, and convert to lowercase
    tokenized_text = [word.lower() for word in word_tokenize(text) if word not in string.punctuation and word.lower() not in stop_words]
    
    # Stemming
    stemmer = PorterStemmer()
    stemmed_text = [stemmer.stem(word) for word in tokenized_text]
    
    # Stem the words in the words_list too, to ensure consistency
    stemmed_words_list = [stemmer.stem(word) for word in words_list]
    
    def phrase_vector(phrase):
        words = word_tokenize(phrase.lower())
        word_vectors = [model[word] for word in words if word in model]
        if not word_vectors:
            return None  # Return None if no words in the phrase have vectors
        phrase_vector = np.mean(word_vectors, axis=0)
        return phrase_vector
    
    # Find Similar Words
    similar_words = {}
    for phrase in words_list:
        phrase_vec = phrase_vector(phrase)
        if phrase_vec is not None:
            # Finding similar words for each word in the phrase
            for word in word_tokenize(phrase.lower()):
                if word in model:
                    similar_words_for_word = [item[0] for item in model.most_similar(word, topn=10) if item[0] in stemmed_text]
                    # Combining the similar words found for each word in the phrase
                    similar_words[phrase] = similar_words.get(phrase, []) + similar_words_for_word
    
    print(similar_words)
    return similar_words

if __name__ == "__main__":
    phrase_finder(text, words_list)
