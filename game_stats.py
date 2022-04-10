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
        
    def reset_stats(self):
        """Initialize statisticsthat can change during the game."""
        self.ships_left = self.settings.ship_limit
        