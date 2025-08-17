import pygame

class Alien:
    def __init__(self, alien_invasion_object, position="center"):
        self.screen = alien_invasion_object.screen
        self.settings = alien_invasion_object.settings
        self.screen_rect = self.screen.get_rect()

        
        self.image = pygame.image.load('alien.png')
        self.image = pygame.transform.scale(self.image, (60, 48))
        self.rect = self.image.get_rect()

        
        if position == "center":
            self.rect.midtop = self.screen_rect.midtop
        elif position == "left":
            self.rect.topleft = self.screen_rect.topleft
        elif position == "right":
            self.rect.topright = self.screen_rect.topright

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        #blit() is from Pygame which will draw a image at a particular position

     