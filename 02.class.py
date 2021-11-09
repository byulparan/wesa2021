import pygame, sys
import math
import random
import math


pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

center_x = screen.get_width() * 0.5
center_y = screen.get_height() * 0.5

class Particle:
    def __init__(self):
        self.x = screen.get_width() * 0.5
        self.y = screen.get_height() * 0.5
        self.size = 10
        r = random.randrange(100,255)
        self.color = (r,r,r)
        self.x_dir = random.randrange(1,4) * random.choice([-1,1])
        self.y_dir = random.randrange(1,4) * random.choice([-1,1])
    def draw(self):
        self.x += self.x_dir
        self.y += self.y_dir
        self.size -= 0.1
        
        pygame.draw.circle(screen, self.color, [self.x,self.y], self.size)
        if self.x < 0 or self.x > screen.get_width() or self.y < 0 or self.y > screen.get_height() or self.size < 0:
            self.x = center_x
            self.y = center_y
            self.x_dir = random.randrange(1,4) * random.choice([-1,1])
            self.y_dir = random.randrange(1,4) * random.choice([-1,1])
            self.size = 10



particles = [Particle() for _ in range(1000)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((30, 30, 30))
    time = pygame.time.get_ticks() * 0.005
    center_x = math.sin(time) * 200 + screen.get_width() * 0.5
    center_y = math.cos(time) * abs(math.sin(time*0.2)) * 200 + screen.get_height() * 0.5
    for p in particles:
        p.draw()
    pygame.display.update()
    
    clock.tick(120)
