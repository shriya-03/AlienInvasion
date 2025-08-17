import pygame

class Bullet:    

    def __init__(self, game):#pass in the full game, so bullet can access the screen, settings, and ship
        self.screen = game.screen#Store the screen to draw the bullet later.
        self.settings = game.settings#Use the bullet speed from settings

        
        self.rect = pygame.Rect(0, 0, 30, 30)
        self.rect.midtop = game.ship.rect.midtop  # Start at ship's top Places bullet on top of the ship when it is fired.

        self.color = (255, 0, 0)  # Red bullet
        self.speed = 1.0  # Pixels per frame

        

    def update(self):
        self.rect.y = self.rect.y - self.speed#Every frame, move bullet up (y decreases).
       

    def draw(self):        
        pygame.draw.rect(self.screen, self.color, self.rect)#Draws the bullet on the screen.


        
      
