# greeting이라는 변수에 '안녕하세요'라는 문자를 할당한다.
greeting = '안녕하세요'

#주석처리는 ctrl + /
# print(greeting)
# print(greeting)
# print(greeting)
# print(greeting)
# print(greeting)


count=0

#while은 종료조건이 중요(계속 반복된다면 ctrl+c눌러서 종료가능)
while count < 4:
    print(greeting)
    count = count + 1 #저장하는 것이 중요

# 0부터 n-1까지의 숫자들을 만들어주는 range()
# range(5) -> 0,1,2,3,4
for i in range(5):
    print(greeting)
