import pygame, sys
import math
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

x = 400
y = 300

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((30, 30, 30))
    x += random.randrange(-4,4)
    y += random.randrange(-4,4)
    if x > screen.get_width() or x < 0 or y < 0 or y > screen.get_height():
        x = 400
        y = 300
    pygame.draw.circle(screen, (0,0,255), [x,y], 20,2)
    pygame.display.update()
    
    clock.tick(120)
