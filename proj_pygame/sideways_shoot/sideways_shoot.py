import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf



def run_game():
    '''Main sidways shooter game'''
    
    #initialize game
    pygame.init()
    ai_settings = Settings()
    #Create screen surface
    screen = pygame.display.set_mode((ai_settings.width, 
        ai_settings.height))
    pygame.display.set_caption("Sideways Shooter")
    ship = Ship(ai_settings, screen)
    #Make a group to store bullets in
    bullets = Group()
    
    #Main Game Loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
    
    
