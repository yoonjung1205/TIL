import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
response = requests.get(url).text

data = BeautifulSoup(response,'html.parser')

dollar = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
result = dollar.text

print(f'현재 원/달러의 환율은 {result} 입니다.')