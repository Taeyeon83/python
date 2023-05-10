### 별 삼각형 출력
# star = int(input("별 개수: "))

# for s in range(1, star+1):
#     print('*'*s)

### 역삼각형 출력
# star = int(input("별 개수: "))

# for i in range(1, star+1):
#     for s in range(star, 1, -1):
#         print(' ', end=' ')
#     print('*'*i)

### 구구단 x 중첩포문 :
# for num in range(2, 10):
#     for i in range(1, 10): 
#         print(f"{num}x{i}={num*i}")
#     print()    

## Q1. 1부터 입력한 숫자까지 출력
# num = int(input("숫자 입력: "))

# for i in range(1, num+1):
#     print(i, end=' ')

## Q2. 시작하는 수와 끝나는 수 입력 받아서 두 수 사이의 숫자 출력
# num1 = int(input("숫자 입력: "))
# num2 = int(input("숫자 입력: "))

# for i in range(num1, num2+1):
#     print(i)

### 두 개의 숫자 한 번에 입력받기
num = input('두 개의 숫자 입력: ')
num = num.split()
# num[0] = int(num[0])
# num[1] = int(num[1])
num = [int(i) for i in num]
print(num)

