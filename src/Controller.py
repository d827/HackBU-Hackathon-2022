import sys
import pygame as pg
from pygame import *
import math
import random
from pygame import mixer
from moviepy.editor import VideoFileClip
from src import Sprite
from src import VideoSprite

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
            "Bedroom": "assets/scenes/Bedroom.png",
            "Street": "assets/scenes/Street.png",
            "Campus": "assets/scenes/Campus.png",
            "Classroom": "assets/scenes/Classroom.png",
            "Redjug": "assets/scenes/Redjug.png",
            "Preserve": "assets/scenes/Preserve.png"
        }
        self.char_dict = {
            "Harpur": "assets/chars/Harpur.png",
            "SoM": "assets/chars/SoM.png",
            "Watson": "assets/chars/Watson.png",
            "Nursing": "assets/chars/Nursing.png",
            "Don": "assets/chars/donald.png",
            "Baxter": "assets/chars/Baxter.png",
            "Bus": "assets/chars/Bus.png",
            "Garf": "assets/chars/Garf.png"
        }

        # Menu music
        mixer.music.load("assets/sounds/Theme.mp3")


        self.scene = 'SELECTION'
        self.choice = ''
        self.sprite_group = pg.sprite.Group()

        # PLAYER PARAM
        self.playerX = 50
        self.playerX_change = 0
        self.playerY = 150
        self.player = Sprite.Sprite("Player", 150, 850, "assets/chars/donald.png")

        # ENEMY PARAM
        self.enemy = Sprite.Sprite("Baxter", 150, 850, "assets/chars/Baxter.png")
        self.enemyX = 970
        self.enemyX_change = .1

        # OBJECT PARAM
        self.object = Sprite.Sprite("Bus", 150, 850, "assets/chars/Bus.png")
        self.objectX = 1000
        self.objectX_change = -10
        self.objectY = 360

        # Score related
        self.letter = 4
        self.grade_list = ["F","D","C","B","A"]
        self.score_value = self.grade_list[self.letter]
        self.score_font = pg.font.Font('freesansbold.ttf',32)



        self.inputMode = True
        self.next_choice = 'Classroom'
        self.boundary = 600

        # Title and icon
        pg.display.set_caption("The Binghamton Trail")

        pg.font.init()
        self.state = "MENU"


    def stateChange(self):
        clock = pg.time.Clock()
        mixer.music.play(-1)
        while True:

            keys = pg.key.get_pressed()

            if keys[pg.K_RIGHT]:
                if self.scene == 'PRESERVE':
                    self.playerX += 12
                else:
                    self.playerX += 4.5
            if keys[pg.K_LEFT]:
                if self.scene == 'PRESERVE':
                    self.playerX -= 12
                else:
                    self.playerX -= 4.5

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:

                    if event.key == pg.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    elif event.key == pg.K_RETURN and self.user_text == "MENU":
                        self.state = "MENU"
                    elif event.key == pg.K_RETURN:
                        self.choice = self.user_text
                        self.user_text = ''
                    else:
                        self.user_text += event.unicode

            if self.state == "MENU":

                self.mainMenu()
            elif self.state == "INSTRUCTIONS":
                self.instructions()
            elif self.state == "PLAY":
                self.play()
            elif self.state == "GAMEOVER":
                self.gameover()
            elif self.state == "WIN":
                self.win()

            pg.display.update()
            clock.tick(60)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (255,255,255))
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
        if mode == "INPUT":
            y_change = -20
        elif mode == "OPTIONS":
            y_change = -175

        for text in option_text:
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

        self.backg = pg.image.load('assets/scenes/bing.jpg').convert()
        self.screen.blit(self.backg, (0,0))

        title = pg.font.Font("freesansbold.ttf", 70)
        TextSurf, TextRect = self.text_objects("THE BINGHAMTON TRAIL", title)
        TextRect.center = ((self.width/2), (self.height/2))
        self.screen.blit(TextSurf, TextRect)

        self.button("PLAY!",250, 550, 100, 50, (24, 103, 48),(204, 204, 0), "PLAY")
        self.button("RULES",750, 550, 100, 50, (24, 103, 48),(0, 102, 204), "INSTRUCTIONS")


        while self.state == "MENU":

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    #movie.stop()
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    for b in self.buttons:
                        if b[0].collidepoint(event.pos):
                            self.state = b[1]
                            self.buttons = []


            pg.display.update()

    # Title and icon

    def instructions(self):
        self.screen.fill((24, 103, 48))
        self.textBox(500, 350, 850, 400, (0, 0, 0), "OPTIONS", "Rules:~1. Each scene will have options~2. Choose an option by typing in option number~3. Each option affects your letter grade~4. You can move your character with the right~and left arrow keys~after choosing an option")
        self.button("PLAY!",250, 700, 100, 50, (255, 255, 0),(204, 204, 0), "PLAY")
        self.button("MENU",750, 700, 100, 50, (51, 135, 255),(0, 102, 204), "MENU")

        while self.state == "INSTRUCTIONS":
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    for b in self.buttons:
                        if b[0].collidepoint(event.pos):
                            self.state = b[1]
                            self.buttons = []

            pg.display.update()

    def play(self):
        #self.all_sprites.update()
        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 1000:
            self.playerX = 1000

        if self.scene == 'SELECTION':
            self.screen.fill((24, 103, 48))
            self.textBox(500, 350, 750, 400, (0, 0, 0), "OPTIONS", "Who are you? Who you decide will change~your stats.~1. Harpur~2. Watson~3. SoM~4. Decker")
            self.textBox(500, 550, 750, 80, (0, 0, 0), "INPUT", self.user_text)
            if self.choice == '1':
                self.scene = 'SELECTION2'
                self.player.updateImg(self.char_dict["Harpur"])
                self.choice = ''
            elif self.choice == '2':
                self.scene = 'SELECTION2'
                self.player.updateImg(self.char_dict["Watson"])
                self.choice = ''
            elif self.choice == '3':
                self.scene = 'SELECTION2'
                self.player.updateImg(self.char_dict["SoM"])
                self.choice = ''
            elif self.choice == '4':
                self.scene = 'SELECTION2'
                self.player.updateImg(self.char_dict["Nursing"])
                self.choice = ''


        elif self.scene == 'SELECTION2':
            self.textBox(500, 350, 750, 400, (0, 0, 0), "OPTIONS", "What is your name?")
            self.textBox(500, 550, 750, 80, (0, 0, 0), "INPUT", self.user_text)


            if self.choice != '':
                self.player.updateName(self.choice)
                self.scene = 'START'
                self.choice = ''

        elif self.scene == 'START':
            self.backg = pg.image.load(self.scene_dict["Bedroom"]).convert()
            self.screen.blit(self.backg, (0,0))
            if self.inputMode:
                self.textBox(500, 350, 750, 400, (0, 0, 0), "OPTIONS", "Options:~1. Take the bus~2. Booze")
                self.textBox(500, 550, 750, 80, (0, 0, 0), "INPUT", self.user_text)
                if self.choice == '1':
                    self.next_choice = "Street"
                    self.inputMode = False
                    self.choice = ''
                elif self.choice == '2':
                    self.next_choice = "Redjug"
                    self.inputMode = False
                    self.choice = ''
            else:

                self.screen.blit(self.backg, (0,0))
                self.screen.blit(pg.image.load('assets/chars/Garf.png'), (550,525))
                if self.playerX >= 350:

                    self.playerX = 150
                    self.backg = pg.image.load(self.scene_dict[self.next_choice]).convert()
                    self.screen.blit(self.player.image, (self.playerX,540))
                    self.screen.blit(self.backg, (0,0))
                    self.scene = self.next_choice.upper()
                    self.inputMode = True


                else:

                    self.screen.blit(self.player.image, (self.playerX,540))
                    pg.display.update()

        elif self.scene == 'STREET':
            # self.screen.blit(self.backg, (0,0))
            if self.inputMode:
                self.textBox(500, 350, 750, 400, (0, 0, 0), "OPTIONS", "Options:~1. Go on the bus~2. Ride the almighty bearcat")
                self.textBox(500, 550, 750, 80, (0, 0, 0), "INPUT", self.user_text)
                if self.choice == '1':
                    self.next_choice = "Campus"
                    self.inputMode = False
                    self.choice = ''
                    self.boundary = 600
                elif self.choice == '2':
                    self.next_choice = "Campus"
                    self.inputMode = False
                    self.choice = ''
                    self.boundary = 1000
                    self.score_value = 'B'
            else:
                self.screen.blit(self.backg, (0,0))

                self.enemyX += self.enemyX_change
                if self.enemyX >= 1000:
                    self.enemyX = 1000
                    self.enemyX_change = -self.enemyX_change
                    self.enemyX += self.enemyX_change
                elif self.enemyX <= 968:
                    self.enemyX = 968
                    self.enemyX_change = -self.enemyX_change
                    self.enemyX += self.enemyX_change

                self.screen.blit(self.enemy.image, (self.enemyX,540))

                self.objectX += self.objectX_change

                if self.objectX <= 500:
                    self.objectX = 500
                    self.objectX += self.objectX_change



                if self.playerX >= self.boundary:

                    self.playerX = 150
                    self.backg = pg.image.load(self.scene_dict[self.next_choice]).convert()
                    self.screen.blit(self.player.image, (self.playerX,540))
                    self.screen.blit(self.backg, (0,0))
                    self.inputMode = True
                    self.scene = self.next_choice.upper()


                #self.all_sprites.draw(self.screen)
                else:
                    #self.screen.blit(self.backg, (0,0))
                    self.screen.blit(self.player.image, (self.playerX,540))
                    self.screen.blit(self.object.image, (self.objectX,self.objectY))
                    pg.display.update()

        elif self.scene == 'CAMPUS':
            # self.screen.blit(self.backg, (0,0))
            if self.inputMode:
                self.textBox(500, 350, 750, 400, (0, 0, 0), "OPTIONS", "Options:~1. Travel to class~2. Take a walk")
                self.textBox(500, 550, 750, 80, (0, 0, 0), "INPUT", self.user_text)
                if self.choice == '1':
                    self.next_choice = "Classroom"
                    self.inputMode = False
                    self.choice = ''
                    self.boundary = 1000
                elif self.choice == '2':
                    self.next_choice = "Preserve"
                    self.inputMode = False
                    self.choice = ''
                    self.boundary = 1000
                    self.score_value = 'B'
            else:
                self.screen.blit(self.backg, (0,0))

                if self.playerX >= self.boundary:

                    self.playerX = -20
                    self.backg = pg.image.load(self.scene_dict[self.next_choice]).convert()
                    self.screen.blit(self.player.image, (self.playerX,540))
                    self.screen.blit(self.backg, (0,0))
                    self.scene = self.next_choice.upper()
                    self.inputMode = True


                #self.all_sprites.draw(self.screen)
                else:
                    #self.screen.blit(self.backg, (0,0))
                    self.screen.blit(self.player.image, (self.playerX,540))
                    pg.display.update()

        elif self.scene == 'PRESERVE':
            # self.screen.blit(self.backg, (0,0))
            if self.inputMode:
                self.textBox(500, 350, 750, 400, (0, 0, 0), "OPTIONS", "Options:~1. Walk around~2. Go to class")
                self.textBox(500, 550, 750, 80, (0, 0, 0), "INPUT", self.user_text)
                if self.choice == '1':
                    #self.next_choice = "Gameover"
                    self.inputMode = False
                    self.choice = ''
                    self.boundary = 1050
                elif self.choice == '2':
                    #self.next_choice = "Gameover"
                    self.inputMode = False
                    self.choice = ''
                    self.boundary = 1050

            else:
                self.screen.blit(self.backg, (0,0))
                if self.inputMode:
                    self.textBox(500, 350, 750, 400, (0, 0, 0), "OPTIONS", "Options:~1. Walk around the preserve~2. Go to class")
                    self.textBox(500, 550, 750, 80, (0, 0, 0), "INPUT", self.user_text)
                    if self.choice == '1':
                        #self.next_choice = "Gameover"
                        self.inputMode = False
                        self.choice = ''
                        self.boundary = 1050
                    elif self.choice == '2':
                        #self.next_choice = "Gameover"
                        self.inputMode = False
                        self.choice = ''
                        self.boundary = 1050

                # self.enemyX = self.playerX - 50 + .5

                if self.playerX >= 300:
                    self.enemyX += self.enemyX_change
                    self.screen.blit(pg.transform.flip(self.enemy.image,True,False), (self.enemyX,540))
                    self.enemyX_change += 1*self.enemyX_change/6
                else:
                    self.enemyX = -50


                if self.playerX >= self.boundary or self.playerX <= self.enemyX:

                    self.playerX = 150
                    # self.backg = pg.image.load(self.scene_dict[self.next_choice]).convert()
                    self.screen.blit(self.player.image, (self.playerX,540))
                    self.screen.blit(self.backg, (0,0))
                    self.scene = self.next_choice.upper()
                    self.state = 'GAMEOVER'


                #self.all_sprites.draw(self.screen)
                else:
                    #self.screen.blit(self.backg, (0,0))
                    self.screen.blit(self.player.image, (self.playerX,540))
                    pg.display.update()

        elif self.scene == 'CLASSROOM':
            #self.screen.blit(self.backg, (0,0))
            if self.inputMode:
                if self.inputMode:
                    self.textBox(500, 350, 750, 400, (0, 0, 0), "OPTIONS", "Options:~1. Stay in... *snore*... class...~2. Give in to temptation")
                    self.textBox(500, 550, 750, 80, (0, 0, 0), "INPUT", self.user_text)
                    if self.choice == '1':
                        self.next_choice = "Gameover"
                        self.inputMode = False
                        self.choice = ''
                        self.boundary = 300
                    elif self.choice == '2':
                        self.next_choice = "Redjug"
                        self.inputMode = False
                        self.choice = ''
                        self.boundary = 300
            else:
                self.screen.blit(self.backg, (0,0))

                #if self.playerX >= 600:
                if self.playerX >= self.boundary:
                    self.inputMode = True
                    self.playerX = 150

                    self.screen.blit(self.player.image, (self.playerX,540))
                    self.screen.blit(self.backg, (0,0))
                    if self.next_choice == "Gameover":
                        if self.letter >= 2:
                            self.state = "WIN"
                        else:
                            self.state = "GAMEOVER"
                    else:
                        self.backg = pg.image.load(self.scene_dict[self.next_choice]).convert()
                        self.scene = self.next_choice.upper()

                else:
                    self.screen.blit(self.player.image, (self.playerX,540))
                    pg.display.update()

        elif self.scene == 'REDJUG':
            if self.inputMode:
                self.screen.blit(self.backg, (0,0))
                self.textBox(500, 350, 750, 400, (0, 0, 0), "OPTIONS", "Options:~1. Have a drink~2. Try and get to class")
                self.textBox(500, 550, 750, 80, (0, 0, 0), "INPUT", self.user_text)
                if self.choice == '1':
                    self.next_choice = "Redjug"
                    if self.score_value == 'F':
                        self.inputMode = False
                    else:
                        self.letter -= 1
                        if self.letter <= 0:
                            self.letter = 0
                        elif self.letter >= 4:
                            self.letter = 4
                        self.playerX = 50
                        self.inputMode = True
                        self.score_value = self.grade_list[self.letter]
                    self.choice = ''
                    self.boundary = 1050

                    self.score_value = self.grade_list[self.letter]
                elif self.choice == '2':
                    self.letter -= 1
                    if self.letter <= 0:
                        self.letter = 0
                    elif self.letter >= 4:
                        self.letter = 4
                    self.score_value = self.grade_list[self.letter]
                    self.playerX = 50
                    self.next_choice = "Classroom"
                    self.inputMode = False
                    self.choice = ''
                    self.boundary = 1050



            else:
                self.screen.blit(self.backg, (0,0))
                if self.score_value == 'F':
                    pass


                if self.playerX >= 600:
                    self.state = 'GAMEOVER'
                else:

                    self.screen.blit(self.player.image, (self.playerX,540))
                pg.display.update()

        self.show_score(10, 10, self.score_font, self.score_value)


    def show_score(self,x, y, font, value):
        score = font.render("Score: " + value, True, (255,255,255))
        self.screen.blit(score, (x,y))

    def gameover(self):
        self.screen.fill((201, 32, 32))
        pg.time.wait(800)
        self.screen.fill((0, 0, 0))

        self.backg = pg.image.load('assets/chars/baxterEnd.png').convert()
        self.screen.blit(self.backg, (0,0))
        self.roar()

        gameOverText = pg.font.Font("freesansbold.ttf", 70)
        TextSurf, TextRect = self.text_objects("GAME OVER, GO TO CLASS!", gameOverText)
        TextRect.center = ((self.width/2), (self.height/2))
        self.screen.blit(TextSurf, TextRect)

        while self.state == "GAMEOVER":

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    #movie.stop()
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    for b in self.buttons:
                        if b[0].collidepoint(event.pos):
                            self.state = b[1]
                            self.buttons = []

            pg.display.update()

        # self.screen.blit()

    def roar(self):
        roar_Sound = mixer.Sound('assets/sounds/Roar.mp3')
        roar_Sound.play()
        mixer.music.stop()

    def win(self):
        self.backg = pg.image.load('assets/chars/Stenger.jpg').convert()
        self.screen.blit(self.backg, (0,0))

        winText = pg.font.Font("freesansbold.ttf", 80)
        TextSurf, TextRect = self.text_objects("YOU WIN!!!", winText)
        TextRect.center = ((self.width/2), (self.height/2))
        self.screen.blit(TextSurf, TextRect)

        while self.state == "WIN":

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    #movie.stop()
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    for b in self.buttons:
                        if b[0].collidepoint(event.pos):
                            self.state = b[1]
                            self.buttons = []


            #self.clock.tick_busy_loop(25)
            pg.display.update()
