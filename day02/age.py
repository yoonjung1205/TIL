import requests


name = 'alice'
url = f'https://api.agify.io/?name={name}'


#json() -> dict
response = requests.get(url).json()
print(response)

# name의 나이는 age 입니다.
name = response['name']
age = response['age']
print(f'{name}의 나이는 {age} 입니다.')