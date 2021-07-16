# setWebHook 요청보내야함
import requests

# token,url, ngrok url
TOKEN = '1860467196:AAFooWV_16Z-gUwynqLNq4dsIhkWt2Vm1Xk'
#요청 통합 url 변수에 담기
url = f'https://api.telegram.org/bot{TOKEN}'
#ngrok_url = 'https://6dd8b726d7f3.ngrok.io'
python_anywhere = 'https://yoonjung1205.pythonanywhere.com'
set_webhook_url = f'{url}/setWebhook?url={python_anywhere}/telegram'
# telegram이 내 ngrok telegram으로 요청을 보내고 200응답 받아감.

response = requests.get(set_webhook_url)
print(response.text)