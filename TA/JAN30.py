# 1225 이상한 곱셈
a,b = input().split()
print(sum(map(int,a))*sum(map(int,b)))

# 2438 별찍기

print(*['*'*i for i in range(1,int(input())+1)],sep='\n')

# 2739 구구단
n = int(input())
for i in range(1,10):
    print(f'{n} * {i} = {n*i}')

# 2953 나는 요리사다
n = [sum(list(map(int,input().split()))) for i in range(5)]
print(n.index(max(n))+1,max(n))

# 2669 직사각형 네개의 합집합의 면적 구하기
lst = [[0]*100 for i in range(100)]
cnt = 0
for i in range(4):
    a,b,c,d = list(map(int,input().split()))
    for x in range(a,c):
        for y in range(b,d):
            lst[x][y] = 1
for i in lst:
    cnt += i.count(1)
print(cnt)
    