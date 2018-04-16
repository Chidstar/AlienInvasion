class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialise statistics."""
        self.ai_settings = ai_settings
        
        # Store high score
        self.high_score = 0
        
        self.reset_stats()
        
        # Start game in an inactive state.
        self.game_active = False
        
    def reset_stats(self):
        """Initialise stats that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
