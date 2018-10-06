class HashTags(object):
    
    def __init__(self):
        self.hashAllTags = dict()
    
    def addHashTag(self, hashTag):
        hashTag = hashTag.lower()
        if hashTag in self.hashAllTags.keys():
            self.hashAllTags[hashTag] += 1
            return
        self.hashAllTags[hashTag] = 1

    def addListOfHashTags(self, hashTags):
        for hashTag in hashTags:
            hashTag = hashTag.lower()
            if hashTag in self.hashAllTags.keys():
                self.hashAllTags[hashTag] += 1
                continue
            self.hashAllTags[hashTag] = 1

    def removeLowerValues(self, frequency):
        for key, value in self.hashAllTags.copy().items():
            if value < frequency:
                self.hashAllTags.pop(key)

    def Sort(self):
        self.hashAllTags = sorted(self.hashAllTags.items(), key=lambda value: value[1])

    def Reverse(self):
        self.hashAllTags = sorted(self.hashAllTags.items(), key=lambda value: value[1], reverse=True)
    
    def getHashTags(self):
        return (self.hashAllTags)