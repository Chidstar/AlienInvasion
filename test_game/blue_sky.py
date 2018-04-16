#Create a game that moves an image all across the surface

import pygame
from pygame.sprite import Group

from settings import Settings
from mario import Mario
import game_functions as gf


def run_game():
    # Initialise game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Blue Sky")
    
    #Bring in Mario
    #Feed screen attributes to set Mario's position relative
    #to the screen size
    mario = Mario(ai_settings, screen) 
    
    # Create a group for the bullets
    bullet = Group()
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, mario, bullet)    
        mario.update()
        gf.update_bullets(bullet)
        
        gf.update_screen(ai_settings, screen, mario, bullet)

        
run_game()
