import requests
from bs4 import BeautifulSoup

service_key = ''

params = {
    'stationName' : '동대문구',
    'dataTerm' : 'month',
    'pageNo' : '1',
    'numOfRows' : '1',
    'returnType' : 'xml',
    'serviceKey' : service_key
}

req = requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty', params)
resp = BeautifulSoup(req.text, 'html.parser')


for item in resp.find_all('item'):
    print('---------------------------------------------------------')
    print('데이터일자: ', item.find('datatime').text)
    print('so2: ', item.find('so2value').text)
    print('khai: ', item.find('khaivalue').text)
    print('pm10: ', item.find('pm10value').text)
    print('co: ', item.find('covalue').text)
    print('o3: ', item.find('o3value').text)
    print('no2: ', item.find('no2value').text)
    
    

    
