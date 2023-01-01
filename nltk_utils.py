import nltk
import numpy as np
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

#Create a Stemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    #Tokenizing each sentence
    '''
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    '''

    return nltk.word_tokenize(sentence)

def stem(word):
    '''
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    '''
    return stemmer.stem(word.lower())

def chunk_of_words(tokenized_sentence, all_words):
    '''
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    '''
    #Stem each word in the sentence
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    #Initialize a bag with 0s for all words
    bag = np.zeros(len(all_words), dtype=np.float32)
    #Use enumarate to get index and the corresponding word 
    for index, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[index] = 1.0

    return bag