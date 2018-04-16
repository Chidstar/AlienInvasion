import sys
import pygame
from pygame.sprite import Group
from random import randint

def run_game():
    """Main body of running game."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Stars")
    
    bg_colour = (7, 39, 188)
    
    star = pygame.image.load('images/star.bmp.')
    rect = star.get_rect()
    star_width = rect.width
    star_height = rect.height
    stars = Group()

    scr_rect = screen.get_rect()
    scr_width = scr_rect.width
    scr_height = scr_rect.height
    
    avail_space_x = scr_width - star_width
    num_stars_x = int(avail_space_x / (star_width))
    avail_space_y = scr_height - star_height
    num_stars_y = int(avail_space_y / (star_height))
    flag = 0

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                sys.exit()
                
        screen.fill(bg_colour)
        
        while flag < num_stars_y:
            for star_num in range(num_stars_x):
                for row_num in range(num_stars_y):
                    star = pygame.image.load('images/star.bmp.')
                    rect = star.get_rect()
                    star_width = rect.width
                    star_height = rect.height
                    ran_x = randint(-10,10)
                    ran_y = randint(-10,10)
                    star_x = (star_width + star_width * star_num) + ran_x
                    star_y = (star_height +  star_height * row_num) + ran_y
                    star_rect = (star_x, star_y)
                    print(star_num, row_num, star_rect)
                    flag += 1
                    screen.blit(star, star_rect)
            
            pygame.display.flip()
run_game()

    
