import pygame
import sys

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
    pygame.draw.circle(screen, (0,0,255), [x,y], 20,2)
    pygame.display.update()
    
    clock.tick(120)
