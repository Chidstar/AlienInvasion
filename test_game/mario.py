#Module modelling mario character and its behavios

import pygame

class Mario():
    """Test class for Mario image and behaviors."""
    
    def __init__(self, ai_settings, screen):
        """Initialise mario and set starting position."""
        self.screen = screen # to keep mario within the screen size
        self.ai_settings = ai_settings # to access speed attribute
        
        #load mario image and get its rect
        self.image = pygame.image.load('images\mario.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Start each new mario at bottom left of screen
        self.rect.left = self.screen_rect.left
        self.rect.bottom = self.screen_rect.bottom
        
        # Store decimal value for mario's center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Update mario's position based on movement flag."""
        # Update ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.mario_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.mario_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.mario_speed_factor
        elif self.moving_down and self.rect.bottom != self.screen_rect.bottom:
            self.centery += self.ai_settings.mario_speed_factor
    
        #Update rect object from self.center.
        self.rect.centerx = self.centerx #rect.centerx controls the
        #movement. if it isn't updated according to what we are changing
        #the attribnute 'self.centerx' by, nothing will happen.
        self.rect.centery = self.centery
        
    def blitme(self):
        """Draw mario at its current location."""
        self.screen.blit(self.image, self.rect)
        
