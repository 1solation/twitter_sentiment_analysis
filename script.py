import tweepy
from textblob import TextBlob

# obfuscate keys from code
lines = []                  # Declare an empty list
with open('./keys/consumer_key.txt', 'rt') as in_file:
    # Open file ./keys/consumer_keys.txt to enable reading of the data
    for line in in_file:  # loop over each line in in_file
        lines.append(line.rstrip('\n'))  # add to list & strip newline chars

# add key variables - keys file not commited for security reasons.
consumer_key = lines[0]
consumer_secret = lines[1]

access_token = lines[2]
access_token_secret = lines[3]

# authenticate with twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# enter the search term you want to search twitter for and analyse
search_term = 'brexit'

# search tweets for any string and store in public_tweets variable
public_tweets = api.search(search_term)


print('######################################################################')
print("### Here is what people are saying about '" +
    search_term + "' and how they are feeling ###")
print('######################################################################')
for tweet in public_tweets:
    print(tweet.text)
    # use TextBlob library to perform sentiment analysis on tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print('\n')
