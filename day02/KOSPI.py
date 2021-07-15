import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text #-> 응답 받은 문서를 문자열로 반환한다.
#print(response)

#bs4를 통해 파이썬이 읽을 수 있는 데이터 형으로 변경
#변경하는 문서가 어떤 형태인지도 같이 작성 해줘야 한다.
#html.parser -> html 문서를 파이썬에서 읽을 수 있도록 만들어 준다.
data = BeautifulSoup(response, 'html.parser')
#print(data)

kospi = data.select_one('#KOSPI_now')
#print(kospi)
result = kospi.text

print(f'현재의 코스피 지수는 {result} 입니다.')