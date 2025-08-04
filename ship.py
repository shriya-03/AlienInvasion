import pygame

class Ship:
    """A class to manage the player's ship."""

    def __init__(self, alien_invasion_object): #Takes the game instance (AlienInvasion) as a parameter to get screen and settings.
        self.screen = alien_invasion_object.screen #Stores screen and settings
        self.settings = alien_invasion_object.settings
        self.screen_rect = alien_invasion_object.screen.get_rect()#This gives rectangle,Useful for positioning the ship

        # Load and scale the ship image
        self.image = pygame.image.load('ship.jpg') #self.image is the ship image
        self.image = pygame.transform.scale(self.image, (60, 48))#Resizing  image to a width of 60 pixels and height of 48 pixels.
        self.rect = self.image.get_rect()#self.rect tells Pygame width and height of the ship

        # Start at bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement
        self.moving_right = False
        self.moving_left = False






    def update(self):#This is the method that updates the ship’s position on screen.
       if self.moving_right:# check Is the player currently holding the right arrow key?
        #If yes, we want to move the ship right... but only if it's not at the edge.
           if self.rect.right < self.screen_rect.right:
               self.rect.x = self.rect.x + self.settings.ship_speed#This moves the ship right by adding to its x-position.
#The amount added is set in Settings.py in ship_speed = 1.5 So each frame it moves 1.5 pixels to the right.

# self.rect.right is the x-position of the right edge of the ship.
# self.screen_rect.right is the x-position of the right edge of the screen.
# This condition checks:
# “Is the ship still inside the right side of the screen?”
# If yes, then move.



       if self.moving_left:#Same as before, but checking if the player is holding the left arrow key.
        #self.rect.left is the x-position of the left edge of the ship.
            if self.rect.left > 0:#check:“Is the ship’s left edge still inside the screen (not past 0)?”
               self.rect.x = self.rect.x - self.settings.ship_speed
#Moves the ship left by subtracting from its x-position.

    def blitme(self):#blit() means to draw the image.
        self.screen.blit(self.image, self.rect)#This line draws the ship image on the screen at the location stored in self.rect.
# This is called every frame in the game loop after updating movement, so it draws the ship in its new position.

