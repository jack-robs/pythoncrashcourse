'''
(1) Create an empty screen
(2) In event loop: print event.key attribute after pygame.KEYDOWN
(3) Run program
'''
import sys
import pygame

def run_game():
    #Main game program 
    
    #initialize the game
    pygame.init()
    #make a screen surface 
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Key presses game")
    while True:
        #catches events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
            
        pygame.display.flip()
        
run_game()
