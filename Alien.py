import pygame
class Alien:
    def __init__(self,alien_invasion_object):
        self.screen = alien_invasion_object.screen #Stores screen and settings
        self.settings = alien_invasion_object.settings
        self.screen_rect = alien_invasion_object.screen.get_rect()
        

        self.image = pygame.image.load('alien.png')
        self.image = pygame.transform.scale(self.image, (60, 48))
        self.rect = self.image.get_rect()

        self.rect.midtop = self.screen_rect.midtop

   
    def blitme(self):#Draws the alien at its current position on the screen.
        self.screen.blit(self.image, self.rect)

     