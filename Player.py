class Player:
    UPPER = 6  # upper category 6개
    LOWER = 7  # lower category 7개
    def __init__(self, name):
        self.name = name
        self.scores = [0 for i in range(self.UPPER+self.LOWER)] #category
        self.used = [False for i in range(self.UPPER+self.LOWER)] #category
        self.bonus = 0
    def setScore(self, score, index):
        self.scores[index] = score
    def setAtUsed(self, index):
        self.used[index] = True
    def getUpperScore(self):
        sum = 0
        for i in range(self.UPPER):
            sum += self.scores[i]
        self.upperScore = sum
        return self.upperScore
    def getLowerScore(self):
        sum = 0
        for i in range(self.LOWER):
            sum += self.scores[self.UPPER + i]
        self.lowerScore = sum
        return self.lowerScore
    def getUsed(self, index):
        return self.used[index]
    def getTotalScore(self):
        sum = 0
        for i in range(self.LOWER + self.UPPER):
            sum += self.scores[i]
        self.totalScore = sum
        return self.totalScore
    def toString(self):
        return self.name
    def allLowerUsed(self):
        for i in range(6, 13):
            if self.used[i] == False:
                return False
        return True
    def allUpperUsed(self):
        for i in range(self.UPPER):
            if self.used[i] == False:
                return False
        return True