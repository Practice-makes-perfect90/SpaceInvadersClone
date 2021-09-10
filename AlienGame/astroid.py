import pygame
import os
from pygame.sprite import Sprite 

class Astroid(Sprite):
    def __init__(self,ai_game):
        """initialize the block and it's starting position"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()


        # load the astroid image onto the screen 
        self.image = pygame.image.load('images/astroid.png')
        self.rect = self.image.get_rect()

        #astroid starting position 

        self.rect.center = self.screen_rect.center
    
        #astroid horizontal movement 

        self.x = float(self.rect.x)


    #add add collision detection for the astroid
    def check_edges(self):
        """Return True if astroid is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            #find out what we are returning true
            return True


    def blitAstroid(self):
        """Draw the astroid at its current location."""
        """This is probably only for after it moves and the while loop iterates"""
        self.screen.blit(self.image, self.rect)
    
    
    def update(self):
        self.x = self.x + self.settings.astroid_speed 
        
        if self.rect.right >= self.screen_rect.right: # turn the astroid to the left if it hits the right of screen
            self.settings.astroid_speed = -0.5
        
        if self.x <= 0: #If the astroid goes all the way to the left of the screen it turns right
            self.settings.astroid_speed = 0.5

        self.rect.x = self.x
    

 








 
        

