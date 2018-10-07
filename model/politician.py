from follower import Follower

class Politician(Follower):
    
    def __init__(self, politicianId, politicianName, politiciaParty):
        self.politicianId = politicianId
        self.politicianName = politicianName
        self.politiciaParty = politiciaParty
        self.users_followers = set()

    def addFollowerId(self, followerId):
        self.users_followers.add(followerId)

    @staticmethod
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
            Politician("354095556","Fernando Haddad", "PT"),
            Politician("105155795", "Marina Silva", "Rede"),
            Politician("634712862", "Vera Lúcia", "PSTU")
        ]