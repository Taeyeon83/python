### 1
# num1 = input("문구 입력: ")
# num2 = int(input("숫자 입력: "))

# print(num1, end="")
# print(num2)

## 또는

# print(num1, num2, sep='')

# print(f"{num1}{num2}")

### 2
# GCCD = "과천코딩2023"

# print(GCCD[2:6])
# print(GCCD[-6:-2])

### 4
# num1 = int(input("숫자 입력: "))
# num2 = int(input("숫자 입력: "))

# print(f"{num1}+{num2}={num1+num2}")
# print(f"{num1}-{num2}={num1-num2}")
# print(f"{num1}x{num2}={num1*num2}")
# print(f"{num1}/{num2}={num1/num2:.2f}")

### 5
# num = int(input("숫자 입력: "))

# if num%2==0: print("even")
# elif num%!==0: print("odd")
# else: print("zero")

### 6
# num = int(input("숫자 입력: "))

# for yak in range(1, num+1):
#     if num%yak==0: print(yak, end=" ")

### 7
# num = int(input("숫자 입력: "))
# cnt = 0

# for yak in range(1, num+1):
#     if num%yak==0: cnt += 1

# if cnt == 2: print('True')
# else: print('False')

### 8

### 9
# num = int(input("숫자 입력: "))
# total = 0

# for i in range(1, num+1):
#     total += i

# print(total)

### 10
# num  = int(input("숫자 입력: "))

# for i in range(1, num+1):
#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         print('x', end=' ')
#     if i % 10 == 3 or i // 10 == 6 or i // 10 == 9:
#         print('x', end=' ')
         
#     else:
#         print(i, end=" ")

### 11
# for line in range(5):
#     for n in range(1, 6):
#         print(n+line, end=" ")
#     print()

### 12
num = int(input("숫자 입력: "))

for i in range(num):
    print(' '*i+'*'*((num*2-1)-(2*i)))
for s in range(2, num+1):
    print(' '*((num*2-3)-s)+'*'*(s*2-1))
