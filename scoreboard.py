# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 21:46:08 2022

@author: Studi
"""

#%%
import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
        """A class to report scoring information."""
        
        def __init__(self, ai_game):
            """Initialize scorekeeping attributes."""
            self.ai_game = ai_game
            self.screen = ai_game.screen
            self.screen_rect = self.screen.get_rect()
            self.settings = ai_game.settings
            self.stats = ai_game.stats
            
            # Font settings for scoring information.
            self.text_color = (30, 30, 30)
            self.font = pygame.font.SysFont(None, 48)
            
            # Prepare the initial score images.
            self.prep_score()
            self.prep_alltime_high()
            self.prep_high_score()
            self.prep_level()
            self.prep_ships()
            
        def prep_score(self):
            """Turn the score into a rendered image."""
            rounded_score = round(self.stats.score, -1)
            score_str = "{:,}".format(rounded_score)
            self.score_image = self.font.render(score_str, True,
                                                self.text_color,
                                                self.settings.bg_color)
            
            # Display the score at the top right of the screen.
            self.score_rect = self.score_image.get_rect()
            self.score_rect.right = self.screen_rect.right - 20
            self.score_rect.top = 20
        
        def prep_alltime_high(self):
            """Turn the all time high score into a rendered image."""
            alltime_high = round(int(self.stats.alltime_high), -1)
            alltime_high_str = ("All Time High Score: " +
                                "{:,}".format(alltime_high))
            self.alltime_high_image = self.font.render(alltime_high_str, True,
                        self.text_color, self.settings.bg_color)
            
            # Center the all time high score at the top of the screen.
            self.alltime_high_rect = self.alltime_high_image.get_rect()
            self.alltime_high_rect.centerx = self.screen_rect.centerx
            self.alltime_high_rect.top = self.score_rect.top
            
        def prep_high_score(self):
            """Turn the session high score into a rendered image."""
            high_score = round(self.stats.high_score, -1)
            high_score_str = ("Session High Score: " +
                              "{:,}".format(high_score))
            self.high_score_image = self.font.render(high_score_str, True,
                    self.text_color, self.settings.bg_color)
            
            # Center the high score at the top of the screen beneath the all
            # time high score.
            self.high_score_rect = self.high_score_image.get_rect()
            self.high_score_rect.centerx = self.screen_rect.centerx
            self.high_score_rect.top = self.alltime_high_rect.bottom + 10
            
        def prep_level(self):
            """Turn the level into a rendered image."""
            level_str = str(self.stats.level)
            self.level_image = self.font.render(level_str, True,
                    self.text_color, self.settings.bg_color)
            
            # Position the level below the score.
            self.level_rect = self.level_image.get_rect()
            self.level_rect.right = self.score_rect.right
            self.level_rect.top = self.score_rect.bottom + 10
            
        def prep_ships(self):
            """Show how many ships are left."""
            self.ships = Group()
            for ship_number in range(self.stats.ships_left):
                ship = Ship(self.ai_game)
                ship.rect.x = 10 + ship_number * ship.rect.width
                ship.rect.y = 10
                self.ships.add(ship)
                    
        def show_score(self):
            """Draw scores, level, and ships to the screen."""
            self.screen.blit(self.score_image, self.score_rect)
            self.screen.blit(self.alltime_high_image, self.alltime_high_rect)
            self.screen.blit(self.high_score_image, self.high_score_rect)
            self.screen.blit(self.level_image, self.level_rect)
            self.ships.draw(self.screen)

        def check_alltime_high(self):
            """Check to see if there's a new all time high score."""
            if int(self.stats.score) > int(self.stats.alltime_high):
                self.stats.alltime_high = self.stats.score
                alltime_high_save = open('alltime_high.txt', 'w')
                alltime_high_save.write(str(self.stats.alltime_high))
                alltime_high_save.close()
                # test_print_alltime = open('alltime_high.txt', 'r')
                # print(test_print_alltime.read())
                # test_print_alltime.close()
                self.prep_alltime_high()
            
        def check_high_score(self):
            """Check to see if there's a new session high score."""
            if self.stats.score > self.stats.high_score:
                self.stats.high_score = self.stats.score
                self.prep_high_score()
