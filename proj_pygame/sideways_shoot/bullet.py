import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from ship"""
    
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current location"""
        super().__init__()
        self.screen = screen 
        
        #Create a bullet rect at (0,0) and set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
            ai_settings.bullet_height)
        
        self.rect.left = ship.rect.left
        self.rect.top = self.rect.top 
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        self.y = float(self.rect.left)
    
        
    def update(self):
        """Move the bullet across the screen"""
        self.y -= self.speed_factor
        self.rect.left = self.y
        
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
        
