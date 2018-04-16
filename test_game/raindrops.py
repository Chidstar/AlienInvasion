import sys
import pygame
from pygame.sprite import Group

def run_game():
    # Initialise pygame and screen object
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Raindrop, Droptop")
    
    bg_colour = (0, 0, 122)
    
    drop = pygame.image.load('images/rain.bmp')
    rect = drop.get_rect()
    drop_width = rect.width
    scr_rect = screen.get_rect()
    scr_height = scr_rect.height
    drop_y = rect.height - (0.5 * rect.height)
    drops = Group()
    
    scr_width = scr_rect.width
    
    avail_space_x = scr_width - drop_width
    num_drops_x = int(avail_space_x / drop_width)

    
    for drop_num in range(num_drops_x):
        drop = pygame.image.load('images/rain.bmp')
        drop_rect = drop.get_rect()
        drop_width = drop_rect.width
        drop_x = (drop_width + drop_width * drop_num)
        drop_rect = (drop_x, drop_y)
        screen.blit(drop, drop_rect)   
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
    
        screen.fill(bg_colour)
        
        for drop_num in range(num_drops_x):
            drop = pygame.image.load('images/rain.bmp')
            drop_rect = drop.get_rect()
            drop_width = drop_rect.width
            drop_x = (drop_width + drop_width * drop_num)
            drop_rect = (drop_x, drop_y)
            screen.blit(drop, drop_rect)   
    
        pygame.display.flip()

run_game()
