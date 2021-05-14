from tkinter import *
from PIL import Image, ImageTk
from time import sleep
import RPi.GPIO as GPIO
from random import randint


#this debug value can be set true to enable debugging output
#mainly a syntax thing for right now
DEBUG = False

class Enemy():
    def __init__(self,name,HP,atkVal):
        self.name = name
        self.HP = HP
        self.atkVal = atkVal

class Item():
    def __init__(self, name, atk):
        self.name = name
        self.atk = atk

    def __str__(self):
        return "{}".format(self.name)

        
#this is for the rooms of the game
class Area():
    def __init__(self, name, image, image2):
        self.name = name
        self.image = image
        self.image2 = image2

        self.neighbors = {}
        self.items = []
        self.enemies = []

    def __str__(self):
        return self.name
    
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
        parent.attributes("-fullscreen", True)
        self.setupGUI()
        Game.inventory = {}
        Game.invOpen = False
        Game.atkVal = 5
        Game.HP = 100
        Game.strengths = 0
        
    def setHP(self, val):
        if(Game.HP + val > 100):
            Game.HP = 100
        else:
            Game.HP += val
    def lose():
        exit

    def __str__(self):
        return self.name

    def createArea(self):
        a1 = Area("Area 1", "pics/Game1Room1.gif", "pics/CurrentRoom1Pic.gif")
        a2 = Area("Area 2", "pics/Game1Room2.gif", "pics/CurrentRoom2Pic.gif")
        a3 = Area("Area 3", "pics/Game1Room3.gif", "pics/CurrentRoom3Pic.gif")
        a4 = Area("Area 4", "pics/Game1Room4.gif", "pics/CurrentRoom4Pic.gif")
        a5 = Area("Area 5", "pics/Game1Room5.gif", "pics/CurrentRoom5Pic.gif")
        a6 = Area("Area 6", "pics/Game1Room6.gif", "pics/CurrentRoom6Pic.gif")
        a7 = Area("Area 7", "pics/Game1Room7.gif", "pics/CurrentRoom7Pic.gif")
        a8 = Area("Area 8", "pics/Game1Room8.gif", "pics/CurrentRoom8Pic.gif")
        a9 = Area("Area 9", "pics/Game1Room9.gif", "pics/CurrentRoom9Pic.gif")
        a10 = Area("Area 10", "pics/Game1Room10.gif", "pics/CurrentRoom10Pic.gif")
        a11 = Area("Area 11", "pics/Game1Room11.gif", "pics/CurrentRoom11Pic.gif")
        a12 = Area("Area 12", "pics/Game1Room12.gif", "pics/CurrentRoom12Pic.gif")
        a13 = Area("Area 13", "pics/Game1Room13.gif", "pics/CurrentRoom13Pic.gif")
        a14 = Area("Area 14", "pics/Game1Room14.gif", "pics/CurrentRoom14Pic.gif")
        a15 = Area("Area 15", "pics/Game1Room15.gif", "pics/CurrentRoom15Pic.gif")
        a16 = Area("Area 16", "pics/Game1Room16.gif", "pics/CurrentRoom16Pic.gif")
        a17 = Area("Area 17", "pics/Game1Room17.gif", "pics/CurrentRoom17Pic.gif")
        a18 = Area("Area 18", "pics/Game1Room18.gif", "pics/CurrentRoom18Pic.gif")
        a19 = Area("Area 19", "pics/Game1Room19.gif", "pics/CurrentRoom19Pic.gif")
        a20 = Area("Area 20", "pics/Game1Room20.gif", "pics/CurrentRoom20Pic.gif")
        
        #a1 neighbors
        a1.addNeighbor("east", a2)
        #a1 items
        a1.addItem(Item("woodenDagger", 5))
        #a1 enemies
        a1.addEnemy(Enemy("Jared", 3, 3))
        
        #a2 neighbors
        a2.addNeighbor("east", a3)
        a2.addNeighbor("north", a11)
        a2.addNeighbor("west", a1)
        #a2 items
        a2.addItem(Item("strengthPotion", 5))
        #a2 enemies
        
        #a3 neighbors
        a3.addNeighbor("west", a2)
        a3.addNeighbor("east", a4)
        #a3 items
        a3.addItem(Item("steelDagger", 7))
        #a3 enemies
        a3.addEnemy(Enemy("goblin", 20, 4))
        
        #a4 neighbors
        a4.addNeighbor("west", a3)
        a4.addNeighbor("north", a5)
        #a4 items
        a4.addItem(Item("strengthPotion", 5))
        #a4 enemies
        
        #a5 neighbors
        a5.addNeighbor("west", a6)
        a5.addNeighbor("east", a8)
        a5.addNeighbor("south", a4)
        #a5 items
        a5.addItem(Item("enhancedDagger", 9))
        #a5 enemies
        a5.addEnemy(Enemy("troll", 30, 7))
        
        #a6 neighbors
        a6.addNeighbor("east", a5)
        a6.addNeighbor("south", a7)
        #a6 items
        a6.addItem(Item("shortSword", 12))
        #a6 enemies
        
        #a7 neighbors
        a7.addNeighbor("north", a6)
        #a7 items
        a7.addItem(Item("strengthPotion", 5))
        #a7 enemies
        
        #a8 neighbors
        a8.addNeighbor("west", a5)
        a8.addNeighbor("south", a9)
        #a8 items
        a8.addItem(Item("strengthPotion", 5))
        #a8 enemies
        a8.addEnemy(Enemy("giantTroll", 40, 10))
        
        #a9 neighbors
        a9.addNeighbor("north", a8)
        a9.addNeighbor("south", a10)
        #a9 items
        a9.addItem(Item("enhancedShortSword", 15))
        #a9 enemies
        
        #a10 neighbors
        a10.addNeighbor("north", a9)
        #a10 items
        a10.addItem(Item("strengthPotion", 10))
        #a10 enemies
        
        #a11 neighbors
        a11.addNeighbor("south", a2)
        a11.addNeighbor("east", a12)
        a11.addNeighbor("north", a18)
        #a11 items
        a11.addItem(Item("strengthPotion", 10))
        #a11 enemies
        a11.addEnemy(Enemy("griffin", 50, 20))
        
        #a12 neighbors
        a12.addNeighbor("west", a11)
        a12.addNeighbor("east", a13)
        #a12 items
        a12.addItem(Item("strengthPotion", 10))
        #a12 enemies
        
        #a13 neighbors
        a13.addNeighbor("west", a12)
        a13.addNeighbor("north", a14)
        #a13 items
        a13.addItem(Item("strengthPotion", 10))
        #a13 enemies
        
        #a14 neighbors
        a14.addNeighbor("south", a13)
        a14.addNeighbor("east", a15)
        #a14 items
        a14.addItem(Item("longSword", 17))
        #a14 enemies
        a14.addEnemy(Enemy("minotaur", 60, 30))
        
        #a15 neighbors
        a15.addNeighbor("west", a14)
        a15.addNeighbor("south", a16)
        #a15 items
        a15.addItem(Item("strengthPotion", 10))
        #a15 enemies
        
        #a16 neighbors
        a16.addNeighbor("north", a15)
        a16.addNeighbor("east", a17)
        #a16 items
        a16.addItem(Item("strengthPotion", 10))
        #a16 enemies
        
        #a17 neighbors
        a17.addNeighbor("west", a16)
        #a17 items
        a17.addItem(Item("enhancedLongSword", 22))
        #a17 enemies
        a17.addEnemy(Enemy("hydra", 70, 40))
        
        #a18 neighbors
        a18.addNeighbor("south", a11)
        a18.addNeighbor("east", a19)
        #a18 items
        a18.addItem(Item("strengthPotion", 15))
        #a18 enemies
        a18.addEnemy(Enemy("dragon", 100, 60))
        
        #a19 neighbors
        a19.addNeighbor("west", a18)
        a19.addNeighbor("east", a20)
        #a19 items
        a19.addItem(Item("lightningBow", 60))
        #a19 enemies
        a19.addEnemy(Enemy("wraith", 200, 30))
        
        #a20 neighbors
        a20.addNeighbor("west", a19)
        #a20 items
        a20.addItem(Item("FountainOfYouth", 300))
        #a20 enemies
        a20.addEnemy(Enemy("Lord Gourd", 1773, 100))
        
        Game.currentArea = a1
    

    def setupGUI(self):
        self.pack(fill = BOTH, expand = 1)
        #rows and columns of Frame window
        for row in range(2):
            Grid.rowconfigure(self, row, weight=1)

        for col in range(2):
            Grid.columnconfigure(self, col, weight=1)
        


        img = None
        Game.image = Label(self, image=img)
        Game.image.grid(row=0, column = 0, pady = 250, sticky="nsew")
        Game.image.pack_propagate(True)

        #input for now

        
        Game.player_input = Entry(self, bg = "lightgrey")
        
        
##        Game.var = "advance east"

        
        
        

        Game.player_input.grid(row=2, column=0, columnspan=2, sticky="nsew")
        Game.player_input.focus()


        #text for now
        text_frame = Frame(self, width = int(WIDTH/2))
        Game.text = Text(text_frame, bg = "lightgrey", state = DISABLED)
        Game.text.pack(fill=X,expand=1)
        text_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
        text_frame.pack_propagate(True)

        self.pack(fill = BOTH, expand = 1)

    def setAreaImage(self):
        Game.img = Image.open(Game.currentArea.image)
        resized = Game.img.resize((400,300), Image.ANTIALIAS)

        Game.image = ImageTk.PhotoImage(resized)

        Game.display = Label(self, image = Game.image)
        Game.display.grid(row=0, column=0, sticky="nsw")

        Game.img2 = Image.open(Game.currentArea.image2)
        resized2 = Game.img2.resize((400,300), Image.ANTIALIAS)

        Game.image2 = ImageTk.PhotoImage(resized2)

        Game.display2 = Label(self, image = Game.image2)
        Game.display2.grid(row=0, column=1, sticky="nsw")

    def setCurrentAreaImage(self):
        Game.img = PhotoImage(file = Game.currentArea.image)
        Game.image.config(image = Game.img)
        Game.image.image = Game.img
        Game.image.grid(row=0, column=1, sticky=N+S+E+W)

    def setStatus(self, status):
        Game.text.config(state = NORMAL)
        Game.text.delete("1.0", END)

        if(Game.currentArea == None):
            Game.text.insert(END, "You are dead. You may quit \n")
        else:
            Game.text.insert(END, str(Game.currentArea)+\
                            "\n\n" + status +\
                            "\nYour HP is at {}".format(Game.HP) +\
                            "\nYour Attack value is {}".format(Game.atkVal + Game.strengths) +\
                            "\nThere is {} enemy(s)".format(len(Game.currentArea.enemies)) +\
                            "\nThere {} item(s)".format((len(Game.currentArea.items))))
            Game.text.config(state = DISABLED)

    def regen(self):
        self.setHP( 10)

    def play(self):
        self.createArea()
        self.setupGUI()
        self.setAreaImage()

    def process(self, event, res):

        
        action = res
        
        

        if(Game.currentArea == None):
            Game.player_input.delete(0, END)
            return
        words = action.split()
        verb = words[0]
        if(len(words) > 1):
            noun = words[1]

        if(verb == "advance"):
            response = "cannot advance there (perhaps there is no area to go to)."

            if(noun in Game.currentArea.neighbors):
                Game.regen(self)
                Game.currentArea = Game.currentArea.neighbors[noun]
                response = "You move to the area to the {}".format(noun)

        elif(verb == "loot"):
            response = "cannot loot an item, for there is none"
            if(len(Game.currentArea.items) > 0):
                Game.regen(self)
                if(Game.currentArea.items[0].name == "strengthPotion"):
                    Game.strengths += Game.currentArea.items[0].atk
                    response = "You drank the strength pot"
                    Game.currentArea.delItem(Game.currentArea.items[0])
                else:
                
                    Game.inventory[len(Game.inventory)] = Game.currentArea.items[0]

                    response = "Item {} was taken.".format(Game.currentArea.items[0])
                    if(Game.currentArea.items[0].atk > Game.atkVal):
                        Game.atkVal = Game.currentArea.items[0].atk
                        response += "\nIt was equipped"
                    GPIO.output(leds[2], True)
                    sleep(0.5)
                    GPIO.output(leds[2], False)
                    Game.currentArea.delItem(Game.currentArea.items[0])

        elif(verb == "inv"):
            Game.invOpen = not Game.invOpen
            response = "inventory open = {}".format(Game.invOpen)
            Game.player_input.delete(0, END)
            Game.display.grid_forget()
            inv = {}
            for key in Game.inventory:
                inv[key] = Game.inventory[key].name 
                
                
            while(Game.invOpen):
                GPIO.output(leds[0], True)
                Game.image = Label(self, text = inv, font = "25")
                Game.image.grid(row=0, column=0, columnspan = 2, sticky="nsew")
                Game.image.pack_propagate(False)
                
                self.process()
            GPIO.output(leds[0], False)
                
            Game.image.grid_forget()

        elif(verb == "attack"):
            
            Game.currentArea.Enemy = Game.currentArea.enemies[0]
            Game.player_input.delete(0, END)
##            response = ""
            while(Game.HP>0 and Game.currentArea.Enemy.HP>0):
                GPIO.output(leds[1], True)
                Game.HP -= Game.currentArea.Enemy.atkVal
                Game.currentArea.Enemy.HP -= (Game.atkVal + Game.strengths)
                print("Current HP: {}".format(Game.HP))
                print("{}'s current HP: {}".format(Game.currentArea.Enemy.name,Game.currentArea.Enemy.HP))
                print("")
                if(Game.HP <= 0):
                    response = "You have died"
                    self.setStatus(response)
                    sleep(2)
                    GPIO.cleanup()
                    sys.exit(0)
                    
                    break
                    
                else:
                    response = ("Current HP: {}".format(Game.HP))
                    response += ("\n{}'s current HP: {}".format(Game.currentArea.Enemy.name,Game.currentArea.Enemy.HP))
                    response += ("\n")
                    

                self.setStatus(response)
                
                
                sleep(1)
            
            Game.currentArea.delEnemy(Game.currentArea.enemies[0])
            Game.strengths += 2
            response += "Your remaining health is {}".format(Game.HP)
            GPIO.output(leds[1], False)

        else:
            response = "Pick something else"
            


        self.setStatus(response)
        self.setAreaImage()

            


HEIGHT = 600
WIDTH = 800
window = Tk()
window.title("Avalache's Fighters of the forum")
g = Game(window)
g.play()



#button and led setup
buttons = [18,19,20,21,17,16,13]#determine slots
leds = [12,6,5]#determine slots
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttons, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, False)



def onButtonPress(butt):

    
    if(butt == 19):
        res = "advance east"
    elif(butt == 18):
        res = "advance north"
    elif(butt == 20):
        res = "advance south"
    elif(butt == 21):
        res = "advance west"
    elif(butt == 17):
        res = "inv"
    elif(butt == 16):
        res = "attack"
    elif(butt == 13):
        res = "loot"
    
    g.process("<<GpioButtonPress>>", res)


GPIO.add_event_detect(19, GPIO.BOTH, lambda e: onButtonPress(19), bouncetime = 300)
GPIO.add_event_detect(18, GPIO.BOTH, lambda e: onButtonPress(18), bouncetime = 300)
GPIO.add_event_detect(17, GPIO.BOTH, lambda e: onButtonPress(17), bouncetime = 300)
GPIO.add_event_detect(16, GPIO.BOTH, lambda e: onButtonPress(16), bouncetime = 300)
GPIO.add_event_detect(13, GPIO.BOTH, lambda e: onButtonPress(13), bouncetime = 300)
GPIO.add_event_detect(20, GPIO.BOTH, lambda e: onButtonPress(20), bouncetime = 300)
GPIO.add_event_detect(21, GPIO.BOTH, lambda e: onButtonPress(21), bouncetime = 300)


window.mainloop()


