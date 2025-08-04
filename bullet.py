import pygame

class Bullet:
    

    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings

        
        self.rect = pygame.Rect(0, 0, 30, 30)
        self.rect.midtop = game.ship.rect.midtop  # Start at ship's top

        self.color = (255, 0, 0)  # Red bullet
        self.speed = 3.0  # Pixels per frame

    def update(self):
        self.rect.y = self.rect.y - self.speed
       

    def draw(self):
        
        pygame.draw.rect(self.screen, self.color, self.rect)


        
      
