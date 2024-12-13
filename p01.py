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
import pygame
from p01_npc import NPC
from p01_player import Player
from p01_bullet import Bullet

class StartMenu:
    def __init__(self, windowtitle="Back in the 80s Space Shooter!"):
        self.root = tk.Tk()
        self.root.minsize(width=500,height=450)
        self.root.maxsize(width=500, height=450)
        self.root.title(windowtitle)

        self.difficultySetting = None
        self.difficulties = (("Easy","easy"),("Hard","hard"))
        self.startButton = None
        self.titleLabelText = tk.StringVar()
        self.titleLabel = None
        self.var = tk.StringVar()

    def create_titleLabel(self,labeltext="Back in the 80s\nSpace Shooter!"):
        self.titleLabelText.set(labeltext)
        self.titleLabel = tk.Label(self.root, textvariable=self.titleLabelText)
        self.titleLabel.pack()

    def create_difficultySetting(self):
        for setting in self.difficulties:
            r = tk.Radiobutton(self.root, text=setting[0], value=setting[1], variable = self.var)
            r.pack()

    def create_startButton(self,buttontext="Start Game!"):
        self.startButton = tk.Button(self.root, text=buttontext, command=self.startButton_handler)
        self.startButton.pack()

    def startButton_handler(self):
        currentDifficulty = self.var.get()
        game = Game(currentDifficulty)
        game.run()

class Game:
    def __init__(self,difficulty):
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill('#9CBEBA')
        self.clock = pygame.time.Clock()
        self.player = Player(self.size)
        self.doomShip = NPC(self.size)
        self.playerAttack = Bullet(self.size)
        if difficulty == "easy":
            self.playerHealth = 50
            self.enemyHealth = 50
        elif difficulty == "hard":
            self.playerHealth = 5
            self.enemyHealth = 100

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            if pygame.sprite.spritecollide(self.player, [self.doomShip], False):
                self.playerHealth -= 1
                if self.playerHealth < 1:
                    font = pygame.font.SysFont("ComicSans", 36)
                    txt = font.render('Game over...', True, "red")
                    self.screen.blit(txt, (self.size[0]//2, self.size[1]-100))
            elif pygame.sprite.spritecollide(self.doomShip, [self.playerAttack], False):
                self.enemyHealth -= 1
                if self.enemyHealth < 1:
                    font = pygame.font.SysFont("ComicSans", 36)
                    txt = font.render('You won!', True, "green")
                    self.screen.blit(txt, (self.size[0]//2, self.size[1]-100))
            else:
                self.player.movement(pygame.key.get_pressed())
                self.doomShip.movement()
                self.playerAttack.movement()
                self.screen.fill('#9CBEBA')
                self.screen.blit(self.player.surf, self.player.rect)
                self.screen.blit(self.doomShip.surf, self.doomShip.rect)
                self.screen.blit(self.playerAttack.surf, self.playerAttack.rect)
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