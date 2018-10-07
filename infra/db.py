import pymongo

class DataBase(object):
    
    def __init__(self, dbName, collectionName):
        myClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.collectionName = collectionName
        self.dbName = dbName
        self.mydb = myClient[self.dbName]
        self.politicians = self.mydb[collectionName]

    def create(self, politician_id, data):
        for user in data:
                self.politicians[politician_id].insert({"id" : str(user.followerId), "Tweets: ": list(user.get_tweets()), "hashtags" : list(user.get_hashtags())})

    def read(self, politician_id):
        result = self.politicians[politician_id].find()
        return result

    def update(self):
        return

    def delete(self,politician_id, user):
        self.politicians[politician_id].remove({"_id" : str(user.followerId), "hashtags" : list(user.get_hashtags())})

    def DropCollection(self):
        self.mydb[self.dbName].drop()
        return
            
            