from tkinter import *
from tkinter import font
import tkinter.messagebox
from Player import *
from Dice import *
from Configuration import *
class YahtzeeBoard:
    UPPERTOTAL = 6
    UPPERBONUS = 7
    LOWERTOTAL = 15
    TOTAL = 16
    dice = []
    diceButtons = []
    fields = []
    players = []
    numPlayers = 0
    player = 0
    round = 0
    roll = 0
    undo = []#?????????????????????????????????????????????????????????????????????????????????????????????????????
    def initPlayers(self):
        self.pwindow = Tk()
        self.pwindow.title("Ready")
        self.TempFont = font.Font(size=16, weight="bold", family="Consolas")
        self.label = []
        self.entry = []
        self.label.append(Label(self.pwindow, text="플레이어 수", font=self.TempFont))
        self.label[0].grid(row=0, column=0)
        for i in range(1, 11):
            self.label.append(Label(self.pwindow, text="플레이어"+str(i)+"이름",\
                                    font=self.TempFont))
            self.label[i].grid(row=i, column=0)
        for i in range(11):
            self.entry.append(Entry(self.pwindow, font = self.TempFont))
            self.entry[i].grid(row=i, column=1)
        Button(self.pwindow, text="Yahtzee 플레이어 설정 완료",\
               font=self.TempFont, command=self.playerNames).grid(row=11, column=0)
        self.pwindow.mainloop()
    def playerNames(self):
        self.numPlayers = int(self.entry[0].get())
        for i in range(1, self.numPlayers+1):
            self.players.append(Player(str(self.entry[i].get())))
        self.pwindow.destroy()
        self.initInterface()
    def undo(self):
        for i in range(5):
            self.diceButtons[i]["state"] = "normal"
            self.diceButtons[i]["bg"] = "white"
    def rollDiceListener(self):#주사위 굴리기 버튼 누르면
        for i in range(5):
            if self.diceButtons[i]["state"] != "disabled":
                self.dice[i].rollDie()
                self.diceButtons[i].configure(text=str(self.dice[i].getRoll()))
        self.undo()
        if self.roll == 0 or self.roll == 1:
            self.roll += 1
            self.bottomLabel.configure(text="주사위 선택 후 ReRoll/카테고리 선택")
        elif self.roll == 2:
            self.bottomLabel.configure(text="카테고리를 선택하세요")
            self.rollDice["state"] = "disabled"
            self.rollDice["bg"] = "light gray"
            for i in range(5):
                self.diceButtons[i]["state"] = "disabled"
                self.diceButtons[i]["bg"] = "light gray"
    def diceListener(self, row):#각 주사위의 버튼 비활성화
        if self.roll >= 1:
            self.diceButtons[row]["state"] = "disabled"
            self.diceButtons[row]["bg"] = "light gray"
    def nextTurn(self):
        for i in range(5):
            self.diceButtons[i]["text"] = "?"
        self.roll = 0
        self.rollDice["state"] = "normal"
        self.rollDice["bg"] = "white"
        self.undo()
        self.player = (self.player + 1) % self.numPlayers
        self.bottomLabel.configure(text=self.players[self.player].toString() + "차례: Roll Dice 버튼을 누르세요.")
        for i in range(self.TOTAL + 1):
            for j in range(self.numPlayers):
                if j != self.player or i == self.UPPERTOTAL or i == self.UPPERBONUS \
                        or i == self.LOWERTOTAL or i == self.TOTAL:
                    self.fields[i][j]["state"] = "disabled"
                    self.fields[i][j]["bg"] = "light gray"
                else:
                    self.fields[i][j]["state"] = "normal"
                    self.fields[i][j]["bg"] = "white"
        for i in range(6):
            if self.players[self.player].getUsed(i) == True:
                self.fields[i][self.player]["state"] = "disabled"
                self.fields[i][self.player]["bg"] = "light gray"
        for i in range(8,15):
            if self.players[self.player].getUsed(i-2) == True:
                self.fields[i][self.player]["state"] = "disabled"
                self.fields[i][self.player]["bg"] = "light gray"
        if self.player == 0:
            self.round += 1
        if self.round == 13:
            tmp = 0
            winner = 0
            for i in range(self.numPlayers):
                if tmp < self.players[i].getTotalScore() + self.players[i].bonus:
                    tmp = self.players[i].getTotalScore() + self.players[i].bonus
                    winner = i
            tkinter.messagebox.showinfo("결과","승자는 "+self.players[winner].toString()+" 입니다.\n\t"+str(tmp)+"점")
    def categoryListener(self, row):#점수계산한것표시하기
        if self.roll >= 1:
            score = Configuration.score(row, self.dice)
            index = row
            if row > 7:
                index = row - 2
            self.players[self.player].setScore(score, index)
            self.players[self.player].setAtUsed(index)
            self.fields[row][self.player].configure(text = str(score))#안눌러도 뜨게 수정
            if self.players[self.player].allUpperUsed():
                self.fields[self.UPPERTOTAL][self.player].configure(\
                    text = str(self.players[self.player].getUpperScore()))
                if self.players[self.player].getUpperScore() > 63:
                    self.fields[self.UPPERBONUS][self.player].configure(text="35")
                    self.players[self.player].bonus = 35
                else:
                    self.fields[self.UPPERBONUS][self.player].configure(text="0")
            if self.players[self.player].allLowerUsed():
                self.fields[self.LOWERTOTAL][self.player].configure(text=str(self.players[self.player].getLowerScore()))
            if self.players[self.player].allUpperUsed() and self.players[self.player].allLowerUsed():
                if self.players[self.player].getUpperScore() > 63:
                    self.fields[self.TOTAL][self.player].configure(text=\
                     str(self.players[self.player].getUpperScore() + self.players[self.player].getLowerScore() + 35))
                else:
                    self.fields[self.TOTAL][self.player].configure(text=\
                    str(self.players[self.player].getUpperScore() + self.players[self.player].getLowerScore()))
            self.nextTurn()
    def initInterface(self):
        self.window = Tk()
        self.window.title("Yahtzee Game")
        self.window.geometry("1800x800")
        self.TempFont = font.Font(size=16, weight="bold", family="Consolas")#?
        for i in range(5):#1
            self.dice.append(Dice())
        self.rollDice = Button(self.window, text="Roll Dice", font=self.TempFont,\
                               command=self.rollDiceListener)
        self.rollDice.grid(row=0, column=0)
        for i in range(5):#2
            self.diceButtons.append(Button(self.window, text="?",\
                                           font=self.TempFont, width=8, command=lambda row=i:self.diceListener(row)))
            self.diceButtons[i].grid(row=i+1, column=0)
        self.undoButton = Button(self.window, text="undo", font=self.TempFont, command=self.undo)
        self.undoButton.grid(row=6, column=0)
        for i in range(self.TOTAL+2):
            Label(self.window, text=Configuration.configs[i], font=self.TempFont).grid(row=i, column=1)
            for j in range(self.numPlayers):
                if i == 0:
                    Label(self.window, text=self.players[j].toString(), font=self.TempFont).grid(row=0, column=2+j)
                else:
                    if j == 0:
                        self.fields.append([])
                    self.fields[i-1].append(Button(self.window, text="?", font=self.TempFont, width=8,\
                                                   command=lambda row=i-1: self.categoryListener(row)))#3
                    self.fields[i-1][j].grid(row=i, column=2+j)
                    if j != self.player or (i-1) == self.UPPERTOTAL or (i-1) == self.UPPERBONUS \
                        or (i-1) == self.LOWERTOTAL or (i-1) == self.TOTAL:
                        self.fields[i-1][j]["state"] = "disabled"
                        self.fields[i-1][j]["bg"] = "light gray"
        self.bottomLabel = Label(self.window, text=self.players[self.player].toString()+"차례: Roll Dice 버튼을 누르세요.", \
                                 width=35, font=self.TempFont)
        self.bottomLabel.grid(row=self.TOTAL + 2, column=0)
        self.window.mainloop()
    def __init__(self):
        self.initPlayers()
Y = YahtzeeBoard()