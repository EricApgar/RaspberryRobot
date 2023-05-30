import pygame, sys
import pygame.camera
from adafruit_motorkit import MotorKit


# Init the motors.
kit = MotorKit()

# Set up pygame.
pygame.init()
pygame.camera.init()

# Setup the camera.
screen = pygame.display.set_mode((640, 480), 0)
cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0], (32, 24))
cam.start()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400

# window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
# window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.HIDDEN)

current_status = {
    'F': False,
    'B': False,
    'L': False,
    'R': False}

def status_to_motor(orig_status: dict):

    # If only left/right is pressed, the pivot.
    # If F/B + L/R then F/B @ 50% + L/R @ 25%

    current_status = orig_status

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

    image1 = cam.get_image()
    image1 = pygame.transform.scale(image1, (640, 480))
    screen.blit(image1, (0, 0))
    pygame.display.update()

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

