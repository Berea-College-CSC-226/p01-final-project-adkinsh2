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

import pygame
import random

class Bullet(pygame.sprite.Sprite):
    def __init__(self, user, screen_size):
        super().__init__()
        self.screen_size = screen_size
        self.user = user
        if self.user == "player":
            self.surf = pygame.image.load('images/laser.png').convert_alpha()
        if self.user == "enemy":
            self.surf = pygame.image.load('images/fireball.png').convert_alpha()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0]//2, self.screen_size[1]//2)
        self.velocity = 5

    def movement(self):
        if (self.rect.top <= 0) or (self.rect.bottom <= self.screen_size[1]):
            self.velocity = 0 - self.velocity

        self.rect.move_ip(random.randrange(-3, 3), self.velocity)