import pygame

from pygame.sprite import Sprite

class Missile(Sprite):
    def __init__(self, ai_game):
        """Create a missile object"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.color = self.settings.missile_color
        #probably not needed

        # Create a missile rect at (0, 0) and then set correct position. # <----convert this for missiles 
        self.image = pygame.image.load('images/missile.png')
        self.rect = self.image.get_rect()



        #FIXME:-maybe use this self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
        #self.settings.bullet_height)
            # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.missile_height, self.settings.missile_width)
           
        #puts missile rect at the top of the ship
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value. # for missiles
        self.y = float(self.rect.y)

    def update(self):
        """Move the missile up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.missile_speed
        # Update the rect position.
        self.rect.y = self.y


    def draw_missile(self):
        """Draw the missile to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)#TODO:Hope this with the self.image draws a ship 
        self.screen.blit(self.image, self.rect)
        
    
    #FIXME:def blitMissile(self):
       #self.screen.blit(self.image, self.rect)