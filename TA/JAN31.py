# 2441 별찍기-4
n = int(input())
print(*[' '*i+'*'*(n-i) for i in range(n)],sep='\n')

# 2592 대표값
from collections import Counter
import sys
input=sys.stdin.readline
n = [int(input()) for _ in range(10)]
print(sum(n)//10)
print(Counter(n).most_common()[0][0])

# 10798 세로 읽기
n = [list(input()) for _ in range(5)]

for x in range(16):
    for y in range(5):
        try:
            print(n[y][x],end='')
        except:
            pass

# 9455 박스
for _ in range(int(input())):
    x,y = map(int,input().split())
    n = [list(input().split()) for _ in range(x)]
    new_n = [[0]*x for _ in range(y)]
    cnt = 0
    for i in range(y):
        for j in range(x):
            new_n[i][j]=n[j][y-i-1]
    for a in new_n:
        for b in range(len(a)):
            if a[b] == '1':
                cnt += a[b:].count('0')
            else:
                pass
    print(cnt)

# 1652 누울 자리를 찾아라
room = [list(input()) for _ in range(int(input()))]
n = len(room)
w = 0
h = 0
for i in room:
    cnt = 0
    for j in i:
        if j == '.':
            cnt += 1
        else:
            if cnt > 1:
                w += 1
            cnt = 0
    if cnt > 1:
        w += 1
for x in range(n):
    cnt2 = 0
    for y in range(n):
        if room[y][x] == '.':
            cnt2 += 1
        else:
            if cnt2 > 1:
                h += 1
            cnt2 = 0
    if cnt2 > 1:
        h += 1
print(w, h) 

