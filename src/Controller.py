import sys
import pygame as pg
from pygame import *
import math
import random
from pygame import mixer

class Controller:

    def __init__(self):
        # Initialize
        pg.init()
        self.width = 1000
        self.height = 800

        # Creating screen
        self.screen = pg.display.set_mode((width,height))

        #background
        self.bg = pg.Surface(self.screen.get_size()).convert()
        self.clock = (pg.time.Clock())


        self.state = "MENU"


    def stateChange(self):
        while True:
            if self.state == "MENU":
                self.mainMenu()


    # Title and icon

    # Player Image and variables
    playerImg = pg.image.load()
    playerX = 200
    playerY = 200 # Adjust for accuracy
    playerX_change = 0


    def player(x,y):
        screen.blit(playerImg, (x,y))

    def isCollision(boundaryX,boundaryY,playerX,playerY):
        distance = math.sqrt( (math.pow(boundaryX-playerX,2)) + (math.pow(boundaryY-playerY,2)) )
        if distance < 32:
            return True
        return False

    def loop(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        playerX_change = -2.5

                    if event.key == pg.K_RIGHT:
                        playerY_change = 2.5


                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                        playerX_change = 0


        # Player boundaries
            playerX += playerX_change
            if playerX <= 0:
                playerX = 0
            elif playerX >= 1000:
                playerX = 1000

            player(playerX,playerY)
            pg.display.update()
