import json
import secret
from requests_oauthlib import OAuth1Session

class TwitterSearch(object):

    def __init__(self):
        self.session = OAuth1Session(secret.API_KEY, secret.API_SECRET, secret.ACCESS_TOKEN, secret.ACCESS_TOKEN_SECRET)

    # user_id = ID do usuario
    # count = quantidade de posts da timeline de user_id
    def get_user_hashtags(self, user_id, count):
        hashtags_list = []

        response = self.session.get("https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=" + str(user_id) + "&count=" + str(count))    
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

    # user_id = ID do usuario
    # count = quantidade de amigos de user_id
    def get_user_friends_id(self, user_id, count):

        response = self.session.get("https://api.twitter.com/1.1/followers/ids.json?user_id=" + str(user_id) + "&count=" + str(count))    
        content = json.loads(response.content)

        if 'errors' in content:
            for errors in content['errors']:
                message = errors['message']
                code = errors['code']
                print("Message: " + message + " Code: " + str(code))
            return []
        else:
            return content['ids']

    # user_id = ID do usuario
    # followers = quantidade de seguidores de user_id
    # posts = quantidade de posts dos followers de user_id
    def get_user_friends_hashtags(self, user_id, followers, posts):
        hashtags_list = []
        friends_id = self.get_user_friends_id(user_id, followers)

        for id in friends_id:
            hashtags = self.get_user_hashtags(id, posts)

            for hashtag in hashtags:
                if(hashtag not in hashtags_list):
                    hashtags_list.append(hashtag)
                    
        return hashtags_list

            

client = TwitterSearch()
hashtags = client.get_user_friends_hashtags(128372940, 50, 4000)

for hashtag in hashtags:
    print(hashtag)