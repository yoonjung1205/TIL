number = 3
print(type(number))


string = '문자열'
print(type(string))

boolean = True
print(type(boolean))

#형변환
string_number='58'
print(type(int(string_number)))

#f-string
name = '홍길동'
print(f'{name}입니다. 반갑습니다')

"""
리스트
"""

#리스트 선언
my_list=['java','python']
#원소 접근
print(my_list[0])
#원소 변경
my_list[0] = 'django'
print(my_list)
#리스트 길이
print(len(my_list))

"""
딕셔너리
"""
my_info = {
    'name': '정윤정',
    'age': 15
}
print(my_info)

#원소 접근
print(my_info['name'])
print(my_info.get('name'))
#print(my_info['location'])

#원소 변경
my_info['name'] = '홍길동'
print(my_info)

"""
딕셔너리 실습
"""
coin = {
    'BTC': {
        'opening_price': '44405000',
        'closing_price': '38806000',
        'min_price': '36640000',
        'max_price': '44999000',
        'prev_closing_price': '44404000',
        'fluctate_24H': '-7463000',
        'fluctate_rate_24H': '-16.13',
    },
    'ETH': {
        'opening_price': '1458000',
        'closing_price': '1229000',
        'min_price': '1100000',
        'max_price': '1490000',
        'prev_closing_price': '1458000',
        'fluctate_24H': '-275000',
        'fluctate_rate_24H': '-18.28',
    },
    'XRP': {
        'opening_price': '364.5',
        'closing_price': '311.9',
        'min_price': '284.2',
        'max_price': '372.7',
        'prev_closing_price': '364.2',
        'fluctate_24H': '-90.6',
        'fluctate_rate_24H': '-22.51',
    },
}

# 2-1. 코인의 정보에서 BTC의 최대 가격을 출력하시오.
print(coin['BTC']['max_price'])

# 2-2. BTC의 시가와(opening price) XRP의 시가를 더한 결과를 출력하시오.
print(float(coin['BTC']['opening_price'])+float(coin['XRP']['opening_price']))