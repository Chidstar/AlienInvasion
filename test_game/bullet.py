""" Module that contains bullet class"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired."""
    
    def __init__(self, ai_settings, screen, mario):
        """Create a bullet object at Mario's current position."""
        super().__init__()
        self.screen = screen
        
        # Create a bullet at rect (0,0) and then set correct position
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = mario.rect.centerx
        self.rect.centery = mario.rect.centery
        self.rect.right = mario.rect.right
        
        # Store position as a decimal value
        self.x = float(mario.rect.right)
        
        self.colour = ai_settings.bullet_colour
        self.speed_factor = ai_settings.bullet_speed
        
    def update(self):
        """Move the bullet to the right of the screen."""
        # Update the decimal position of the bullet
        self.x += self.speed_factor
        self.rect.x = self.x
    
    def draw_bullet(self):
        """Draw bullet to screen."""
        pygame.draw.rect(self.screen, self.colour, self.rect)
    
