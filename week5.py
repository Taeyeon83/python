# ### week4 복습
# ### 문자열
# ## Q1. 사용자에게 오늘의 날짜를 입력 받아서 (형식, yyyy/mm/dd)
# # "오늘은 -월 -일 입니다." 출력

# yyyy = 2023
# mm = 3
# dd = 29

# print(f"오늘은 {yyyy}년 {mm}월 {dd}일 입니다.")

# # 인덱스
# date = 2023/3/29
# print(f"오늘은 {date[5]}월 {date[-2:]}일 입니다.")

# # 함수(메소드)
# date = date.split('/')
# # print(date)
# print(f"오늘은 {date[1]}월 {date[2]}일 입니다.")

# Q2. 전화번호를 입력 받아서 (형식, 010-1111-2222)
# 공백 없이 붙여서 출력

number = "010-7122-6331"
number = number.split('-')
print(f"{number[0]}{number[1]}{number[2]}")

number = "010-7122-6331"
number = number.replace('-', '')
print(number)

### list 추가 in / join
# 멤버십 연산자 in
even = [2, 4, 6, 8, 10, 12]
print(3 in even)

# join 
friends = ['태연','하진','민정','채민','동진']
print(' '.join(friends))

# 인덱스 슬라이딩
print(friends[::-1])

friends.reverse()
print(friends)

### 튜플
tu = (1, 2, 3, 4, 5)
print(tu, type(tu))

print(tu[2])

### 리스트 vs 튜플
## 리스트
l1 = [1, 2, 3]
l2 = l1[:]
l2[1] = 4
# l2[1] = 4
print(l1)
print(l2)
print(l1 == l2) # 값이 같은지
print(l1 is l2) #대상(객체)이 같은지

## 튜플
t1 = (1, 2, 3)
t2 = t1[:]
# t2[1] = 4
# t2[1] = 4
print(t1)
print(t2)
print(t1 == t2) # 값이 같은지
print(t1 is t2) #대상(객체)이 같은지

### 추가 함수
## .endswith() / .startswith()
## lstrip() / rstrip() / strip()

f_name = "study.txt"
# print(f_name.endswith('txt','doc','hwp','pages'))

f_name = "2023_note.hwp"
print(f_name.startswith('2023'))

## lstrip() / rstrip() / strip()
data = " 삼성전자 " 
print(data.lstrip())