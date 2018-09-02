import pymongo

class DataBase(object):
    
    def __init__(self):
        myClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = myClient["myPoliticianData"]
        self.politicians = self.mydb["Politicians"]

    def create(self, politician_id, data):
        for user in data:
            if(len(user.user_hashtags) > 0):
                self.politicians[politician_id].insert({"_id" : user.followerId, "hashtags" : list(user.user_hashtags)})

    def read(self):
        return

    def update(self):
        return

    def delete(self, data):
        self.politicians.delete(data)
