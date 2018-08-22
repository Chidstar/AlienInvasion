#Make empty Pygame screen with keypres events

import sys

import pygame

def run_game():
    """Initialise game and create screen."""
    
    pygame.init()
    screen = pygame.display.set_mode((300,300))
    pygame.display.set_caption("Keys")
    
    
    #Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event)
                print("Down")

run_game()
