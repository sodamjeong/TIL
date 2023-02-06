# 10101 삼각형 외우기

n = [int(input()) for i in range(3)] 
m = ['Equilateral','Isosceles','Scalene']
if sum(n) != 180:
    print('Error')
else:
    print(m[len(set(n))-1])

# 2720 세탁소 사장 동혁

for i in range(int(input())):
    n = int(input())
    print(n//25,n%25//10,(n%25)%10//5,n%5)

# 1453 피시방 알바

people = int(input())
seat = list(map(int,input().split()))
seats = []

for i in seat:
    if i not in seats:
        seats.append(i)
print(people-len(seats))

# 10773 제로
import sys
input = sys.stdin.readline
n = []
for i in range(int(input())):
    m  = int(input())
    if m > 0:
        n.append(m)
    else:
        n.pop()
print(sum(n))

# 2161 카드 1

from collections import deque
import sys

card = deque(range(1,int(sys.stdin.readline()) + 1))

while len(card) > 1:
    print(card.popleft(),end=" ")
    card.append(card.popleft()) # card.rotate(-1)
print(card[0])

# 9012 괄호

# 1안 카운트 
for i in range(int(input())):
    n = input()
    cnt = 0
    for x in n:
        if x == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                print('NO')
                break
    else:
        if cnt == 0:
            print('YES')
        elif cnt > 0:
            print('NO')

# 2안 스택을 사용한 방법
for i in range(int(input())):
    n = input()
    m = []
    try:
        for x in n:
            if x == '(':
                m.append(x)
            else:
                m.pop()
        if len(m) == 0:
            print('YES')
        else:
            print('NO')
    except IndexError:
        print('NO')