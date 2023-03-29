### 문자열(string)
### 문자열 선언
text = 'hello'
print(text)

### 문자열 연산
fruit1 = "watermelon"
fruit2 = "dragonfruit"
print(f"{fruit1} + {fruit2} = {fruit1 + fruit2}") #병합
#print(f"{fruit1} - {fruit2} = {fruit1 - fruit2}") #오류발생
print(f"{fruit1} * {2} = {fruit1 * 2}") #반복
#print(f"{fruit1} / {fruit2} = {fruit1 / fruit2}") #오류발생

##index(인덱스)
s1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s2 = 'abcdefghijklmnopqrstuvwxyz'

name = s1[19] + s2[0] + s2[4] + s2[24] + s2[4] + s2[14] + s2[13]
print(name)

## 이스케이프 코드
print('엄마가 말했다. "숙제 다 했니?"')

## 문자열 함수
hi = "Hello, world!"

print(hi.count('o')) #특정 문자 개수 반환
print("Wooooooo".count('o'))

print(hi)
print(hi.lower()) #문자열을 소문자로 변환
print(hi.upper()) #문자열을 대문자로 변환

print(hi.replace('Hello', 'Bye')) #문자 치환 (Hello -> Bye)

num = "010-2010-0803"
print(num.isalpha()) #문자가 알파벳으로만 구성 되었는지 확인
print(num.isdigit()) #문자가 숫자로만 구성 되었는지 확인

birth = "2010/08/03"
births = birth.split('/')
print(birth)
print(births)

print(len(num))
print(len(birth))
print(len(births))