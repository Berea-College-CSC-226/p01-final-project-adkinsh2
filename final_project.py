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
        game.run()

class Game:
    def __init__(self):
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill('#24026D')
        self.clock = pygame.time.Clock()
        self.player = None #TODO set these to respective classes
        self.doomship = None
        self.playerAttack = None
        self.enemyAttack = None
        self.playerHealth = 3
        self.enemyHealth = 10

    def run(self):
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
            if pygame.sprite.spritecollide(self.doomship, [self.playerAttack], False):
                self.enemyHealth -= 1
                if self.enemyHealth > 1:
                    font = pygame.font.SysFont("ComicSans", 36)
                    txt = font.render('Congratulations! But can you do it faster?', True, "#5EE1F3")
                    self.screen.blit(txt, (self.size[0] // 2, self.size[1] - 100))

        pygame.quit()

def main():
    startGame = StartMenu()

    startGame.create_startButton()
    startGame.create_titleLabel()
    startGame.create_difficultySetting()

    startGame.root.mainloop()

if __name__ == "__main__":
    main()