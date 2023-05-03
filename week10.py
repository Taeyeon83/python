### 반복문 for
## for x 리스트

# student = ['태연', '민정', '길동']
# cnt = 1
# for s in student:
#     print(cnt, s)
#     cnt += 1

## for x 튜플
# snack = ('빼빼로', '맛동산', '새우깡', '양파링')
# cnt = 1

# for s in snack:
#     print(cnt, s)
#     cnt += 1

# for s in snack:
#     print(s, end=' ')

## for x 딕셔너리
# score = {'국어':100, '영어':100, '수학':80, '역사': 90}

# for s in score: 
#     print(s, ':', score[s])

# ## for x range()
# for i in range(10): #(횟수) #0~9까지 생성
#     print(i)

# for i in range(1, 11): #(시작값, 끝값+1)
#     print(i)

# for i in range(1, 101, 2): # -> (시작값, 끝값 + 1, 간격)
#     print(i)

### Q1. 입력받은 숫자만큼 'python'을 출력하세요.

# num = int(input("숫자 입력: "))

# for i in range(num):
#     print("python")

### Q2. 1부터 입력받은 숫자 중에서 짝수만 차례대로 한 줄로 출력하세요.

# num = int(input("숫자 입력: "))

# for i in range(2, num+1, 2):
#     print(i, end=' ')

### Q3. 입력받은 숫자의 구구단 출력

num = int(input("숫자 입력: "))

for i in range(1, 10):
    print(f"{num}x{i}={num*i}")