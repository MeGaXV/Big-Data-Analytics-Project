#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tweepy
from tweepy import OAuthHandler

#Variables that contains the user credentials to access Twitter API 
api_key = "wTLNWBC5OwIGYZ1mO4hYgL2Db"
api_secret = "9zEr51MLfKC8hrwympTpvRaU2efM0LYrK3vlWjUyFs3z8ftiUj"
access_token = "710522218569191424-ECNhGIGkZq6RXuWS9WdNn3FYpVuLzA3"
access_secret = "HLsnS6tR3roPqEZNO7GxotMS8ij2U2snCskqpCeIRf9u2"


auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

args = ["google"]
api = tweepy.API(auth,timeout = 10)

query = args[0]
f = open("input/twitter.txt","w")

# this will stream based on the filter
if len(args) == 1:
    for status in tweepy.Cursor(api.search_tweets, q = query+" -filter:retweets",lang="en",result_type = "recent").items(100):
        f.write(status.text)
