from twitter import *

dbName = "myPoliticianData"
dbCollection = "Politicians"
def testDb(politicianData):
    for user in politicianData:
        print(("Followers %s %s") % (user["_id"] , user["hashtags"]))

def getPoliticians():
    return [73745956, 989899804200325121, 33374761, 74215006, 762402774260875265,
        870030409890910210, 128372940, 256730310, 164687650, 73889361, 59915378,
        105155795, 634712862]

def main():
    client = TwitterSearch()
    #client.getHashTagsFromUserByPolitician(128372940, 10, 100)
    myDb = DataBase(dbName, dbCollection)

    #politicianData = client.getPolitician()
    #myDb.create(128372940, politicianData)
    #policicianData = myDb.read(128372940)
    #testDb(policicianData)
    politicians = getPoliticians()

    for politician in politicians:
        client.getHashTagsFromUserByPolitician(politician, 2000, 4000)
        myDb.create(politician, client.getPolitician())

if __name__ == "__main__":
    main() 