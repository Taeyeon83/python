# ### 딕셔너리
# d =  dict()
# print(d, type(d))

# d = {'이름':'홍길동','학교':'과천중','학년':1}
# print(d, type(d))

# ## 딕셔너리 값 가져오기
# print(d['학교'])

# ## 딕셔너리 추가
# d['반'] = 9
# print(d)

# ## 딕셔너리 수정
# d['학교'] = '문원중'
# print(d)

# ## 딕셔너리 삭제
# del d['반']
# print(d)

## 딕셔너리 함수
fruits = {'사과':1200, '귤':500, '망고':2000}

# key 만 묶어서 변환
keys = list(fruits.keys())
print(keys[0], type(keys))

# value 들만 묶어서 변환
val = fruits.values()
print(val, type(val))

# key와 value 쌍으로 묶어서 반환
item = list(fruits.items())
print(item, type(item))

# key에 해당하는 값 반환
# print(fruits['바나나'])  # 딕셔너리에 키가 없어서 오류 발생
print(fruits.get('바나나')) # key가 없을 경우 none 반환

# 딕셔너리 정보 업데이트
fruits.update({'사과': 800, '바나나': 1500, '수박': 8000})
print(fruits)

# 딕셔너리 초기화
fruits.clear()
print(fruits)

