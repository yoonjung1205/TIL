# Flask 불러온다.
from flask import Flask, render_template, request
import requests


TOKEN = '1860467196:AAFooWV_16Z-gUwynqLNq4dsIhkWt2Vm1Xk'
#요청 통합 url 변수에 담기
url = f'https://api.telegram.org/bot{TOKEN}'


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#flask로 어떤 문서를 응답할때, return에 작성하는 것이 아니라,
#특정 문서 자체를 불러와서 응답해줄 수 있다.
# flask가 가지고 있는 함수 render_templete 시용

@app.route('/ssafy')
def ssafy():
    # ssaft.html을 rendering 한다.
    return render_template('ssafy.html')

#write함수 send
@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    #사용자가 요청보낸 정보 확인할 수 있는 request 불러온다.
    #print(request)
    #print(dir(request))
    message = request.args.get('message')

    #텔레그램 챗봇 api url 필요
    #내 챗봇 토큰 필요
    TOKEN = '1860467196:AAFooWV_16Z-gUwynqLNq4dsIhkWt2Vm1Xk'
    #요청 통합 url 변수에 담기
    url = f'https://api.telegram.org/bot{TOKEN}'

    #메세지 보낼 사람 chat_id
    chat_id = 1837876799
    send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={message}'
    #파이썬으로 요청보내는 requests 필요
    requests.get(send_message_url)
    
    return render_template('send.html')

# POST 방식의 요청만 받겠다.
@app.route('/telegram', methods=['POST'])
def telegram():
    # 요청정보는 request에 들어있다.
    response = request.get_json()
    #print(response)
    
    # response에 chat_id, text 들어있고
    # text에 들어있는 값이 무엇인지에 따라 보낼메세지 바꿔준다.
    # 조건문 넣어주면 될 것 같다.
    # 사용자가 챗봇한테 보낸 메세지 똑같이 돌려보내주는 코드

    chat_id = response['message']['from']['id']
    text = response['message']['text']


    #누구야 -> ~~님의 챗봇입니다. 추출
    if text == '누구야':
        text = '저는 정윤정님의 챗봇입니다.'
        
    elif text == '미세먼지':
        servicekey = 'F%2FG7Q2MaQZRgQ8uRoi93bGC0PrdDdGmFTpwTuNXkUmouTrshQCZPoiHJxrCqb%2B6LVoaFyFN8vlExCPlNTXf37w%3D%3D'
        dust_url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={servicekey}&returnType=json&numOfRows=100&pageNo=1&sidoName=서울&ver=1.0'

        response2 = requests.get(dust_url).json()
        #print(response['response']['body']['items'][5])

        sido_name = response2['response']['body']['items'][5]['sidoName']
        station_name = response2['response']['body']['items'][5]['stationName']
        dust = response2['response']['body']['items'][5]['pm10Value']

        text = f'{sido_name}시 {station_name}의 미세먼지 농도는 {dust}입니다.'
        

    send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(send_message_url)
    # 응답은 본문과 status_code 200을 같이 보내준다.
    return '',200









if __name__ == '__main__':
    app.run(debug=True)