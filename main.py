from twitter import *

dbName = "myPoliticianData"
dbCollection = "Politicians"
def testDb(politicianData):
    for user in politicianData:
        print(("Followers %s %s") % (user["_id"] , user["hashtags"]))

def main():
    #client = TwitterSearch()
    #client.getHashTagsFromUserByPolitician(128372940, 10, 100)
    myDb = DataBase(dbName, dbCollection)

    #politicianData = client.getPolitician()
    #myDb.create(128372940, politicianData)
    myDb.DropCollection()
    policicianData = myDb.read(128372940)
    testDb(policicianData)

if __name__ == "__main__":
    main()