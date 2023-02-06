# 10817 세 수
print(sorted(list(map(int,input().split())))[1])

# 20001 고무오리 디버깅
from collections import deque

start = input()
question = deque()

while 1:
    n = input()
    if n == '문제':
        question.append(n)
    elif n == '고무오리 디버깅 끝':
        if len(question) > 0:
            print('힝구')
            break
        else:
            print('고무오리야 사랑해')
            break
    else:
        if len(question) == 0:
            question.append(n)
            question.append(n)
        else:
            question.popleft()

# 1269 대칭 차집합

n = input()
a = set(map(int,input().split()))
b = set(map(int,input().split()))
print(len(a ^ b))

# 3052 나머지

print(len(set([int(input()) % 42 for _ in range(10)])))

# 1181 단어 정렬

# 1안
n = sorted(set([input() for _ in range(int(input()))]))
for x in range(51):
    for y in n:
        if len(y) == x:
            print(y)

# 2안
n = sorted(set([input() for _ in range(int(input()))]))
print(*sorted(n,key=len),sep='\n')

# 11286 절댓값 힙

import heapq
import sys

input = sys.stdin.readline
heap = []

for _ in range(int(input())):
    num = int(input())
    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(num), num))

