from tkinter import *

#create class for an enemy
class Enemy():
    def __init__(self,name,HP,atkVal):
        self.name = name
        self.HP = HP
        self.atkVal = atkVal

class Item():
    def __init__(self, name, atk):
        self.name = name
        self.atk = atk

        
#this is for the rooms of the game
class Area():
    def __init__(self, name, image):
        self.name = name
        self.image = image

        self.neighbors = {}
        self.items = []
        self.enemies = []
    
    def addNeighbor(self, neighbor, area):        #adds nearby rooms
        #neighbors are keys, areas are values
        self.neighbors[neighbor] = area

    def addItem(self, item):                      #adds items to the rooms
        self.items.append(item)

    def addEnemy(self, enemy):
        self.enemies.append(enemy)
    

class Game(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

    def createArea(self):
        a1 = Area("Area 1", "pics/test.gif")

        a1.addItem(Item("sword", 23))
##        a1.addEnemy(Enemy("Jared", 3))
            

































window = Tk()
window.title("Avalanche's Fighters of the Forum")

g = Game(window)

window.mainloop()
