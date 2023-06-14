### 함수 만들기
# '사인' -> '안녕하세요'
# '둑도' -> '손 들어, 꼼짝 마!'
# '구친' -> '어서오세요!'

# def mytobot(msg):
#     if msg == '인사':
#         print('안녕하세요')
#     elif msg == '둑도':
#         print('손 들어, 꼼짝 마!')
#     elif msg == '구친':
#         print('어서오세요!')

# mytobot('인사')
# mytobot('둑도')
# mytobot('구친')

### 클래스 생성
# class Cal:
#     total = 0
#     def add(self, n):
#         self.total =+ n
#         return print(self.total)
    
# math = Cal()     #객체선언 #객체생성
# math.add(10)
# math.add(3)

# sc = Cal()
# sc.add(100)

### 생성자
# class Lol:
#     def __init__(self):
#         print("게임이 실행 되었습니다.")

# class Slt_crt(Lol):   # 클래스 상속
#     def __init__(self):
#         super().__init__()   # 생성자 오버로딩
#         print("캐릭터 선택")
    
# # play = Lol()
# play = Slt_crt()

### 계산기 프로그램
class Cal:
    def __init__(self):
        self.total = 0
    def add(self, n):
        self.total += n
        return print(self.total)
    def sub(self, n):
        self.total -= n
        return print(self.total)
    def mul(self, n):
        self.total *= n
        return print(self.total)
    def div(self, n):
        self.total /= n
        return print(self.total)
    
# math = Cal()
# math.add(10)
# math.sub(5)
# math.mul(7)
# math.div(7)
# math.div(0)

### 클래스 상속 연습
# class Cal_divup(Cal):
#     def __init__(self):
#         super().__init__()
#         print("나는 Cal_divup")
#     def div(self, n):
#         if n == 0: print("연산 불가")
#         else:
#             self.total /= n
#             return print(self.total)

# math = Cal_divup()
# math.add(10)
# math.sub(5)
# math.mul(7)
# math.div(0)

### 모듈 module
## 게임 플레이

# from move import *
# import move, attack

# move.up()
# move.left()

# p1 = attack.Attack()
# p1.punch()

from move import *
from attack import *

up()
left()

p1 = Attack()
p1.punch()