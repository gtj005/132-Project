from time import *

class Enemy():
    def __init__(self,name,HP,atkVal):
        self.name = name
        self.HP = HP
        self.atkVal = atkVal

class Player():
    def __init__(self,HP,atkVal):
        self.HP=HP
        self.atkVal=atkVal

e1=Enemy("Jared", 40, 3)
p1=Player(50,5)

while(p1.HP>0 and e1.HP>0):
    p1.HP = p1.HP-e1.atkVal
    e1.HP = e1.HP-p1.atkVal
    print("Current HP: {}".format(p1.HP))
    print("{}'s current HP: {}".format(e1.name,e1.HP))
    print("")
    sleep(1)

