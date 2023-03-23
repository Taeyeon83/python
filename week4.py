### 리스트(list)
### 리스트 생성
score= [90, 100, 80, 100, 60]
print(score, type(score))

## 리스트 수정
score[2] = 70
print(score)

## 리스트 추가
score.append(95) # 리스트 마지막에 추가
print(score)
score.insert(3, 100) # 원하는 인덱스 위치에 추가
print(score)

## 리스트 삭제
score.pop() # 리스트 맨 마지막 값 삭제
print(score)
score.remove(100) # 원하는 값 삭제 (중복은 가장 앞에서부터)
print(score)

print(max(score)) # 리스트에 있는 값 중 최댓값 전환
print(min(score)) # 최소값
print(len(score)) # 리스트 길이 (개수)
print(sum(score)) # 총합

## 평균 구하기
print(f"평균 : {sum(score)/5}점")
print(f"평균 : {sum(score)/len(score)}점")

print(score.index(70)) # 해당 값의 인덱스 반환
print(score.count(100)) # 해당 값의 개수 반환

## 정렬
print(score)
score.reverse() # 역순으로 정렬
print(score)

score.sort() # 오름차 순 정렬
print(score)

score.sort(reverse=True) # 내림차 순 정렬
print(score)
