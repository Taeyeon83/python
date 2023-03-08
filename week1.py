## 주석
## ㅆㅃ살려줘요으앙야에에엥ㅇ어렁ㅇ
"""
이것도 
여러 줄
주석임
"""
'''
응
애
'''
print("hiii")
print(type("근데왜저를보고말하세요웅웅어어얼알앵랴애너랴ㅐㅇ")) #str : string (문자열!)
print(1+1) #int : integer(정수) ; ... -3, -2, -1, 0, 1, 2,..
print(type(3.141592)) #float : 실수(소수점이 있는 숫자)

### 연산자
print(1+1)
print(10-2)
print(1*2)
print(10/2)  #나눗셈은 자료형이 float(실수)로 바뀜
print(10//3) #나눗셈 몫만 구하는 연산
print(10%3)
print(2**3)
### 변수
a = 10 # = : 대입연산자

print(a)

name = "김태연"
age = 100444
height = 200000.0

print(name)
print(age)
print(height) 

### 변수의 연산
age = age + 1
age += 1 #복합 연산자

### 비교 연산자
# print(age==14)

a=10
b=20


print(a==b) #false
print(a != b) #true
print(a>b) #false
print(a<b) #true
print(a >= b) #false
print(a <= b) #true


### 논리 연산자
a = 10
b = 20

print(a<b and a==10) #T T => true
print(a<b and a==20) #T F => false
print(a>b and a==20) #F F => false

print(a<b or a==10) #T T => true
print(a<b or a==20) #T F => true
print(a>b or a==20) #F F => false

print(not a<b) #T => false
print(not a>b) #F => true
print(not a==10) #T => false

