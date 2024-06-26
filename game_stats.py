# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:29:30 2022

@author: Studi
"""

#%%
class GameStats:
    """Track statistics for Alien Invastion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False
        
        # Session high score resets when program is closed.
        self.high_score = 0
        
        # All time high score should never be reset.
        self.alltime_high_file = open('alltime_high.txt', 'r')
        self.alltime_high = self.alltime_high_file.read()
        self.alltime_high_file.close()
                
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    