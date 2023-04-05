### range() 함수
n = range(1, 11, 2)
n = list(n)
print(n)

n = list(range(1, 11, 2))
print(n)

### zip
l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(l1 + l2)
print(list(zip(l1, l2)))

t1 = (4, 5, 6)
print(list(zip(l1, l2)))

### 중첩 리스트(튜플)
weapon = ['맨 손','막대기','창','도끼','검']
lv = [1, 2, 3, 4, 5]
armor = ['장갑','방패','전투화','투구','갑옷']

item = [lv, weapon, armor]
print(item)

my_item = [item[0][0], item[1][0], item[2][0]]
print(my_item)

my_item = [item[0][1], item[1][1], item[2][1]]
print(my_item)

my_item = [item[0][2], item[1][2], item[2][2]]
print(my_item)

### numpy 설치
### 터미널 창에, pop install numpy 입력

### numpy 불러오기
import numpy as np

a = [1, 2, 3, 4, 5]
print(a, type(a))
b = np.array(a)
print(b, type(b))
print(b[2])

### 두 배열의 원소들의 연산
n1 = np.array([1, 2, 3])
n2 = np.array([4, 5, 6])

print(np.add(n1, n2))
print(np.subtract(n1, n2))
print(np.multiply(n1, n2))
print(np.divide(n1, n2))

### 2차원 배열
import numpy as np

# arr = np.array
# ([[1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11. 12, 13, 14, 15],  
#     [16, 17, 18, 19, 60],
#     [21, 22, 24, 25, 26],])
    
# print(arr)
# print(arr3[0][1])
# print([3],[0])
# print(arr.shape)
# arr1 = range(1, 100+1, 2)
# print(np.array(arr1))

# ar2 = range(2, 100+2, 2) 
# print(np.array(arr2))

### 다차원배열로 만들기
# arr1 = range(1, 100-1)
# arr1 = np.array(arr1)
# print(arr1)
# print(arr1.reshape(10, 10))

# ### 1~100까지 짝수 생성
# arr2 = range(2, 100+1, 2)
# # print(np.array(arr2))
# arr2 = np.array(arr2)
# print(arr2.reshape(5, 10))
# print(arr2.reshape(10, 5))

### quiz
## 120까지의 3의 배수 (3, 6, 9...120)로 이루어진 배열을 
## (8, 5)의 크기의 2차원 array로 만드시오.

arr1 = range(3, 120+1, 3)
arr1 = np.array(arr1)
print(arr1.reshape(8, 5))