import requests
import re
from bs4 import BeautifulSoup
import pygame, sys
import math
import random
import math
import threading
import time


temperature = 0
precipitation = 0
humidity = 0
wind = 1
# 날씨
def get_data():
    while True:
        global temperature, precipitation, humidity, wind
        r = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=날씨")
    
        if r.status_code == 200:
            parse = BeautifulSoup(r.text, 'html.parser')
            regex = re.compile('[0-9]+')
            temperature = int(regex.search(parse.find_all('div', class_='temperature_text')[0].text).group())
            print('온도: ', temperature)
            info = parse.find_all('div', class_='temperature_info')[0].text
            regex = re.compile('강수확률 (\\d+)%')
            precipitation = int(regex.search(info).groups()[0])
            print('강수확률: ', precipitation)
            regex = re.compile('습도 (\\d+)%')
            humidity = int(regex.search(info).groups()[0])
            print('습도: ', humidity)
            regex = re.compile('바람.+ (\\d+)m/s')
            wind = int(regex.search(info).groups()[0])
            print('바람: ', wind)
        time.sleep(10)


thd = threading.Thread(target=get_data)
thd.start()



pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

center_x = screen.get_width() * 0.5
center_y = screen.get_height() * 0.5

class Particle:
    def __init__(self):
        global wind
        self.x = screen.get_width() * 0.5
        self.y = screen.get_height() * 0.5
        self.size = 10
        r = random.randrange(100,255)
        self.color = (r,r,r)
        self.x_dir = random.randrange(1,wind*4) * random.choice([-1,1])
        self.y_dir = random.randrange(1,wind*4) * random.choice([-1,1])
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
    t = pygame.time.get_ticks() * 0.005
    center_x = math.sin(t) * 200 + screen.get_width() * 0.5
    center_y = math.cos(t) * abs(math.sin(t*0.2)) * precipitation + screen.get_height() * 0.5
    for p in particles:
        p.draw()
    pygame.display.update()
    
    clock.tick(120)
