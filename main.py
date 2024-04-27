#IMPORTS
from graphics import *

#GRAPHIC SETUP
makeGraphicsWindow(800, 600)
def startWorld(world):
    world.ballX = 50
    world.ballY = 300


#LOGIC
direction = 'right'
def updateWorld(world):
    global direction
    if direction == 'right': world.ballX +=2
    else: world.ballX -=2
    if world.ballX >= 775: direction = 'left'
    elif world.ballX <= 15: direction = 'right'

#GRAPHIC DISPLAY
def drawWorld(world):
    fillCircle(world.ballX, world.ballY, 50, "red")
runGraphics(startWorld, updateWorld, drawWorld)