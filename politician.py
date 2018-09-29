from follower import Follower

class Politician(Follower):
    
    def __init__(self, politicianId, politicianName, politiciaParty):
        self.politicianId = politicianId
        self.politicianName = politicianName
        self.politiciaParty = politiciaParty
        self.users_followers = set()

    def addFollowerId(self, followerId):
        self.users_followers.add(followerId)