import scripts.bert_embedding as be
import scripts.word2vec_embedding as we

def init_word2vec(model):
    if not model:
        # Load pre-trained Word2Vec model
        path = "./model/bin/word2vec.bin"
        model = we.Word2VecEmbedding(path)
    return model

def init_bert(model):
    if not model:
        # Load pre-trained Bert model
        model = be.BertEmbedding()
    return model


if __name__ == '__main__':
    option = ''
    word2vec_model = None
    bert_model = None

    while option.lower() != 'bye':
        print('choose the option to try:')
        print('\t word2vec exmaple')
        print('\t bert example')
        option = input(':>')

        if option.lower() == 'word2vec':
            word2vec_model = init_word2vec(word2vec_model)
            print('choose the option to try:')
            print('1. word embedding')
            print('2. word similarity')
            print('3. word most similar')
            option = input(':>')
            if option == '1':
                word = input('wirte a word: ')
                embedding_vector = word2vec_model.get_word_vector(word)
                print(f'The embedding for the word: {word} is: {embedding_vector}')
            elif option == '2':
                word1 = input('wirte word1: ')
                word2 = input('wirte word2: ')
                score = word2vec_model.get_word_similarity(word1, word2)
                print(f'The similarity score between {word1} and {word2} is: {score}')
            elif option == '3':
                word = input('wirte a word: ')
                closest = word2vec_model.get_word_most_similar(word)
                print(f'The closest word to: {word} is: {closest}')
            else:
                print('invalid option')
        elif option.lower() == 'bert':
            bert_model = init_bert(bert_model)
            print('choose the option to try:')
            print('1. word embedding')
            print('2. word similarity')
            option = input(':>')
            if option == '1':
                word = input('wirte a word: ')
                embedding_vector = bert_model.get_word_vector(word)
                print(f'The embedding for the word: {word} is: {embedding_vector}')
            elif option == '2':
                word1 = input('wirte a word: ')
                word2 = input('wirte a word: ')
                score = bert_model.get_word_similarity(word1, word2)
                print(f'The similarity score between {word1} and {word2} is: {score}')
            else:
                print('invalid option')