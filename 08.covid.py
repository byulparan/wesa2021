import requests
from bs4 import BeautifulSoup

service_key = ''

params = {
    'pageNo' : '1',
    'numOfRows' : '10',
    'startCreateDt' : '20211109',
    'endCreateDt' : '20211109',
    'serviceKey' : service_key
}

req = requests.get('http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson', params)

resp = BeautifulSoup(req.text, 'html.parser')

for item in resp.find_all('item'):
    print('---------------------------------------------------------')
    print('데이터일자: ', item.find('statedt').text)
    print('데이터시간: ', item.find('statetime').text)
    print('확진자: ', item.find('decidecnt').text)
    print('사망자: ', item.find('deathcnt').text)
    print('격리해제: ', item.find('clearcnt').text)
    print('치료중: ', item.find('carecnt').text)

