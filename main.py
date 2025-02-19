# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here

    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config

        # Add the new code below this comment

        # Draw on the screen multiple lines starting from (0, 10) to (100, 110)
        # Each line will have a width of 5 pixels
        thickness = 5
        for y_offset in range(0, 100, 10):
            pygame.draw.line(screen, config.RED, [0, 10 + y_offset], [100, 110 + y_offset], thickness)

       
        pygame.display.flip()

        # Limit the frame rate to the specified frames per second (FPS) 
        clock.tick(config.FPS)

    
    pygame.quit()
    sys.exit()

if __name__== "__main__":
    main()
