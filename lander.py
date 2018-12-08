# Tom Baker
# Moon Lander

import pygame
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moon Lander")
background = pygame.image.load("background.bmp")
nothrust = pygame.image.load("lander.bmp")
nocrash = pygame.image.load("lander.bmp")
crash = pygame.image.load("crash.bmp")
thrust = pygame.image.load("landerthrust.bmp")
thrust.set_colorkey(WHITE)
nothrust.set_colorkey(WHITE)
crash.set_colorkey(WHITE)
nocrash.set_colorkey(WHITE)
fuel = 100

win_state = ""

lander_x = 320
lander_y = 0
lander_x_speed = 0
lander_LEFT_speed = 0
lander_RIGHT_speed = 0
lander_FALL_speed = 0
lander_FALL = True
lander_LEFT = False
lander_RIGHT = False
speed_color = GREEN
fuel_color = GREEN

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                lander_FALL = True
            if event.key == pygame.K_RIGHT:
                lander_RIGHT = False
            if event.key == pygame.K_LEFT:
                lander_LEFT = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                lander_RIGHT = True
            if event.key == pygame.K_LEFT:
                lander_LEFT = True
            if event.key == pygame.K_SPACE:
                lander_FALL = False

    # If keys are pressed, move lander.
    if fuel > 0 and not lander_FALL:
        fuel -= 1
        lander = thrust
        lander_FALL_speed -= .05
        if lander_FALL_speed < -3:
            lander_FALL_speed = -3
    if lander_RIGHT:
        lander_RIGHT_speed += .05
        if lander_RIGHT_speed > 2:
            lander_RIGHT_speed = 2
    if lander_LEFT:
        lander_LEFT_speed -= .05
        if lander_LEFT_speed < -2:
            lander_LEFT_speed = -2

    # If no keys are pressed, make lander fall straight down.
    if lander_FALL:
        lander = nothrust
        lander_FALL_speed += .05
        if lander_FALL_speed > 8:
            lander_FALL_speed = 8
    if not lander_RIGHT:
        lander_RIGHT_speed -= .05
        if lander_RIGHT_speed < 0:
            lander_RIGHT_speed = 0
    if not lander_LEFT:
        lander_LEFT_speed += .05
        if lander_LEFT_speed > 0:
            lander_LEFT_speed = 0

            # If lander hits the ground, what happens?
    if lander_y > 404 and lander_FALL_speed > 1.5:
        lander = crash
        win_state = "YOU LOSE"
        done = True
    if lander_y > 404 and lander_FALL_speed < 1.6:
        lander = nocrash
        win_state = "YOU WIN"
        done = True

    # Set lander coords to manipulated variable values.
    lander_x_speed = lander_LEFT_speed + lander_RIGHT_speed
    lander_x += lander_x_speed
    lander_y += lander_FALL_speed

    # Keep lander on the screen.
    if lander_x > 650:
        lander_x = 650
    if lander_x < 0:
        lander_x = 0
    if lander_y > 405:
        lander_y = 405

    # Change speed display color
    if lander_FALL_speed > 1.5:
        speed_color = RED
    else:
        speed_color = GREEN
    if fuel < 50:
        fuel_color = RED

    # Update alt and fall variables for display
    altitude = round(405 - lander_y, 1)
    fall = round(5 * lander_FALL_speed, 1)

    # Drawing code
    screen.blit(background, [0, 0])
    screen.blit(lander, [lander_x, lander_y])
    font = pygame.font.SysFont('Calibri', 25, True, False)
    fall_display = font.render("SPEED: " + str(fall), True, speed_color)
    screen.blit(fall_display, [0, 445])
    alt_display = font.render("ALT: " + str(altitude), True, GREEN)
    screen.blit(alt_display, [0, 470])
    fuel_display = font.render("FUEL: " + str(fuel), True, fuel_color)
    screen.blit(fuel_display, [230, 470])

    if lander == crash or lander == nocrash:
        state_font = pygame.font.SysFont('Calibri', 50, True, False)
        state_display = state_font.render(win_state, True, RED)
        screen.blit(state_display, [275, 200])

    # Update screen
    pygame.display.flip()
    clock.tick(60)

    print(fuel)

time.sleep(3)
pygame.quit()