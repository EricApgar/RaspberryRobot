# Print on/off key press status for the arrow keys.

import pygame


pygame.init()



# pygame.K_UP
# pygame.K_DOWN
# pygame.K_LEFT
# pygame.K_RIGHT

# while True:

# #     print('here')
#     pressed_keys = pygame.key.get_pressed()
    
#     if pressed_keys[pygame.K_UP]:
#         print('UP')

#     pygame.event.pump()
#     print('there')



# is_moving = False

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
#             # is_moving = True
#             print('DOWN')
#         elif event.type == pygame.KEYUP and event.key == pygame.K_m:
#             print('m')
#         pygame.event.pump()

# done = False
# clock = pygame.time.Clock()

# while not done:
#     clock.tick(60)

#     keyState = pygame.key.get_pressed()

#     if keyState[pygame.K_UP]:
#         print('\nGame Shuting Down!')
#         done = True

#     pygame.event.pump()

while True:
    # print('Looking...')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass
 
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        print("w is pressed")