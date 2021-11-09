import requests
import re
from bs4 import BeautifulSoup
import pygame, sys
import math
import random
import math
import threading
import time


# 주식
r = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=주식')

down = True
value = 0.0

def get_data():
    global down, value
    while True:
        if r.status_code == 200:
            parse = BeautifulSoup(r.text, 'html.parser')
            info = parse.find_all('span', class_='spt_con dw')
            if len(info) == 0:
                info = parse.find_all('span', class_='spt_con up')
            info = info[0]
            down = info.find_all('span', class_='ico')[0].text == "하락"
            value = float(info.find_all('em')[0].text)
            print('get data....', info.find_all('span', class_='ico')[0].text, value)
        time.sleep(10)

thd = threading.Thread(target=get_data)
thd.start()

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

class Particle:
    def __init__(self):
        self.x = random.randrange(0, screen.get_width())
        self.y = random.randrange(0, screen.get_height())
        self.size = 10
        self.color = (0,0,255) if down else (255,0,0)
        self.y_dir = value * 0.1 * (1 if down else -1)
    def draw(self):
        self.x += random.randrange(-2,3)
        self.y += self.y_dir
        
        pygame.draw.circle(screen, self.color, [self.x ,self.y], self.size)
        if self.x < 0 or self.x > screen.get_width() or self.y < 0 or self.y > screen.get_height() or self.size < 0:
            self.x = random.randrange(0,screen.get_width())
            self.y = 0 if down else screen.get_height()
            self.y_dir =  value * 0.1 * (1 if down else -1)
            self.size = 10



particles = [Particle() for _ in range(10)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((30, 30, 30))
    for p in particles:
        p.draw()
    pygame.display.update()
    
    clock.tick(120)


    

