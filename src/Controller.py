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
        self.user_text = ''
        self.scene_dict = {
            "Bedroom": "assets/scenes/Bedroom.png"
        }
        self.char_dict = {
            "Harpur": "assets/chars/Harpur.png",
            "SoM": "assets/chars/SoM.png",
            "Watson": "assets/chars/Watson.png"
        }
        self.scene = 'SELECTION'
        self.choice = ''

        # Title and icon
        pg.display.set_caption("Binghamton Trail")
        # icon = pg.image.load('')
        # pg.display.set_icon(icon)

        pg.font.init()
        self.state = "MENU"


    def stateChange(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    elif event.key == pg.K_RETURN and self.user_text == "MENU":
                        self.state = "MENU"
                    elif event.key == pg.K_RETURN:
                        self.choice = self.user_text
                    else:
                        self.user_text += event.unicode

            if self.state == "MENU":
                self.mainMenu()
            elif self.state == "INSTRUCTIONS":
                self.instructions()
            elif self.state == "PLAY":
                self.play()
            # elif self.state == "QUIT":
            #     self.quit()
            pg.display.update()



    # def quit(self):
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             pg.display.quit()
    #             sys.exit()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (0,0,0))
        return textSurface, textSurface.get_rect()

    def textBox(self, x, y, w, h, col1, mode, user_text):
        option_text = user_text.split("~")
        input_rect = Surface((w,h))
        input_rect.fill(col1)
        rec = input_rect.get_rect()
        rec.center = (x, y)
        self.screen.blit(input_rect, rec)
        user_font = pg.font.Font("freesansbold.ttf",32)
        #Center
        #TextRect.center = (x, y)
        if mode == "INPUT":
            y_change = -20
        elif mode == "OPTIONS":
            y_change = -175

        for text in option_text:
            #TextRect.x = x-145
            TextSurf, TextRect = self.text_objects(text, user_font)
            TextRect.x = x-365
            TextRect.y = y + y_change #change this value to raise text in box
            self.screen.blit(TextSurf, (TextRect.x+5, TextRect.y+5))
            y_change += 50


    def button(self, msg, x, y, w, h, col, col2, state=None):
        btn = Surface((w,h))
        btn.fill(col)
        rec = btn.get_rect()
        rec.center = (x, y)
        self.buttons.append((rec, state))
        self.screen.blit(btn, rec)
        txt = pg.font.Font("freesansbold.ttf", 20)
        TextSurf, TextRect = self.text_objects(msg, txt)
        TextRect.center = (x, y)
        self.screen.blit(TextSurf, TextRect)


    def mainMenu(self):

        self.screen.fill((24, 103, 48))
        title = pg.font.Font("freesansbold.ttf", 70)
        TextSurf, TextRect = self.text_objects("THE BINGHAMTON TRAIL", title)
        TextRect.center = ((self.width/2), (self.height/2))
        self.screen.blit(TextSurf, TextRect)
        #pg.display.update()
        self.button("PLAY!",250, 550, 100, 50, (255, 255, 0),(204, 204, 0), "PLAY")
        self.button("RULES",750, 550, 100, 50, (51, 135, 255),(0, 102, 204), "INSTRUCTIONS")

        # while.self.state == "MENU":
        #     for event in pg.event.get():
        #         if event.type == pg.MOUSEBUTTONDOWN:
        #

        while self.state == "MENU":
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    for b in self.buttons:
                        if b[0].collidepoint(event.pos):
                            self.state = b[1]
                            self.buttons = []

            pg.display.update()
    # Title and icon

    def instructions(self):
        pass

    def play(self):

        if self.scene == 'SELECTION':
            self.screen.fill((100, 0, 0))
            self.textBox(500, 350, 750, 400, (79, 98, 184), "OPTIONS", "1. Kill Joe~2. Kill Joe~3. Fucking Kill Joe")
            self.textBox(500, 550, 750, 80, (0, 50, 50), "INPUT", self.user_text)
            # if choice == '1':
            #     self.state = "MENU"

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

    def controls(self):
        pass
