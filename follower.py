class Follower(object):

    def __init__(self, followerId):
        self.followerId = followerId
        self.user_hashtags = set()
        self.user_tweets = set()

    def __str__(self):
        return "ID: " + str(self.followerId) + " Hashtags: " + str(self.get_hashtags())[:]

    def get_hashtags(self):
        return list(self.user_hashtags)

    def get_tweets(self):
        return list(self.user_tweets)