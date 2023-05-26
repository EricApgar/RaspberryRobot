import pygame, sys
from adafruit_motorkit import MotorKit


# Init the motors.
kit = MotorKit()

# Set up pygame.
pygame.init()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
# windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.HIDDEN)

current_status = {
    'F': False,
    'B': False,
    'L': False,
    'R': False}

def status_to_motor(current_status: dict):

    # If only left/right is pressed, the pivot.
    # If F/B + L/R then F/B @ 50% + L/R @ 25%

    num_status = current_status
    for key, val in num_status.items():  # Translate True/False to 1/0
        num_status[key] = 1 if val else 0

    if current_status['F'] and current_status['B']:
        current_status['F'], current_status['B'] = False, False
    if current_status['L'] and current_status['R']:
        current_status['L'], current_status['R'] = False, False

    # F:  L@+0.8 U R@+0.8
    # B:  L@-0.8 U R@-0.8
    # L:  L@-1.0 U R@+1.0
    # R:  L@+1.0 U R@-1.0
    # FL: L@+0.8 U R@+1.0
    # FR: L@+1.0 U R@+0.8
    # BL: L@-0.8 U R@-1.0
    # BR: L@-1.0 U R@-0.8

    if current_status['F']:
        if current_status['R']:
            kit.motor1.throttle = 1.0
            kit.motor2.throttle = .9
        elif current_status['L']:
            kit.motor1.throttle = .9
            kit.motor2.throttle = 1.0
        else:  # Just forward.
            kit.motor1.throttle = .9
            kit.motor2.throttle = .9

    elif current_status['B']:
        if current_status['R']:
            kit.motor1.throttle = -1.0
            kit.motor2.throttle = -.9
        elif current_status['L']:
            kit.motor1.throttle = -.9
            kit.motor2.throttle = -1.0
        else:  # Just forward.
            kit.motor1.throttle = -.9
            kit.motor2.throttle = -.9
    
    elif current_status['L']:
        kit.motor1.throttle = -1
        kit.motor2.throttle = 1
    elif current_status['R']:
        kit.motor1.throttle = 1
        kit.motor2.throttle = -1

    else:
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0

    # kit.motor1.throttle = None  # Set motor to coast.
    return

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
                current_status['L'] = True
                print('Press: Left')
            if event.key == pygame.K_RIGHT:
                current_status['R'] = True
                print('Press: Right')
            if event.key == pygame.K_UP:
                current_status['F'] = True
                print('Press: UP')
            if event.key == pygame.K_DOWN:
                current_status['B'] = True
                print('Press: DOWN')

        if event.type == pygame.KEYUP:
            # Change the keyboard variables.
            if event.key == pygame.K_LEFT:
                current_status['L'] = False
                print('Un-press: Left')
            if event.key == pygame.K_RIGHT:
                current_status['R'] = False
                print('Un-press: Right')
            if event.key == pygame.K_UP:
                current_status['F'] = False
                print('Un-press: UP')
            if event.key == pygame.K_DOWN:
                current_status['B'] = False
                print('Un-press: DOWN')

        status_to_motor(current_status)

