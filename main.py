from twitter import *

dbName = "Politicians"

def testDb(politicianData):
    for user in politicianData:
        print(("Followers %s %s") % (user["_id"] , user["hashtags"]))

def getPoliticians():
    return [
            #Politician("73745956", "Alvaro Dias", "Podemos", "0.0563"),
            #Politician("989899804200325121", "Cabo Daciolo", "Patriota", "0.0039"),
            #Politician("33374761", "Ciro Gomes", "PDT", "0.0515"),
            #Politician("74215006", "Geraldo Alckmin", "PSDB", "0.1585"),
            #Politician("762402774260875265", "Guilherme Boulos", "PSOL", "0.0217"),
            #Politician("870030409890910210", "Henrique Meirelles", "MDB", "0.0101"),
            #Politician("128372940", "Jair Bolsonaro", "PSL", "0.2453"),
            #Politician("256730310", "Joao Amoedo", "Novo", "0.0322"),
            #Politician("164687650", "Joao Goulart Filho", "PPL". "0.002"),
            #Politician("73889361", "Jose Maria Eymael", "DC", "0.0037"),
            #Politician("354095556","Fernando Haddad", "PT", "0.1117"),
            #Politician("105155795", "Marina Silva", "Rede", "0.3046"),
            #Politician("634712862", "Vera Lucia", "PSTU", "0.002")
    ]


def main():
    
    politicians = getPoliticians()

    for politician in politicians:
        # politicianId = ID do usuario
        # maxNumberOfFollowers = quantidade de seguidores de politicianId
        # maxNumberOfPosts = quantidade de posts dos followers de politicianId
        client = TwitterSearch()
        client.getHashTagsFromUserByPolitician(politician.politicianId, 5000, 500)
        myDb = DataBase(dbName, politician.politicianName)
        myDb.create(politician.politicianId, client.getPolitician())

if __name__ == "__main__":
    main() 