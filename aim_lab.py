

# Imports
import pygame
import math  # for checking for collisions with the mouse and the circle
import random

# Define the screen the screen and initialize pygame
pygame.init()

width = 1200
height = 500
display = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
purple = (128, 0, 128)
grey = (128, 128, 128)
sky = (0, 0, 220)
blue = (85, 206, 255)
orange = (255, 127, 80)
red = (200, 0, 0)
light_red = (255, 0, 0)
green = (0, 200, 0)
light_green = (0, 255, 0)
colors = [white, grey, purple, sky, blue, orange, red, light_red, green, light_green]

# Globals
clock = pygame.time.Clock()  # To set the frame rate


cx = random.randint(20, width - 20)
cy = random.randint(20, height - 20)
width_of_circle = random.randint(14, 20)
pygame.draw.circle(display, random.choice(colors), (cx, cy), width_of_circle)

carImg = pygame.image.load('img0.png')

def car(x,y): # this is actually not a car just an red rectangle for the test 
    display.blit(carImg, (x,y))


# Main loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    click = pygame.mouse.get_pressed()

    sqx = (x - cx)**2
    sqy = (y - cy)**2

    if math.sqrt(sqx + sqy) < width_of_circle and click[0] == 1:
        display.fill(black)  # Reset the screen
        cx = random.randint(20, width - 20)
        cy = random.randint(20, height - 20)
        width_of_circle = random.randint(14, 20)
        #pygame.draw.circle(display, random.choice(colors), (cx, cy), width_of_circle)
        car(cx,cy)
    pygame.display.update()
    clock.tick()
