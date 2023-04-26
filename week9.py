### 반복문 while

### 열 번 찍어 안 넘어가는 나무 없다!
# count = 0

# while count < 10:
#     count += 1
#     print(f"나무를 {count}번 찍었습니다.")

# print("나무가 넘어갑니다!")

### 로그인 프로그램
# user = {'ty83':'1234','mjspmk':'5678','jake':'2022'}
# value = True

# while value:
#      id = input("아이디 입력: ")
#      pw = input("비밀번호 입력: ")
#      if id in user:
#           if pw == user[id]:
#                print("환영합니다.")
#                value = False
#           else:
#                print("다시 입력해 주세요.")
#      else:
#          print("아이디를 확인해 주세요.")


# value = True

# while value:
#     print("무한 반복")
#     value = False
# print("종료")

### 별 찍기
# star = 0
# while True:
#     star += 1
#     print('*'*star)
#     if star >= 5:
#         break

### Practice 
#1. 정수를 입력 받아 1부터 입력 받은 정수까지 차례대로 출력하는 프로그램을 작성하시오.
# num = int(input("숫자 입력: "))
# hp = 0

# # while hp < num:
# #     hp += 1
# #     print(hp)

# while True: 
#     hp += 1
#     print(hp)
#     if hp == num:
#         break

#2. 정수를 입력 받다가 0이 입력되면 그 때까지 입력 받은 홀수의 개수와 짝수의 개수를 출력하시오.
even = 0
odd = 0

while True:
    num = int(input("숫자 입력: "))
    print(num)
    if num == 0:
        break
    elif num % 2 == 0:
        even += 1
    elif num % 2 != 0:
        odd += 1
    else:
        print("잘못 입력하셨습니다.")
print(f"홀수: {odd}개, 짝수: {even}개")

### Homework #######
##1. while 문을 이용하여 1부터 입력 받은 정수까지의 합을 구하여 출력하는 프로그램을 작성하시오.
##2. 점수를 입력받아 80점 이상이면 합격메시지를 그렇지 않으면 불합격 메시지를 출력하는 작업을 반복하다가 0~100점 이외의 점수가 입력되면 종료하는 프로그램을 작성하시오.
##3. 점수를 계속 입력을 받다가 0이 입력되면 0을 제외하고 이전에 입력된 자료의 수와 합계, 평균을 출력하는 프로그램을 작성하시오. (평균은 반올림하여 소수 둘째자리까지 출력한다.)
