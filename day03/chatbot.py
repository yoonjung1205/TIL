#requsets 불러오기
import requests
from pprint import pprint
#봇 토큰 변수에 담기
TOKEN = '1860467196:AAFooWV_16Z-gUwynqLNq4dsIhkWt2Vm1Xk'
#요청 통합 url 변수에 담기
url = f'https://api.telegram.org/bot{TOKEN}'
#print(url)

#내 챗봇에 메세지 보낸사람 정보 알아내기 (getUpdates)
get_updates_url=f'{url}/getUpdates'
response = requests.get(get_updates_url).json()
    #그 사람이 보낸 메세지와, 그 사람의 chat_id 알아내기

chat_id = response['result'][0]['message']['from']['id']
text = response['result'][0]['message']['text']
print(chat_id,text)
#메세지 보낸사람에게
#그 사람이 보낸 메세지 다시 돌려보내기

send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(send_message_url)