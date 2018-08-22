# Alien Invasion game created with pygame

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # Initialise pygame and screen object
    pygame.init()
    ai_settings = Settings()    # Create instance of settings module
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make a play button.
    play_button = Button(ai_settings, screen, "Play")
    
    # Create an instance to store game statistics and create a scorebrd
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Make a ship, a group of bullets and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Start the main loop for the game
    while True:
    
        #Watch for keyboard and mouse events with function
        gf.check_events(ai_settings, screen, stats, sb, play_button, 
            ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
            bullets, play_button)
        
        if stats.game_active:            
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, 
                aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, 
            bullets)
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, 
            bullets, play_button)
        
        else:
            filename = 'hiscores.txt'
            with open (filename, 'w') as f_obj:
                f_obj.write(str(stats.high_score))

run_game()
