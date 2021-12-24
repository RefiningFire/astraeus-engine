import pygame
import pygame_gui
import math
import classes

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


test_ship = classes.Ship(5,5)
print(f'total mass: {test_ship.stats.mass}')
print(f'engines mass: {test_ship.engines.stats.mass}')
print(f'chassis mass: {test_ship.chassis.stats.mass}')

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
                test_ship.engines.propulsion.power_move_right()
            if event.key == pygame.K_RIGHT and event.mod & pygame.KMOD_LSHIFT:
                test_ship.engines.propulsion.power_rotate_right()
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
