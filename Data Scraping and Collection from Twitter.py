#!/usr/bin/env python
# coding: utf-8

# Data collection:
# To collect tweets related to the Qatar 2022 FIFA World Cup, we can use Twitter's API or third-party tools such as Tweepy, Twython, or Twitter-Search-API. We can filter tweets by location, language, and time to ensure that we only collect relevant tweets from the target audience. It is also essential to clean and preprocess the data to remove noise, irrelevant information, and duplicates before analyzing it.
# 
# Evaluation metrics:
# To evaluate the performance of our sentiment analysis model, we can use metrics such as accuracy, precision, recall, F1-score, and confusion matrix. We can also calculate the sentiment polarity score, which is a numerical representation of the sentiment expressed in a tweet, to quantify the sentiment trends over time.
# 
# Ethical considerations:
# When analyzing sentiment data, it is essential to consider ethical and privacy concerns such as data protection, bias, and misinterpretation. We need to ensure that the data collected is anonymous, and we do not disclose any sensitive or personal information that could violate the privacy of individuals. We should also be aware of the potential bias in the data collection and analysis process, and take steps to mitigate it, such as using diverse data sources and involving multiple annotators to label the sentiment. Finally, we should be careful not to misinterpret or manipulate the sentiment data to avoid spreading false information or influencing public opinion.

# # Data Scraping and Collection

# Here is an example code using Tweepy library to collect tweets related to the Qatar 2022 FIFA World Cup:
# 
# 

# In[4]:


import tweepy
import pandas as pd


# In[2]:


pip install tweepy


# In[ ]:





# # Twitter-Search-API.

# In[5]:


# Twitter API credentials
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIxvmAEAAAAAAOAFgLXFBjrZTO3jqVDFkI%2FtFJQ%3DgXDISYs9WZ1SXtx1V1Ap3vfuoeZADSB0z3zQ9bsdhi1mCWLhrA"
consumer_key = "kikFABTXVWTjfHPzPpCvIdSgw"
consumer_secret = "Xe3JYx2H4LjcI67VYeWZQs2UqGOWs35sFZhkQ1KxFpibOstSge"


# In[ ]:





# In[6]:


# setup authentication with Twitter API
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)


# In[ ]:





# In[7]:


# create Tweepy API object
api = tweepy.API(auth, wait_on_rate_limit=True)


# In[ ]:





# In[8]:


# specify the search query and the number of tweets to retrieve
query = "#FIFAWorldCup2022 OR #Qatar2022 OR #WorldCup2022"
date_since = "2022-11-20" # when the world cup started
date_until = "2022-12-18"# when the world cup ended
num_tweets = 100000 # how many entries or tweets to get
lang = "en" # type of language to fetch


# The Twitter API has rate limits, which may limit the number of tweets you can retrieve in a certain period of time. This can result in the API returning fewer tweets than the number you requested.
# 
# You can try breaking up your request into smaller batches or waiting some time before making another request to get more tweets. Additionally, you can try using different search criteria to get more relevant results.

# In[ ]:





# In[43]:


# search for tweets with the specified query
# tweets = api.search_tweets(q=query, count=num_tweets, lang=lang, tweet_mode='extended')


# In[ ]:





# In[9]:


# Define list to store tweets
tweets = []

# Fetch tweets
while len(tweets) < 1000:
    new_tweets = api.search_tweets(q=query, tweet_mode="extended", count=100, lang=lang)
    if not new_tweets:
        print("No tweets found")
        break
    tweets.extend(new_tweets)
    print(f"Number of tweets collected: {len(tweets)}")

print(f"Total number of tweets collected: {len(tweets)}")


# In[ ]:





# In[10]:


def fetchMoreTweets(num=100, verbose=False):
    # Define list to store tweets
    tweets = []

    # Fetch tweets
    while len(tweets) < num:
        new_tweets = api.search_tweets(q=query, tweet_mode="extended", count=100)
        if not new_tweets:
            if not verbose:
                print("No tweets found")
            break
        tweets.extend(new_tweets)
        if not verbose:
            print(f"Number of tweets collected: {len(tweets)}")

    if not verbose:
        print(f"Total number of tweets collected: {len(tweets)}")
    print('done')
    return tweets


# In[11]:


tweets = fetchMoreTweets(num=5);


# In[ ]:


# output the first 5 tweets
tweets[:5]


# In[ ]:





# In[51]:


# Store tweets in a pandas dataframe
tweet_data = [[tweet.id_str, tweet.created_at, tweet.full_text, tweet.user.screen_name] for tweet in tweets]


# In[52]:


# output the first 5 tweets
tweet_data[:5]


# In[ ]:





# In[53]:


# Store tweets in a pandas dataframe
df = pd.DataFrame(tweet_data, columns=['id', 'created_at', 'text', 'username'])


# In[54]:


# display df
df.head()


# In[55]:


df.info()


# In[ ]:





# In[ ]:





# In[56]:


# save tweets
df.to_csv('qatar2022_tweets.csv', index=False)


# In[ ]:





# In[ ]:





# `summary`
# 
# In this code, we first authenticate to the Twitter API using our API credentials. Then, we define the search query and parameters, such as the keywords to search for, the date range, the language, and the number of tweets to collect. We use the Cursor object to iterate over the search results and collect the tweets. Finally, we store the tweet data in a Pandas dataframe and save it as a CSV file.

# In[ ]:





# In[ ]:




