from Dice import *
class Configuration:
    configs = ["Category","Ones", "Twos","Threes","Fours","Fives","Sixes",
"Upper Scores","Upper Bonus(35)","Three of a kind", "Four of a kind", "Full House(25)",
"Small Straight(30)", "Large Straight(40)", "Yahtzee(50)","Chance","Lower Scores", "Total"]
    def getConfigs():
        return Configuration.configs
    def score(row, d):
        if 0 <= row < 6:
            return Configuration.scoreUpper(d, row+1)
        elif row == 8:
            return Configuration.scoreThreeOfAKind(d)
        elif row == 9:
            return Configuration.scoreFourOfAKind(d)
        elif row == 10:
            return Configuration.scoreFullHouse(d)
        elif row == 11:
            return Configuration.scoreSmallStraight(d)
        elif row == 12:
            return Configuration.scoreLargeStraight(d)
        elif row == 13:
            return Configuration.scoreYahtzee(d)
        elif row == 14:
            return Configuration.sumDie(d)
        else:
            return -1
    def scoreUpper(d, num):
        sum = 0
        for i in range(5):
            if d[i].getRoll() == num:
                sum += num
        return sum
    def scoreThreeOfAKind(d):#여기서 조건체크까지 해야한다.
        tmp = [0 for _ in range(7)]
        for i in range(5):
            tmp[d[i].getRoll()] += 1
        for i in tmp:
            if i == 3:
                return Configuration.sumDie(d)
        return 0
    def scoreFourOfAKind(d):
        tmp = [0 for _ in range(7)]
        for i in range(5):
            tmp[d[i].getRoll()] += 1
        for i in tmp:
            if i == 4:
                return Configuration.sumDie(d)
        return 0
    def scoreFullHouse(d):
        tmp = [0 for _ in range(7)]
        for i in range(5):
            tmp[d[i].getRoll()] += 1
        for i in tmp:
            if i == 3:
                for j in tmp:
                    if j == 2:
                        return 25
        return 0
    def scoreSmallStraight(d):
        tmp = [0 for _ in range(7)]
        for i in range(5):
            tmp[d[i].getRoll()] += 1
        for i in range(3):
            if tmp[i+1] >= 1 and tmp[i+2] >= 1 and tmp[i+3] >= 1 and tmp[i+4] >= 1:
                return 30
        return 0
    def scoreLargeStraight(d):
        tmp = [0 for _ in range(7)]
        for i in range(5):
            tmp[d[i].getRoll()] += 1
        for i in range(2):
            if tmp[i + 1] == 1 and tmp[i + 2] == 1 and tmp[i + 3] == 1 and tmp[i + 4] == 1 and tmp[i+5] == 1:
                return 40
        return 0
    def scoreYahtzee(d):
        if d[0].getRoll() == d[1].getRoll() == d[2].getRoll() == d[3].getRoll() == d[4].getRoll():
            return 50
        return 0
    def sumDie(d):
        sum = 0
        for i in range(5):
            sum += d[i].getRoll()
        return sum