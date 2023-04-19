## 조건문 if
# num = int(input('숫자입력:'))

# if num > 10:
#     print(f"{num}은(는) 10보다 큽니다.")
# elif:
#     print(f"{num}은(는) 10보다 작습니다")
# else: # 예외 처리
#     print(f"{num}은(는) 10과 같습니다")


# ## 삼항연산자
# ## <조건 식이 참일 경우 결과> if <조건 식> else <조건 식이 false일 경우 결과>
# num = int(input('숫자 입력 :'))

# # if num % 2 == 0: print('짝수')
# # else: print('홀수')

# print('짝수') if num%2 == 0 else print('홀수')

## 중첩 if
# num = int(input('숫자 입력:'))

# if num >= 10:
#     print('10 이상')
#     print('짝수')
# elif num >= 10 and num%2 != 0:
#     print('10 이상')
#     print('홀수')
# elif num < 10 and num%2 == 0: and num != 0:
#     print('10 미만')
#     print('짝수')
# elif num > 10 and num%2 != 0:
#     print('10 미만')
#     print('홀수')
# else: print('제로입니다')

## if와 멤버십 연산자 in
# elite = ['민정','태연','동건']
# st = input('학생 이름: ')

# if st in elite:
#     print(f'{st}은(는) 우등생 입니다.')
# else:
#     print(f'{st}학생 좀 더 노력하세요.')


### 연습
##1. 정수 2개를 입력 받아서 큰 수와 작은 수를 차례로 출력하는 프로그램을 작성하시오.
# num1 = int(input('숫자 1: '))
# num2 = int(input('숫자 2: '))

# if num1 > num2:
#     print(num1, num2)
# elif num2 > num1
#     print(num2, num1)
# else:
#     print(num1,'=',num2)

## 성적 출력 프로그램
## 90~100: A, 80~89: B, 70~79: C, 나머지는 F 출력
score = int(input("점수 입력: "))

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
else:
    print("F")
    