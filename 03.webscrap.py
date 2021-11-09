import requests
import re
from bs4 import BeautifulSoup

# 날씨
r = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=날씨")


if r.status_code == 200:
    parse = BeautifulSoup(r.text, 'html.parser')
    regex = re.compile('[0-9]+')
    print('온도: ', regex.search(parse.find_all('div', class_='temperature_text')[0].text).group())
    info = parse.find_all('div', class_='temperature_info')[0].text
    regex = re.compile('강수확률 (\\d+)%')
    print('강수확률: ', regex.search(info).groups()[0])
    regex = re.compile('습도 (\\d+)%')
    print('습도: ', regex.search(info).groups()[0])
    regex = re.compile('바람.+ (\\d+)m/s')
    print('바람: ', regex.search(info).groups()[0])

    
