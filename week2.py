print(100+53)
print(2**10)
'''
응애!
'''
name = 'taeyeon'
num = 10909

print(name, num)
# print(name, num)
# print(name + num) #서로 다른 자료형끼리 + 연산을 하면 오류가 난다

# 포맷팅 (formatting)
# name = '김태연'
# grade = 1
# clas = 9

# print("1학년 9반 김태연입니다.")
# print("%d학년 %d반 %s입니다."%(grade, clas, name)) # 포맷기호
# print("{}학년 {}반 {}입니다.".format(grade, clas, name)) # 포맷함수
# print(f"{grade}학년 {clas}반 {name}입니다.") # f-string

# name = "김태연"
# age = 14
# height = 167.8

# print("이름: 김태연, 나이: 14, 키: 167.8")
# print("이름: %s, 나이: %d살, 키: %.3fcm" %(name, age, height))
# print("이름: {}, 나이: {}살, 키: {}cm". format(name, age, height))
# print(f"이름: {name}, 나이: {age}살, 키: {height}cm")

### input() 함수 : 입력
num = input("숫자를 입력하세요.: ")
print(f"입력하신 숫자는 {num} 입니다.")
name = input("이름을 입력하세요.")
print(f"{name}님, 환영합니다")
