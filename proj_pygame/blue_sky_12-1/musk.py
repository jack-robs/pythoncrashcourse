import pygame

class Musk():
    
    def __init__(self, screen):
        """Initialize the musk and set its starting positoin"""
        self.screen = screen
        
        #load the musk image and get its rect
        self.image = pygame.image.load('images/musk.bmp')
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #start each new musk at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        """Draw the musk at its current location."""
        self.screen.blit(self.image, self.rect)
        
