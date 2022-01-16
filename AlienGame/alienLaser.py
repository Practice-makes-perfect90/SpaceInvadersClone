import pygame
import os

from pygame.sprite import Sprite



class UfoLaser(Sprite):
    """A class to manage lasers fired from the aliens"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.ufoLaser_Color
        self.laser = pygame.mixer.Sound(os.path.join('Audio/laser.mp3'))

        # Create a laser rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.ufoLaser_width,
                                self.settings.ufoLaser_height)
        ### FIX THIS!
        self.rect = ai_game.alien.rect.midtop


        # Store the lasers position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move aliens laser down the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_ufo_laser(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

        pygame.mixer.Sound.play(self.laser)