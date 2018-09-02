import json
import secret
from db import DataBase
from requests_oauthlib import OAuth1Session

class Follower(object):
    user_hashtags = set()

    def __init__(self, followerId):
        self.followerId = followerId

    def __str__(self):
        return "ID: " + str(self.followerId) + " Hashtags: " + self.get_hashtags()

    def get_hashtags(self):
        text = ""
        for hashtag in self.user_hashtags:
            text += hashtag
        return text


class Politician(Follower):
    users_followers = set()

    def __init__(self, politicianId, politicianName, politiciaParty):
        self.politicianId = politicianId
        self.politicianName = politicianName
        self.politiciaParty = politiciaParty

    def addFollowerId(self, followerId):
        self.users_followers.add(followerId)

class TwitterSearch(object):
    politiciansFollowers = []

    def __init__(self):
        self.session = OAuth1Session(secret.API_KEY, secret.API_SECRET, secret.ACCESS_TOKEN, secret.ACCESS_TOKEN_SECRET)

    # user_id = ID do usuario
    # maxNumberOfPosts = quantidade de posts da timeline de user_id
    def getHashTagsFromTimeLine(self, user_id, maxNumberOfPosts):
        hashtags_list = set()

        response = self.session.get("https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=" + str(user_id) + "&count=" + str(maxNumberOfPosts))    
        content = json.loads(response.content)
     
        for tweet in content:
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

            self.politiciansFollowers.append(follower)
        return

    def getPolitician(self):
        return self.politiciansFollowers
        
client = TwitterSearch()
client.getHashTagsFromUserByPolitician(128372940, 1000, 5000)
myDb = DataBase()

politicianData = client.getPolitician()
myDb.create(128372940, politicianData)

#hashtags = client.getHashTagsFromUserByPolitician(128372940, 50, 4000)

#for user in client.politiciansFollowers:
 #   print ("\nUser: %s" % user.followerId)
  #  for hashtag in user.user_hashtags:
   #     print (hashtag)
