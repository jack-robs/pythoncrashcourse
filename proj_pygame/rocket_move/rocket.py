import pygame

class Rocket():
    
    def __init__(self, rocket_settings, screen):
        '''Initialize the rocket, and set its starting posiiton'''
        self.screen = screen
        self.rocket_settings = rocket_settings
        
        #load the rocket image, and get its rect
        self.image = pygame.image.load('images/nat.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Start each new rocket at the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        #store a decimale value for the rocket's center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
   
    def update(self):
        '''Update the ship's positionbased on the movement flag.'''
        #update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.rocket_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.rocket_settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.rocket_settings.rocket_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.rocket_settings.rocket_speed_factor
            
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        
