from politician import Politician
from db import DataBase
from hashtag import HashTags
import csv

dbName = "Politicians"

def main():
    politicians = Politician.getPoliticians()    
    myHashtags = HashTags()
    
    for politician in politicians:
        myDb = DataBase(dbName, politician.politicianName)
        political = myDb.read(politician.politicianId)
        
        for followers in political:
            hashtags = followers["hashtags"]
            
            for hashtag in hashtags:
                myHashtags.addHashTag(hashtag)

    myHashtags.setOffset(50)
    myHashtags.Sort()

    with open("hashtag_data.csv", "w") as csvFile:
        writer = csv.writer(csvFile)

        for hashtag in myHashtags.getHashTags():
            row = [hashtag[0], hashtag[1]]
            writer.writerow(row)

    csvFile.close()

if __name__ == "__main__":
    main() 