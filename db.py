import pymongo

class DataBase(object):
    
    def __init__(self):
        myClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = myClient["myPoliticianData"]
        self.politicians = self.mydb["Politicians"]

    def create(self, data):
        self.politicians.insert(data)

    def read(self):
        return

    def update(self):
        return

    def delete(self, data):
        self.politicians.delete(data)
