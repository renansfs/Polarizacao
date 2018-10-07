from model.politician import Politician
from infra.db import DataBase
from model.hashtag import HashTags
from util.writer import Writer
from graph import Graph
import csv

dbName = "Politicians"

def getHashtags(offset):
    politicians = Politician.getPoliticians()    
    myHashtags = HashTags()
    writer = Writer()
    
    for politician in politicians:
        myDb = DataBase(dbName, politician.politicianName)
        political = myDb.read(politician.politicianId)
        
        for followers in political:
            hashtags = followers["hashtags"]
            
            for hashtag in hashtags:
                myHashtags.addHashTag(hashtag)

    myHashtags.setOffset(offset)
    myHashtags.Sort()

    writer.toCSV("hashtag_data.csv", myHashtags.getHashTags())

def main():
    #getHashtags(50)

    myGraph = Graph()
    myGraph.createNode()

if __name__ == "__main__":
    main() 