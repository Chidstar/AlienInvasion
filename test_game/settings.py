#Create a settings class

class Settings():
    """A class to store all settings for the game."""
    
    def __init__(self):
        """Initialise the game's settings."""
        #Screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_colour = (198, 221, 255)
        
        # Mario settings
        self.mario_speed_factor = 1
        
        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = (255, 0, 0)
        self.bullet_speed = 1
