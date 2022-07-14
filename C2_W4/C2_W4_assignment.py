# Import Python libraries and helper functions (in utils2) 
import nltk
from nltk.tokenize import word_tokenize
import numpy as np
from collections import Counter
from utils2 import sigmoid, get_batches, compute_pca, get_dict
import w4_unittest
import re 
import json

nltk.download('punkt')
# Download sentence tokenizer
nltk.data.path.append('.')

def data_process(data_path, verbose=False):
    with open(data_path) as f:
        data = f.read()  #  Read in the data
    data = re.sub(r'[,!?;-]', '.',data) #  Punktuations are replaced by .
    data = nltk.word_tokenize(data) #  Tokenize string to words
    data = [ ch.lower() for ch in data if ch.isalpha() or ch == '.'] #  Lower case and drop non-alphabetical tokens
    if verbose:
        print("Number of tokens:", len(data),'\n', data[:15])  
    return data

def initialize_model(N,V, random_seed=1):
    '''
    Inputs: 
        N:  dimension of hidden vector 
        V:  dimension of vocabulary
        random_seed: random seed for consistent results in the unit tests
     Outputs: 
        W1, W2, b1, b2: initialized weights and biases
    '''
    
    np.random.seed(random_seed)
    # W1 has shape (N,V)
    W1 = np.random.rand(N,V)
    
    # W2 has shape (V,N)
    W2 = np.random.rand(V,N)
    
    # b1 has shape (N,1)
    b1 = np.random.rand(N,1)
    
    # b2 has shape (V,1)
    b2 = np.random.rand(V,1)
    
    return W1, W2, b1, b2

def softmax(z):
    '''
    Inputs: 
        z: output scores from the hidden layer
    Outputs: 
        yhat: prediction (estimate of y)
    '''
    # Calculate yhat (softmax)
    yhat = np.exp(z) / np.sum(np.exp(z),axis=0)
    return yhat

def forward_prop(x, W1, W2, b1, b2):
    '''
    Inputs: 
        x:  average one hot vector for the context 
        W1, W2, b1, b2:  matrices and biases to be learned
     Outputs: 
        z:  output score vector
    '''
    # Calculate h
    h = np.dot(W1,x)+b1
  
    # Apply the relu on h, 
    # store the relu in h
    h = np.maximum(0,h)

    # Calculate z
    z = np.dot(W2,h)+b2

    return z, h

def compute_cost(y, yhat, batch_size):
    
    # cost function 
    logprobs = np.multiply(np.log(yhat),y)
    cost = - 1/batch_size * np.sum(logprobs)
    cost = np.squeeze(cost)
    return cost

def back_prop(x, yhat, y, h, W1, W2, b1, b2, batch_size):
    '''
    Inputs: 
        x:  average one hot vector for the context 
        yhat: prediction (estimate of y)
        y:  target vector
        h:  hidden vector (see eq. 1)
        W1, W2, b1, b2:  matrices and biases  
        batch_size: batch size 
     Outputs: 
        grad_W1, grad_W2, grad_b1, grad_b2:  gradients of matrices and biases   
    '''
    # Compute l1 as W2^T (Yhat - Y)
    # and re-use it whenever you see W2^T (Yhat - Y) used to compute a gradient
    l1 = np.dot(W2.T, yhat - y)

    # Apply relu to l1
    l1 = np.maximum(0,l1)

    # compute the gradient for W1
    grad_W1 = 1/batch_size * np.dot(l1, x.T)

    # Compute gradient of W2
    grad_W2 = 1/batch_size * np.dot((yhat-y),h.T)
    
    # compute gradient for b1
    grad_b1 = 1/batch_size * np.sum(l1, axis=1, keepdims=True)

    # compute gradient for b2
    grad_b2 = 1/batch_size * np.sum((yhat-y), axis=1, keepdims=True)
    
    return grad_W1, grad_W2, grad_b1, grad_b2

def main():
    
    # Load the data: a text corpus from Shakespeare
    DATA_PATH = "/home/luc/Documents/dev/python/projects/nlp_coursera/C2_W4/data/shakespeare.txt"
    data = data_process(DATA_PATH,verbose=True)
    
    # Compute the frequency distribution of the words in the dataset (vocabulary)
    fdist = nltk.FreqDist(word for word in data)
    
    # get_dict creates two dictionaries, converting words to indices and viceversa.
    word2Ind, Ind2word = get_dict(data)
    V = len(word2Ind)
    
    
    
    return

if __name__ == '__main__':
    main()
    