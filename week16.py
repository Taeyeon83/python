### 모듈2 / 내장모듈 (built-in module)
## 구글 -> 파이썬 표준 라이브러리
## math 모듈
import math

# ## math.gcd(a, b) ## a와 b의 최대공약수
# print(math.gcd(11, 99))
# ## math.lcm(a, b) ## a와 b의 최소공배수
# print(math.lcm(11, 98))
# ## math.sqrt(a) ## a가 되는 제곱근 값 출력
# print(math.sqrt(4))
# ## math.log(a, b) ## 밑이 b인 a의 로그값 반환
# print(math.log(81, 9))

# from math import *

# print(gcd(12, 1024))

## random 모듈
# from random import *

# ## randint(a, b) ## a와 b를 포함한 범위에서 랜덤한 값 반환
# print(randint(1, 100))

# ## choice(s) # 배열 형식의 자료형 s에서 하나의 랜덤 값 반환
# name = ['태연', '민정', '제이크', '둘리', '도우너']
# print(choice(name))
# ## sample(s, n) # s에서 n개의 값을 반환
# print(sample(name, 3))
# ## shuffle(s) # s의 순서를 랜덤으로 섞음
# print(name)
# shuffle(name)
# print(name)

## 주사위게임
# from random import *

# print('주사위 게임!')
# for i in range(3):
#     com = randint(1, 6)
#     input("Enter 키를 눌러서 주사위를 던지세요!")
#     user = randint(1, 6)
#     if user > com: print("사람이 이겼습니다!")
#     elif user < com: print("컴퓨터가 이겼습니다!")
#     else: print("비겼습니다.")

### time 모듈
# from time import *

# ## time() : 현재 Unix timestamp를 소수로 반환
# print(time())
# ## gmtime() : GMT 기준의 struct_time 타입 데이터로 변환
# print(gmtime())
# ## localtime() : 현지 시간 struct_time 타입 데이터 변환
# print(localtime())
# ## ctime() : 현지 시간 반환
# print(ctime())
# ## sleep(sec) : 일정시간(초) 동안 프로그램 실행 지연
# sleep(10)
# print('메롱')

### 타이머 만들기
# from time import *

# set_time = int(input('원하는 시간(초) 입력: '))
# sleep(set_time)
# for i in range(set_time, 0, -1):
#     sleep(1)
#     if i <= 10:
#         print(i)
# print("따르릉~~~!")

### up & down GAME
from random import *
i = randint(1, 100)
cnt = 0

while True:
    num = int(input('숫자 입력: '))
    cnt += 1
    if num > i: print("Down")
    elif num < i: print("Up")
    else:
        print("빙고~~~~!")
        break
print(f"{cnt}번 만에 맞혔습니다!")
