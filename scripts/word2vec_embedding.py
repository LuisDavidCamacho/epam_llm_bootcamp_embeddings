# Import necessary libraries
from gensim.models import KeyedVectors

class Word2VecEmbedding:

    def __init__(self, model_path):
        # download from https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g
        self.__model = KeyedVectors.load_word2vec_format(model_path, binary=True)    

    def get_word_vector(self, word):
        # Get word embedding
        return self.__model[word]

    # Get similarity between words
    def get_word_similarity(self, word1, word2):
        similarity = self.__model.similarity(word1, word2)
        return similarity

    def get_word_most_similar(self, word):
        # Find most similar words
        most_similar = self.__model.most_similar(word)
        return most_similar
