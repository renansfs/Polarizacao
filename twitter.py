import json
import secret
import time
from db import DataBase
from follower import Follower
from politician import Politician
from hashtag import HashTags
from requests_oauthlib import OAuth1Session
from collections import OrderedDict

class TwitterSearch(object):
    
    def Request(self, id, maxNumber, typeRequest):
        status = 429
        timeout = 60
        while status == 429:
            if typeRequest == 0:
                response = self.session.get("https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=" + str(id) + "&count=" + str(maxNumber))    
            elif typeRequest == 1:
                response = self.session.get("https://api.twitter.com/1.1/followers/ids.json?user_id=" + str(id) + "&count=" + str(maxNumber))
            status = response.status_code
            if status == 429:
                time.sleep(60)
                print("Limit Exceeded")

        return response

    def __init__(self):
        self.session = OAuth1Session(secret.API_KEY, secret.API_SECRET, secret.ACCESS_TOKEN, secret.ACCESS_TOKEN_SECRET)
        self.politiciansFollowers = set()

    def isTime(self, date):
        Aug = (16, 31)
        Sep = (1, 24)
        months = {'Aug': Aug,'Sep': Sep}

        sDate = date.split(" ")
        day = sDate[2]
        month = sDate[1]
        year = sDate[5]
        
        if month in months:
            low, high = months[month]
            if low <= int(day) <= high and year == "2018": 
                return True
        return False

    def getTweetsFromTimeLine(self, user_id, maxNumberOfPosts):
        tweets_list = set()

        response = self.Request(user_id, maxNumberOfPosts, 0)
        content = json.loads(response.content)
        print ("Status Code: %s User: %s \n" % (response.status_code, user_id))
        if response.status_code != 200:          
            return []
        
        for tweet in content:
                if self.isTime(tweet['created_at']) is True:
                    tweets_list.add(str(tweet))
        return tweets_list

    # user_id = ID do usuario
    # maxNumberOfPosts = quantidade de posts da timeline de user_id
    def getHashTagsFromTimeLine(self, user_id, maxNumberOfPosts):
        hashtags_list = set()

        response = self.Request(user_id, maxNumberOfPosts, 0)    
        content = json.loads(response.content)
     
        for tweet in content:
            if 'entities' in tweet:
                hashtags = tweet['entities']['hashtags']
                
                if(len(hashtags) > 0) and self.isTime(tweet['created_at']) is True:
                    for texts in hashtags:
                        hashtag = texts['text']
                        hashtags_list.add(hashtag)
        return hashtags_list

    # politicianId = ID do usuario
    # maxNumberOfFollowers = quantidade de amigos de user_id
    def getPoliticianFollowers(self, politicianId, maxNumberOfFollowers):

        response = self.Request(politicianId, maxNumberOfFollowers, 1)    
        content = json.loads(response.content)
  
        if 'errors' in content:
            for errors in content['errors']:
                message = errors['message']
                code = errors['code']
                print("Message: " + message + " Code: " + str(code))
            return []
        else:
            return content['ids']

    # politicianId = ID do usuario
    # maxNumberOfFollowers = quantidade de seguidores de politicianId
    # maxNumberOfPosts = quantidade de posts dos followers de politicianId
    def getHashTagsFromUserByPolitician(self, politicianId, maxNumberOfFollowers, maxNumberOfPosts):
        politicianFollowersId = self.getPoliticianFollowers(politicianId, maxNumberOfFollowers)

        for followerId in politicianFollowersId:
            follower = Follower(followerId)
            follower.user_hashtags = self.getHashTagsFromTimeLine(followerId, maxNumberOfPosts)
            #follower.user_tweets = self.getTweetsFromTimeLine(followerId, maxNumberOfPosts)
            self.politiciansFollowers.add(follower)
        return

    def getPolitician(self):
        return self.politiciansFollowers

