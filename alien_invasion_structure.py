# Basic structure for a game written in Pygame:

import sys  # For system specific parameter and functions

import pygame   # For functionality needed to make a game

def run_game():
    # Initialise game and create a screen object
    pygame.init()   # Initialises background that pygame needs to work
    screen = pygame.display.set_mode((1200, 800))   #set pixel dimension
    pygame.display.set_caption("Alien Invasion")
    
    # Set the background colour.
    bg_colour = (230, 230, 230)
    
    # Start the main loop for the game.
    while True:
        
        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #Redraw the screen during each pass through the loop
        screen.fill(bg_colour)  #screen.fil() method take colour arg
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
run_game()
