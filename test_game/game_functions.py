# Module that controls game functions and events

import sys
import pygame           

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, mario, bullet):
    """Respomnd to keydown events."""
    if event.key == pygame.K_RIGHT:
        mario.moving_right = True
    elif event.key == pygame.K_LEFT:
        mario.moving_left = True
    elif event.key == pygame.K_UP:
        mario.moving_up = True
    elif event.key == pygame.K_DOWN:
        mario.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, mario, bullet)
    
def check_keyup_events(event, mario):
    """Respond to keyup events."""
    if event.key == pygame.K_RIGHT:
         mario.moving_right = False
    elif event.key == pygame.K_LEFT:
        mario.moving_left = False
    elif event.key == pygame.K_UP:
        mario.moving_up = False
    elif event.key == pygame.K_DOWN:
        mario.moving_down = False
    
def check_events(ai_settings, screen, mario, bullet):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, mario, bullet)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mario)

def fire_bullet(ai_settings, screen, mario, bullet):
    """Fire bullet from mario."""
    new_bullet = Bullet(ai_settings, screen, mario)
    bullet.add(new_bullet)

def update_screen(ai_settings, screen, mario, bullet):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through loop
    screen.fill(ai_settings.bg_colour)
    
    # Redraw all bullets behind ship and aliens.
    for bullet in bullet.sprites():
        bullet.draw_bullet()
    
    mario.blitme()
    
    # Make most recent screen visible
    pygame.display.flip()

def update_bullets(bullet):
    # Update bullet position
    bullet.update()
    
    # ~ # Get rid of bullet that has disappeared
    # ~ for bulet in bullet.copy():
        # ~ if bulet.rect.left >= screen.rect.right:
            # ~ bullet.remove(bulet)
