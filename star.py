import pygame
from pygame.sprite import Sprite
from pygame import Surface

from resources import get_resource

class Star(Sprite):
    """Class to define stars in the game"""

    def __init__(self,
            screen : Surface):
        """Initialize star object"""
        super(Star, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image_path = get_resource("images/star.png")
        self.image = pygame.image.load(self.image_path)
        self.image.set_alpha(100)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


    def draw(self):
        """Draw star to the screen"""
        self.screen.blit(self.image, self.rect)