# Module containing ship class for behaviors

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Class for ship image and behaviors"""
    
    def __init__(self,ai_settings, screen):
        """Initialise ship and starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #Load the ship imag3e and get its rect.
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom centre of screen.
        self.rect.centerx = self.screen_rect.centerx   #centre x value
        self.rect.bottom = self.screen_rect.bottom #bottom y value
        
        # Store a decimal value for the ship's centre.
        self.center = float(self.rect.centerx)
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        # ~ if self.moving_right:
            # ~ self.rect.centerx += 1
        # ~ if self.moving_left:
            # ~ self.rect.centerx -= 1
                    
        #Edit: update the ship's center attribute, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # Update rect object from self.center.
        self.rect.centerx = self.center
    
    def center_ship(self):
        """"Center the ship on the screen."""
        self.center = self.screen_rect.centerx
    
    def blitme(self): #draws image to screen with specified rect
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
