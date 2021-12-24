import pygame
import pygame_gui
import math

# Screen constants
FPS = 100
screen_size_x = 1280
screen_size_y = 720


pygame.init()

# Set window name.
pygame.display.set_caption('Astraeus Engine Test')

# Main surface/manager settings.
window_surface = pygame.display.set_mode((screen_size_x, screen_size_y))
manager = pygame_gui.UIManager((screen_size_x, screen_size_y), 'theme.json')
background = pygame.Surface((screen_size_x, screen_size_y))

background.fill(pygame.Color('#000000'))

# Main Game Loop.
clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0

    # Iterate through the event stack.
    for event in pygame.event.get():

        ### Keydown loop ###
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and event.mod == pygame.KMOD_NONE:
                print('K_RIGHT')
            if event.key == pygame.K_RIGHT and event.mod & pygame.KMOD_LSHIFT:
                print('K_RIGHT + LEFT SHIFT!')
            if event.key == pygame.K_LEFT:
                print('K_LEFT')
            if event.key == pygame.K_UP:
                print('K_UP')
            if event.key == pygame.K_DOWN:
                print('K_DOWN')
            if event.key == pygame.K_ESCAPE: # Pressing Escape ends main loop
                is_running = False


    manager.update(time_delta)
    background.fill((0, 0, 0))

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
    clock.tick(FPS)


### WILL QUIT THE GAME ###
pygame.QUIT
