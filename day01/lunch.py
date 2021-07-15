#무작위로 뽑기위해서 random 사용, import를 사용해야한다
import random


#lunch라고 하는 변수에 점심메뉴 3가지 담자


lunch = ['짜장','돈가스','냉면']

print(lunch)
print(lunch[2])

menu = random.choice(lunch)
print(menu)