### for x 조건문 if

# star = int(input('숫자 입력: '))

# for line in range(1, star*2):
#     if line <= star:
#         print('*'*line)
#     else:
#         print('*'*(star*2-line))

# num = int(input('숫자 입력: '))
# for line in range(1, num+1):
#     for i in range(1, num+1):
#       print(line, end=' ')
#     print()

## 함수 / 클래스 / 모듈 /  라이브러리

def hello():
    print("hello!")

hello()  # 함수의 호출
hello() 

def ggd(num):   # 매개변수: num

    for i in range(1, 10):
        print(f"{num} x {i} = {num*i}")

ggd(9)  # 인자값
ggd(6)
ggd(83)