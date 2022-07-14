import nltk                                # Python library for NLP
from nltk.corpus import twitter_samples    # sample Twitter dataset from NLTK
import matplotlib.pyplot as plt            # library for visualization
import random                              # pseudo-random number generator

import re                                  # library for regular expression operations
import string                              # for string operations

from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.stem import PorterStemmer        # module for stemming
from nltk.tokenize import TweetTokenizer   # module for tokenizing strings

# downloads sample twitter dataset.
nltk.download('twitter_samples')

# select the set of positive and negative tweets
all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

# plot the tweets repartition
# Declare a figure with a custom size
# fig = plt.figure(figsize=(5, 5))
# # labels for the two classes
# labels = 'Positives', 'Negative'
# # Sizes for each slide
# sizes = [len(all_positive_tweets), len(all_negative_tweets)] 
# # Declare pie chart, where the slices will be ordered and plotted counter-clockwise:
# plt.pie(sizes, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.axis('equal')  
# # Display the chart
# plt.show()

# show a positive and a negative tweet
# print positive in greeen
# print('\033[92m' + all_positive_tweets[random.randint(0,5000)])
# # print negative in red
# print('\033[91m' + all_negative_tweets[random.randint(0,5000)])

# Pre-processing steps
nltk.download('stopwords')

# Our selected sample. Complex enough to exemplify each step
tweet = all_positive_tweets[2277]
print(tweet)

print('\033[92m' + tweet)
print('\033[94m')

# remove old style retweet text "RT"
tweet2 = re.sub(r'^RT[\s]+', '', tweet)

# remove hyperlinks
tweet2 = re.sub(r'https?://[^\s\n\r]+', '', tweet2)

# remove hashtags
# only removing the hash # sign from the word
tweet2 = re.sub(r'#', '', tweet2)

print(tweet2)