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
        #create areas 1-20
        a1 = Area("test", "pics/test.gif")
        a2 = Area("Area 2", "")
        a3 = Area("Area 3", "")
        a4 = Area("Area 4", "")
        a5 = Area("Area 5", "")
        a6 = Area("Area 6", "")
        a7 = Area("Area 7", "")
        a8 = Area("Area 8", "")
        a9 = Area("Area 9", "")
        a10 = Area("Area 10", "")
        a11 = Area("Area 11", "")
        a12 = Area("Area 12", "")
        a13 = Area("Area 13", "")
        a14 = Area("Area 14", "")
        a15 = Area("Area 15", "")
        a16 = Area("Area 16", "")
        a17 = Area("Area 17", "")
        a18 = Area("Area 18", "")
        a19 = Area("Area 19", "")
        a20 = Area("Area 20", "")
        
        #a1 neighbors
        a1.addNeighbor("east", a2)
        #a1 items
        a1.addItem(Item("sword", 23))
        #a1 enemies
        a1.addEnemy(Enemy("Jared", 3, 3))
        
        #a2 neighbors
        a2.addNeighbor("east", a3)
        a2.addNeighbor("north", a11)
        #a2 items
        #a2 enemies
        
        #a3 neighbors
        a3.addNeighbor("west", a2)
        a3.addNeighbor("east", a4)
        #a3 items
        #a3 enemies
        
        #a4 neighbors
        a4.addNeighbor("west", a3)
        a4.addNeighbor("north", a5)
        #a4 items
        #a4 enemies
        
        #a5 neighbors
        a5.addNeighbor("west", a6)
        a5.addNeighbor("east", a8)
        #a5 items
        #a5 enemies
        
        #a6 neighbors
        a6.addNeighbor("east", a5)
        a6.addNeighbor("south", a7)
        #a6 items
        #a6 enemies
        
        #a7 neighbors
        a7.addNeighbor("north", a6)
        #a7 items
        #a7 enemies
        
        #a8 neighbors
        a8.addNeighbor("west", a5)
        a8.addNeighbor("south", a9)
        #a8 items
        #a8 enemies
        
        #a9 neighbors
        a9.addNeighbor("north", a8)
        a9.addNeighbor("south", a10)
        #a9 items
        #a9 enemies
        
        #a10 neighbors
        a10.addNeighbor("north", a9)
        #a10 items
        #a10 enemies
        
        #a11 neighbors
        a11.addNeighbor("south", a2)
        a11.addNeighbor("east", a12)
        a11.addNeighbor("north", a18)
        #a11 items
        #a11 enemies
        
        #a12 neighbors
        a12.addNeighbor("west", a11)
        a12.addNeighbor("east", a13)
        #a12 items
        #a12 enemies
        
        #a13 neighbors
        a13.addNeighbor("west", a12)
        a13.addNeighbor("north", a14)
        #a13 items
        #a13 enemies
        
        #a14 neighbors
        a14.addNeighbor("south", a13)
        a14.addNeighbor("east", a15)
        #a14 items
        #a14 enemies
        
        #a15 neighbors
        a15.addNeighbor("west", a14)
        a15.addNeighbor("south", a16)
        #a15 items
        #a15 enemies
        
        #a16 neighbors
        a16.addNeighbor("north", a15)
        a16.addNeighbor("east", a17)
        #a16 items
        #a16 enemies
        
        #a17 neighbors
        a17.addNeighbor("west", a16)
        #a17 items
        #a17 enemies
        
        #a18 neighbors
        a18.addNeighbor("south", a11)
        a18.addNeighbor("east", a19)
        #a18 items
        #a18 enemies
        
        #a19 neighbors
        a19.addNeighbor("west", a18)
        a19.addNeighbor("east", a20)
        #a19 items
        #a19 enemies
        
        #a20 neighbors
        a20.addNeighbor("west", a19)
        #a20 items
        #a20 enemies
       
   
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
