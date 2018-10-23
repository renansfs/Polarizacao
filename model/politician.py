from model.follower import Follower

class Politician(Follower):
    
    def __init__(self, politicianId, politicianName, politiciaParty, totalFollowers):
        self.politicianId = politicianId
        self.politicianName = politicianName
        self.politiciaParty = politiciaParty
        self.totalFollowers = totalFollowers
        self.users_followers = set()

    def addFollowerId(self, followerId):
        self.users_followers.add(followerId)

    @staticmethod
    def getPoliticians():
        return [
            Politician("73745956", "Alvaro Dias", "Podemos", "924"),
            Politician("989899804200325121", "Cabo Daciolo", "Patriota", "64"),
            Politician("33374761", "Ciro Gomes", "PDT", "845"),
            Politician("74215006", "Geraldo Alckmin", "PSDB", "2603"),
            Politician("762402774260875265", "Guilherme Boulos", "PSOL", "356"),
            Politician("870030409890910210", "Henrique Meirelles", "MDB", "166"),
            Politician("128372940", "Jair Bolsonaro", "PSL", "4027"),
            Politician("256730310", "Joao Amoedo", "Novo", "528"),
            Politician("164687650", "Joao Goulart Filho", "PPL", "4"),
            Politician("73889361", "Jose Maria Eymael", "DC", "62"),
            Politician("354095556","Fernando Haddad", "PT", "1833"),
            Politician("105155795", "Marina Silva", "Rede", "5000"),
            Politician("634712862", "Vera Lucia", "PSTU", "4")
        ]