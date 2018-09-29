import json
import secret
from db import DataBase
from follower import Follower
from politician import Politician
from hashtag import HashTags
from requests_oauthlib import OAuth1Session
from collections import OrderedDict

class TwitterSearch(object):
    
    def __init__(self):
        self.session = OAuth1Session(secret.API_KEY, secret.API_SECRET, secret.ACCESS_TOKEN, secret.ACCESS_TOKEN_SECRET)
        self.politiciansFollowers = set()

    # user_id = ID do usuario
    # maxNumberOfPosts = quantidade de posts da timeline de user_id
    def getHashTagsFromTimeLine(self, user_id, maxNumberOfPosts):
        hashtags_list = set()

        response = self.session.get("https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=" + str(user_id) + "&count=" + str(maxNumberOfPosts))    
        content = json.loads(response.content)
 
        # 16 de agosto - 24 de setembro
        for tweet in content:
            if 'created_at' in tweet:
                date = tweet.get("created_at").split()
          
                month = date[1]
                day = int(date[2])
                year = int(date[5])

                print(date)
                
                if (month == "Aug" and day >= 16 and year == 2018) or (month == "Sep" and day <= 24 and year == 2018):
                    if 'entities' in tweet:
                        hashtags = tweet['entities']['hashtags']
                        
                        if(len(hashtags) > 0):
                            for texts in hashtags:
                                hashtag = texts['text']
                                hashtags_list.add(hashtag)
            

        return hashtags_list

    # politicianId = ID do usuario
    # maxNumberOfFollowers = quantidade de amigos de user_id
    def getPoliticianFollowers(self, politicianId, maxNumberOfFollowers):

        response = self.session.get("https://api.twitter.com/1.1/followers/ids.json?user_id=" + str(politicianId) + "&count=" + str(maxNumberOfFollowers))    
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

            self.politiciansFollowers.add(follower)
        return

    def getPolitician(self):
        return self.politiciansFollowers

