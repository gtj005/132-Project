from tkinter import *

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

    def delItem(self, item):
        self.items.remove(item)

    def addEnemy(self, enemy):
        self.enemies.append(enemy)

    def delEnemy(self, enemy):
        self.enemies.remove(enemy)
    

class Game(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

    def createArea(self):
        a1 = Area("test", "pics/test.gif")

        a1.addItem(Item("sword", 23))
        a1.addEnemy(Enemy("Jared", 3, 3))




        Game.currentArea = a1

    def setupGUI(self):
        self.pack(fill = BOTH, expand = 1)



        img = None
        Game.image = Label(self, width = WIDTH, image = img)
        Game.image.pack(side = LEFT, fill = Y)
        Game.image.pack_propagate(False)

    def setAreaImage(self):
        Game.img = PhotoImage(file = Game.currentArea.image)
        Game.image.config(image = Game.img)
        Game.image.image = Game.img



    def play(self):
        self.createArea()
        self.setupGUI()
        self.setAreaImage()
        































HEIGHT = 800
WIDTH = 800

window = Tk()
window.title("Avalache's Fighters of the forum")

g = Game(window)
g.play()

window.mainloop()
