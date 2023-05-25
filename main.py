import pygame, sys


# Set up pygame.
pygame.init()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
# windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.HIDDEN)

# Run the game loop.
while True:

# Check for events.
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # Change the keyboard variables.
            if event.key == pygame.K_LEFT:
                print('Press: Left')
            if event.key == pygame.K_RIGHT:
                print('Press: Right')
            if event.key == pygame.K_UP:
                print('Press: UP')
            if event.key == pygame.K_DOWN:
                print('Press: DOWN')

        if event.type == pygame.KEYUP:
            # Change the keyboard variables.
            if event.key == pygame.K_LEFT:
                print('Un-press: Left')
            if event.key == pygame.K_RIGHT:
                print('Un-press: Right')
            if event.key == pygame.K_UP:
                print('Un-press: UP')
            if event.key == pygame.K_DOWN:
                print('Un-press: DOWN')