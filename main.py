from twitter import *

dbName = "Politicians"

def testDb(politicianData):
    for user in politicianData:
        print(("Followers %s %s") % (user["_id"] , user["hashtags"]))

def getPoliticians():
    return [
        Politician("73745956", "Alvaro Dias", "Podemos"),
        Politician("989899804200325121", "Cabo Daciolo", "Patriota"),
        Politician("33374761", "Ciro Gomes", "PDT"),
        Politician("74215006", "Geraldo Alckmin", "PSDB"),
        Politician("762402774260875265", "Guilherme Boulos", "PSOL"),
        Politician("870030409890910210", "Henrique Meirelles", "MDB"),
        Politician("128372940", "Jair Bolsonaro", "PSL"),
        Politician("256730310", "João Amoêdo", "Novo"),
        Politician("164687650", "João Goulart Filho", "PPL"),
        Politician("73889361", "José Maria Eymael", "DC"),
        Politician("59915378", "Luiz Inácio Lula da Silva", "PT"),
        Politician("105155795", "Marina Silva", "Rede"),
        Politician("634712862", "Vera Lúcia", "PSTU")
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