import pygame

from pygame.sprite import Sprite

class Missle(Sprite):
    def __init__(self, ai_game):
        """Create a missle object"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        #probably not needed

        # Create a bullet rect at (0, 0) and then set correct position. # <----convert this for missles 
        self.image = pygame.image.load('images/missle.png')
        self.rect = self.image.get_rect()

        #add-maybe use this self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            #add self.settings.bullet_height)

        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Store the bullet's position as a decimal value. # for missles
        self.y = float(self.rect.y)

    def update(self):
        """Move the missle up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.missle_speed
        # Update the rect position.
        self.rect.y = self.y
        

    def draw_missle(self):
        """Draw the missle to the screen."""
        pygame.draw.rect(self.screen, self.rect)
    
    def blitMissle(self):
       self.screen.blit(self.image, self.rect)