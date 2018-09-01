import json
import secret
import pymongo
from requests_oauthlib import OAuth1Session

class Follower(object):
    user_hashtags = set()

    def __init__(self, followerId):
        self.followerId = followerId

    def addHashTag(self, hashtag):
        self.user_hashtags.add(str(hashtag))

class Politician(Follower):
    users_followers = set()

    def __init__(self, politicianId, politicianName, politiciaParty):
        self.politicianId = politicianId
        self.politicianName = politicianName
        self.politiciaParty = politiciaParty

    def addFollowerId(self, followerId):
        self.users_followers.add(followerId)

class TwitterSearch(object):
    politiciansFollowers = set()

    def __init__(self):
        self.session = OAuth1Session(secret.API_KEY, secret.API_SECRET, secret.ACCESS_TOKEN, secret.ACCESS_TOKEN_SECRET)

    # user_id = ID do usuario
    # maxNumberOfPosts = quantidade de posts da timeline de user_id
    def getHashTagsFromTimeLine(self, user_id, maxNumberOfPosts):
        hashtags_list = []

        response = self.session.get("https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=" + str(user_id) + "&count=" + str(maxNumberOfPosts))    
        content = json.loads(response.content)
     
        for tweet in content:
            if 'entities' in tweet:
                hashtags = tweet['entities']['hashtags']
                
                if(len(hashtags) > 0):
                    for texts in hashtags:
                        hashtag = texts['text']
                        if(hashtag not in hashtags_list):
                            hashtags_list.append(hashtag)

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
            hashtags = self.getHashTagsFromTimeLine(followerId, maxNumberOfPosts)

            for hashtag in hashtags:
                follower.addHashTag(hashtag)
            self.politiciansFollowers.add(follower)
        return
        
client = TwitterSearch()
client.getHashTagsFromUserByPolitician(128372940, 10, 100)


#hashtags = client.getHashTagsFromUserByPolitician(128372940, 50, 4000)

for user in client.politiciansFollowers:
    print ("\nUser: %s" % user.followerId)
    for hashtag in user.user_hashtags:
        print (hashtag)
#    print(hashtag)