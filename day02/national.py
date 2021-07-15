import requests

name = 'alice'
url = f'https://api.nationalize.io/?name={name}'

response = requests.get(url).json()

#print(response)
national = response['country'][0]
country = national['country_id']
percentage = national['probability']*100

#round로 반올림 가능
#round(float, 반올림하고자 하는 위치)
print(f'{name} 의 국가는 {round(percentage,2)}% 확률로 {country} 입니다.')