# Click as fast as you can in a designated amount of time chosen by user. See how much cash the user gains in the certain time limit.

# Importing Turtle and Random Module for this project.
#--- Imports ---#
import turtle as trtl
import random as rand

#--- Setup ---#
wn = trtl.Screen()

#--- Creating objects ---# 
clickTurtle = trtl.Turtle() # This turtle will be the turtle the player needs to click to get cash.
cashTurtle = trtl.Turtle() # This turtle shows how much cash total cash the player has.
upgradeMultiplierTurtle = trtl.Turtle()
showMultiplierStats = trtl.Turtle()

timerTurtle = trtl.Turtle()


#--- Config ---#
clickTurtle.shapesize(5)
clickTurtle.penup()

#-- 
cashTurtle.penup() # Shows cash
cashTurtle.hideturtle()
cashTurtle.goto(-80, 300)

#--
upgradeMultiplierTurtle.penup() # Upgrade Multiplier label (shows price)
upgradeMultiplierTurtle.goto(300, -200)
upgradeMultiplierTurtle.shapesize(1)
upgradeMultiplierTurtle.write("Click here to upgrade multiplier to earn cash faster!", font=("Ariel", 10, "bold"))

#-- 
showMultiplierStats.penup()
showMultiplierStats.hideturtle()
showMultiplierStats.goto(-60, 270)

#--
timerTurtle.penup() # TImer Turtle
timerTurtle.goto(0, 200)
timerTurtle.hideturtle()

#--
turtleColors = ["Purple", "Blue", "Red", "Green", "Yellow", "Black", "Brown", "Cyan"] # The colors the clickTurtle will appear in. (randomly)
turtleShapes = ["circle", "square", "turtle", "triangle"]

#--- Variables ---#
cash = 0
multiplier = 1 # player can upgrade variable so player can earn more cash per click.

timer = 0 # Timer that user will pick.
timerInterval = 1000 # 1000 milliseconds in 1 second

multiplierUpgradePrice = 10 # The price that the multiplier upgrade will cost. This will increment to a higher price when player buys upgrade.

#--- Inputs ---#
timeLimit = int(input("How much time would you like? (Hint: Higher number = Higher score!): "))
timer = timeLimit

CanClick = True # Controls click

#--- Functions ---#
def click(x, y):
    if CanClick:
        global timer
        gainCash()
        randomSpawn(True)
    else:
        print("Time is up! Restart to play again!")

def randomSpawn(CanSpawn): 
    if CanSpawn:
        randColor = rand.randint(0, 7) # 0 to 7 because the turtle colors list index starts from 0.
        randShape = rand.randint(0, 3) # 4 shapes total and list starts from 0.

        randX = rand.randint(-200, 200) 
        randY = rand.randint(-20, 20)

        clickTurtle.hideturtle()
        clickTurtle.goto(randX, randY)
        clickTurtle.color(turtleColors[randColor])
        clickTurtle.shape(turtleShapes[randShape])
        clickTurtle.shapesize(5)
        clickTurtle.showturtle()
    else:
        print("Thank you for playing!")


def countdown(): # Timer system where if player does not click the turtle fast enough, it will move to another random position.
    global timer
    global CanClick
    timerTurtle.clear()
    if timer <= 0:
        timerTurtle.write("TIME IS UP!", font=("Ariel", 20, "bold"), align="center")
        timerTurtle.getscreen().ontimer(countdown, timerInterval)
        randomSpawn(False)
        CanClick = False
    else:
        timerTurtle.write("Timer: " + str(timer), font=("Ariel", 20, "bold"), align="center")
        timer -= 1
        timerTurtle.getscreen().ontimer(countdown, timerInterval)

def gainCash():
    global cash
    global multiplier
    cash += multiplier
    writeCash(cash) # Writing the cash after player gets it.
    writeMultiplier(multiplier)

def writeCash(cash):
    cashTurtle.clear()
    cashTurtle.write(arg=("Total cash: "+str(cash)),font=("Ariel", 20, "normal"))

def updateMultiplier(x, y):
    global multiplier
    global multiplierUpgradePrice
    global cash

    if cash >= multiplierUpgradePrice:
        cash -= multiplierUpgradePrice
        multiplier *= 2
        multiplierUpgradePrice *= 3
        writeCash(cash)

    writeMultiplier(multiplier)
    upgradeMultiplierTurtle.clear()
    upgradeMultiplierTurtle.write("Total multiplier: " + str(multiplier)+ "x. You need: "+ str(multiplierUpgradePrice)+" dollars To upgrade!", font=("Ariel", 10, "bold"))

def writeMultiplier(multiplier):
    showMultiplierStats.clear()
    showMultiplierStats.write(arg=("Total multiplier: "+str(multiplier)+"x"), font=("Ariel", 10, "bold"))


#--- Events ---#
clickTurtle.onclick(click)
upgradeMultiplierTurtle.onclick(updateMultiplier) # Upgrading

wn.ontimer(countdown, timerInterval) # Timer

wn.listen() # listens for the event
wn.update() # Updating 

wn.mainloop()