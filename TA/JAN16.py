# 10039 평균 점수

# 40점 미만인 학생들은 보충학습을 듣는 조건을 수락하면 40점을 받게 된다. 
# 보충학습은 거부할 수 없기 때문에, 40점 미만인 학생들은 항상 40점을 받게 된다.
# 학생 5명의 점수가 주어졌을 때, 평균 점수를 구하는 프로그램을 작성하시오.

x =[]
for i in range(5): # 다섯번의 숫자 입력을 위한 for 문
    n = int(input())
    if n < 40: # 40점보다 낮을 경우
        n = 40 # 40점 부여
    x.append(n) # 점수 리스트 누적

print(sum(x)//5) # 점수 리스트를 sum 하고 평균 구하기

# 2안 만들어 보기

x = [int(input()) for i in range(5)]
# 5번 입력으로 리스트 생성
for index,value in enumerate(x):
# 리스트의 인덱스와 요소를 가져오는 enumerate 함수 사용
    if value < 40 : # 요소의 값이 40미만이면
        x[index] = 40 # 40으로 수정

print(sum(x)//5)
    
# # 10871 x 보다 작은 수 

# n, x = map(int,input().split())
# a = list(map(int,input().split()))
# b = []

# for i in a:
#     if i < x:
#         b.append(i)
# print(*b)

# # 2480 주사위 세개

# a, b, c = map(int,input().split())
# x = [a, b, c]
  
# if a == b == c:
#     print(10000 + 1000 * a)
# elif len(set(x)) == 2 :
#     print(1000 + (100 * sorted(x)[1]))
# else:
#     print(100 * max(x))

# # 10886 0 = not cute / 1 = cute

# n = int(input())
# x =[]

# for i in range(n):
#     a = int(input())
#     x.append(a)

# if x.count(0) > x.count(1):
#     print('Junhee is not cute!')
# else:
#     print('Junhee is cute!')

# # 2506 점수계산

# n = int(input())
# x = list(map(int,input().split()))
# n = 0
# m = []

# for i in x:
#     if i == 1:
#         n += 1
#         m.append(n)
#     else:
#         n = 0

# print(sum(m))