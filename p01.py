######################################################################
# Author: Harry Adkins
# Username: adkinsh2
#
# Final Project
#
# Purpose: To test my knowledge and apply it
#
#######################################################################
# Acknowledgements:
#
# Based on previous teamworks and assignments
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import tkinter as tk
import pygame, random
from p01_npc import NPC
from p01_player import Player

class StartMenu:
    def __init__(self, windowtitle="Back in the 80s Space Shooter!"):
        self.root = tk.Tk()
        self.root.minsize(width=500,height=450)
        self.root.maxsize(width=500, height=450)
        self.root.title(windowtitle)

        self.difficultySetting = None
        self.difficulties = {"Easy" : "0",
                             "Normal" : "1",
                             "Hard" : "2"}
        self.currentDifficulty = None
        self.startButton = None
        self.titleLabelText = tk.StringVar()
        self.titleLabel = None

    def create_titleLabel(self,labeltext="Back in the 80s\nSpace Shooter!"):
        self.titleLabelText.set(labeltext)
        self.titleLabel = tk.Label(self.root, textvariable=self.titleLabelText)
        self.titleLabel.grid(row=0, column=0)

    def create_difficultySetting(self):
        for setting in self.difficulties:
            r = tk.Radiobutton(self.root, text=setting[0], value=setting[1], variable = self.currentDifficulty)
            r.pack()

    def create_startButton(self,buttontext="Start Game!"):
        self.startButton = tk.Button(self.root, text=buttontext, command=self.startButton_handler)
        self.startButton.grid(row=1, column=1)

    def startButton_handler(self):
        game = Game()
        game.run(self.currentDifficulty)

class Game:
    def __init__(self):
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill('#24026D')
        self.clock = pygame.time.Clock()
        self.player = Player(self.size) #TODO set these to respective classes
        self.doomShip = NPC(self.size)
        self.playerAttack = None
        self.enemyAttack = None
        self.playerHealth = 0
        self.enemyHealth = 0

    def run(self,difficulty):
        if difficulty == 0:
            self.playerHealth = 5
            self.enemyHealth = 5
        elif difficulty == 1:
            self.playerHealth = 3
            self.enemyHealth = 8
        elif difficulty >= 2:
            self.playerHealth = 1
            self.enemyHealth = 10

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            if pygame.sprite.spritecollide(self.player, [self.enemyAttack], False):
                self.playerHealth -= 1
                if self.playerHealth > 1:
                    font = pygame.font.SysFont("ComicSans", 36)
                    txt = font.render('Game over...', True, "#E83E57")
                    self.screen.blit(txt, (self.size[0]//2, self.size[1]-100))
            if pygame.sprite.spritecollide(self.doomShip, [self.playerAttack], False):
                self.enemyHealth -= 1
                if self.enemyHealth > 1:
                    font = pygame.font.SysFont("ComicSans", 36)
                    txt = font.render('Congratulations! But can you do it faster?', True, "#5EE1F3")
                    self.screen.blit(txt, (self.size[0] // 2, self.size[1] - 100))
            else:
                self.tuna.movement(pygame.key.get_pressed())
                self.tacocat.movement()
                self.whiskers.movement()
                self.screen.fill('#9CBEBA')
                self.screen.blit(self.tuna.surf, self.tuna.rect)
                self.screen.blit(self.tacocat.surf, self.tacocat.rect)
                self.screen.blit(self.whiskers.surf, self.whiskers.rect)
            pygame.display.update()
            self.clock.tick(24)

        pygame.quit()

def main():
    startGame = StartMenu()

    startGame.create_startButton()
    startGame.create_titleLabel()
    startGame.create_difficultySetting()

    startGame.root.mainloop()

if __name__ == "__main__":
    main()