import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
    """A class to represent raindrops."""
    
    def __init__(self, screen):
        """Initialise the rain and it's starting pos."""
        super().__init__()
        self.screen = screen
        
        self.image = pygame.image.load('images/rain.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        scr_rect = self.screen.get_rect()
        scr_height = scr_rect.height
        
        self.y = float(self.rect.y)
        
    def update(self):        
        """move rain drops down."""
        drop_y = self.y - (0.5 * self.y)
        self.rect.y = drop_y
    
    
