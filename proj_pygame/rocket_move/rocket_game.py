import pygame

from settings import Settings 
from rocket import Rocket
import game_funtions as gf

def run_game():
    """Initialize pygame, settings, and screen object"""
    pygame.init()
    rocket_settings = Settings()
    screen = pygame.display.set_mode(
        (rocket_settings.screen_width, rocket_settings.screen_height))
    pygame.display.set_caption("Rocket Game")
    
    #make a rocket
    rocket = Rocket(rocket_settings, screen)
    
    
    #start the main loop for the game
    while True:
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(rocket_settings, screen, rocket)
    
run_game()
