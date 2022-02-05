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
        self.screen = pg.display.set_mode((self.width,self.height))

        #background
        self.bg = pg.Surface(self.screen.get_size()).convert()
        self.clock = (pg.time.Clock())
        self.buttons = []


        pg.font.init()
        self.state = "MENU"


    def stateChange(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            if self.state == "MENU":
                self.mainMenu()
            elif self.state == "INSTRUCTIONS":
                self.instructions()
            elif self.state == "QUIT":
                self.quit()
            pg.display.update()


    def quit(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.display.quit()
                sys.exit()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (0,0,0))
        return textSurface, textSurface.get_rect()

    def mainMenu(self):

        self.screen.fill((24, 103, 48))
        title = pg.font.Font("freesansbold.ttf", 80)
        TextSurf, TextRect = self.text_objects("BINGHAMTON TRAIL", title)
        TextRect.center = ((self.width/2), (self.height/2))
        self.screen.blit(TextSurf, TextRect)
        #pg.display.update()

        # while.self.state == "MENU":
        #     for event in pg.event.get():
        #         if event.type == pg.MOUSEBUTTONDOWN:
        #
    # Title and icon

    def instructions():
        pass

    # Player Image and variables
    #playerImg = pg.image.load()
    #playerX = 200
    #playerY = 200 # Adjust for accuracy
    #playerX_change = 0


    def player(x,y):
        screen.blit(playerImg, (x,y))

    def isCollision(boundaryX,boundaryY,playerX,playerY):
        distance = math.sqrt( (math.pow(boundaryX-playerX,2)) + (math.pow(boundaryY-playerY,2)) )
        if distance < 32:
            return True
        return False

    def loop(self):
        running = True
        while self.state == "GAME":
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        print("Left button pressed")
                        #playerX_change = -2.5

                    if event.key == pg.K_RIGHT:
                        print("Right button pressed")
                        #playerY_change = 2.5


                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                        print("Button released")
                        #playerX_change = 0


        # Player boundaries
            # playerX += playerX_change
            # if playerX <= 0:
            #     playerX = 0
            # elif playerX >= 1000:
            #     playerX = 1000
            #
            # player(playerX,playerY)
            pg.display.update()
