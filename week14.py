### 소수 판별

# num = int(input("숫자 입력: "))
# factor = 0

# for i in range(1, num+1):
#     if num % i == 0: factor += 1

# if factor > 2: print("소수")
# else: print("소수가 아니다.")        

### 함수
## 함수의 종류
##1. 매개변수와 변환값(리턴) 모두 없는 경우
# def nothing():
#     print("비어있지롱")

# nothing()

##2. 매개변수만 있는 경우
# def mul_table():
    
# for i in range(1, 10):
#     print(f"{num} x {i} = {num*i}")

# num = int(input("숫자 입력: "))

# mul_table(num)

##3. 반환값(리턴)만 있는 경우
# def hello():
#     return "만나서 반가워 하하"

# print(hello())

##4. 매개변수와 반환값(리턴)이 모두 있는 경우
# def mul_table(num):
#     for i in range(1, 10):
#         print(f"{num} x {i} = {num*i}")
#     return print(f"{num}단 끝")

# n = int(input("숫자 입력: "))
# mul_table(n)

## 명함 만들기
# cnt = 0 #지역변수
# def namecard(*arg):
#     global cnt #전역변수
#     print("=====================================")
#     for i in arg:
#         print(i)
#     print("=====================================")
#     cnt += 1
#     return cnt

# nc = {"이름":"태연","학교":"과천중","연락처":"010-0000-1111"}
# namecard("태연", "과천중", "010-2010-0803")
# namecard("민정", "문원중", "010-2010-1216")
# print(namecard("태연", "과천중", "010-2010-0803"))
# namecard("jake", "과천코딩", "010-0000-0000", "jworks@gmail.com")

##넓이 구하는 함수
## 삼각형: 밑변 x 높이 x 1/2
# def smsm(b, h):
#     area = b * h * 1/2
#     return area

# print(smsm)

# base = 1
# height = int(input("숫자 입력: "))
# print(smsm(base, height))

##사각형 : 밑변 x 높이
# def fgh(b, h):
#     area = b * h 
#     return area
# print(fgh)

# base = int(input("가로 입력: "))
# height = int(input("세로 입력: "))
# print(fgh(base, height))

##원 : 반지름 x 반지름 x 3.14
def one(b):
    area = b * b * 3.14
    return area
print(one)

base = int(input("숫자 입력: "))

print(one(base))