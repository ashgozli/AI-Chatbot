import json
from nltk_utils import tokenize, stem, chunk_of_words
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

with open('Ecommerce_Intents.json', 'r') as f:
    intents = json.load(f)

#All words(x) and their corresponding tags(y) would be placed in these lists
all_words = []
tags = []

#A list a tuple of words(x) and their tags(y) 
xy = []

#Loop through each sentence in the intents and patterns in json
for intent in intents['intents']:
    tag = intent['responses']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

#Stem all words and disregard all the ignore_words specified 
ignore_words = ['?', '!', '.']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(tags)
print(tags)

X_train = []
y_train = []
for (pattern_sentence, tag) in xy:
    bag = chunk_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tags.index(tag)
    y_train.append(label) # Only want class labels: CrossEntropyLoss

X_train = np.array(X_train)
y_train = np.array(y_train)

class ChatDataSet(Dataset):
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    #dataset[idx]
    def __getitem__ (self, index):
        return self.x_data[index], self.y_data[index]
        
    def __len__ (self):
        return self.n_samples

#Hyperparameter
batch_size = 8

dataset = ChatDataSet()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=2)

