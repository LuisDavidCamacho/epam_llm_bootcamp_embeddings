# Import necessary libraries
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
import torch

class BertEmbedding:

    def __init__(self):
        # Load pre-trained BERT model and tokenizer
        self.__tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.__model = BertModel.from_pretrained('bert-base-uncased')

    def get_word_vector(self, word):
        # Get word embedding
        inputs = self.__tokenizer(word, return_tensors='pt')
        outputs = self.__model(**inputs)
        embedding = outputs.last_hidden_state[:, 0, :]
        return embedding

    def get_sentence_vector(self, sentence):
        # Get sentece embedding
        inputs = self.__tokenizer(sentence, return_tensors='pt')
        outputs = self.__model(**inputs)
        embedding = outputs.pooler_output
        return embedding

    def get_word_similarity(self, word1, word2):
        input1 = torch.tensor(self.__tokenizer.convert_tokens_to_ids(self.__tokenizer.tokenize(word1))).unsqueeze(0)
        input2 = torch.tensor(self.__tokenizer.convert_tokens_to_ids(self.__tokenizer.tokenize(word2))).unsqueeze(0)

        with torch.no_grad():

            output1 = self.__model(input1)
            output2 = self.__model(input2)

            embeddings1 = output1.last_hidden_state[:, 0, :]
            embeddings2 = output2.last_hidden_state[:, 0, :]
        return cosine_similarity(embeddings1, embeddings2)