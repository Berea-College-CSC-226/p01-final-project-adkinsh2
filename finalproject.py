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


def main():
    startGame = StartMenu()

    startGame.create_startButton()
    startGame.create_titleLabel()
    startGame.create_difficultySetting()

    startGame.root.mainloop()

if __name__ == "__main__":
    main()