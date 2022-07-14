import math
import random
import numpy as np
import pandas as pd
import nltk
import w3_unittest

def load_data():
    with open("./data/en_US.twitter.txt", "r") as f:
        data = f.read()
    print("Data type:", type(data))
    print("Number of letters:", len(data))
    print("First 300 letters of the data")
    print("-------")
    print(data[0:300])
    print("-------")

    print("Last 300 letters of the data")
    print("-------")
    print(data[-300:])
    print("-------")
    
# UNIT TEST COMMENT: Candidate for Table Driven Tests 
### UNQ_C1 GRADED_FUNCTION: split_to_sentences ###
def split_to_sentences(data):
    """
    Split data by linebreak "\n"
    
    Args:
        data: str
    
    Returns:
        A list of sentences
    """
    ### START CODE HERE ###
    sentences = None
    ### END CODE HERE ###
    
    # Additional clearning (This part is already implemented)
    # - Remove leading and trailing spaces from each sentence
    # - Drop sentences if they are empty strings.
    sentences = [s.strip() for s in sentences]
    sentences = [s for s in sentences if len(s) > 0]
    
    return sentences  

# UNIT TEST COMMENT: Candidate for Table Driven Tests 
### UNQ_C8 GRADED FUNCTION: count_n_grams ###
def count_n_grams(data, n, start_token='<s>', end_token = '<e>'):
    """
    Count all n-grams in the data
    
    Args:
        data: List of lists of words
        n: number of words in a sequence
    
    Returns:
        A dictionary that maps a tuple of n-words to its frequency
    """
    
    # Initialize dictionary of n-grams and their counts
    n_grams = {}

    ### START CODE HERE ###
    
    # Go through each sentence in the data
    for sentence in data: # complete this line
        
        # prepend start token n times, and  append the end token one time
        sentence = n * [start_token] + sentence + [end_token]
        
        # convert list to tuple
        # So that the sequence of words can be used as
        # a key in the dictionary
        sentence = tuple(sentence)
        
        # Use 'i' to indicate the start of the n-gram
        # from index 0
        # to the last index where the end of the n-gram
        # is within the sentence.
        
        for i in range(len(sentence) - n+1): # complete this line

            # Get the n-gram from i to i+n
            n_gram = sentence[i:i+n]
            
            # check if the n-gram is in the dictionary
            if n_gram in n_grams: # complete this line with the proper condition
            
                # Increment the count for this n-gram
                n_grams[n_gram] += 1
            else:
                # Initialize this n-gram count to 1
                n_grams[n_gram] = 1
    
            ### END CODE HERE ###
    return n_grams

def main():
    # nltk.download('punkt')
    # nltk.data.path.append('.')
    # load_data()
    
    # test function count_n_grams
    # CODE REVIEW COMMENT: Outcome does not match expected outcome
    sentences = [['i', 'like', 'a', 'cat'],
                ['this', 'dog', 'is', 'like', 'a', 'cat']]
    print("Uni-gram:")
    print(count_n_grams(sentences, 1))
    print("Bi-gram:")
    print(count_n_grams(sentences, 2))
    
    print("debug")
    

if __name__ == '__main__':
    main()
    