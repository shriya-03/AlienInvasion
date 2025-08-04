import sys
import pygame
from Settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()#Starts all the Pygame features (like sound, graphics, etc.).
        self.settings = Settings() #Creates a Settings object so we can use screen size, ship speed, etc., from Settings.py
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #Creates the game window using the width/height from the Settings object.
        pygame.display.set_caption("Alien Invasion")
        

        # Set the background color.
        self.bg_color = self.settings.bg_color

        # Create a ship.
        self.ship = Ship(self)

        self.bullet = None  # No bullet on screen at start
# Creates the player’s ship.
# Passes the self object (the whole game) so the ship can access the screen and settings.

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():#Goes through a list of things that happened (key presses, mouse clicks, etc.).
                if event.type == pygame.QUIT:#X button, the program ends.
                    sys.exit()
                elif event.type == pygame.KEYDOWN: #If the player pressed a key down
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True

                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                           if self.bullet is None:  # Only fire if no bullet
                               self.bullet = Bullet(self)

                elif event.type == pygame.KEYUP:#If the player released a key
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False

                


            self.ship.update()
            #Calls the update() method from ship.py.
#This checks the flags moving_right and moving_left, and moves the ship if needed.
            # Update bullet
            if self.bullet:
    # Only update position if bullet is not at top
               if self.bullet.rect.top > 0:
                   self.bullet.update()





            self.screen.fill(self.bg_color)
            if self.bullet:
                self.bullet.draw()
            self.ship.blitme()
            pygame.display.flip()
# painting a picture behind a curtain.
# screen.fill- wipe the canvas clean.
# blitme- draw the ship.
# flip-pull back the curtain to show what you painted.


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
