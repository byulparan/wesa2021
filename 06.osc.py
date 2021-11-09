import random
import time
import requests
import re
from pythonosc import udp_client
from bs4 import BeautifulSoup


# 127.0.0.1(IP) - 8080(port) 로 데이터를 send 하겠다.
client = udp_client.SimpleUDPClient('127.0.0.1', 8080)


while True:
    r = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=날씨")
    
    if r.status_code == 200:
        parse = BeautifulSoup(r.text, 'html.parser')
        regex = re.compile('[0-9]+')
        temperature = int(regex.search(parse.find_all('div', class_='temperature_text')[0].text).group())
        client.send_message('/temperature', temperature)
        info = parse.find_all('div', class_='temperature_info')[0].text
        regex = re.compile('강수확률 (\\d+)%')
        precipitation = int(regex.search(info).groups()[0])
        client.send_message('/precipitation', precipitation)
        regex = re.compile('습도 (\\d+)%')
        humidity = int(regex.search(info).groups()[0])
        client.send_message('/humidity', humidity)
        regex = re.compile('바람.+ (\\d+)m/s')
        wind = int(regex.search(info).groups()[0])
        client.send_message('/wind', wind)
    time.sleep(2)



    



