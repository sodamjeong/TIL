# 10769 행복한지 슬픈지

n = input()
happy = n.count(':-)')
sad = n.count(':-(')
if happy == sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
else:
    print('unsure')

# 2455 지능형 기차

people = []
cnt = 0
for _ in range(4):
    a,b = map(int,input().split())
    cnt -= a
    people.append(cnt)
    cnt += b
    people.append(cnt)
print(max(people))

# 2606 바이러스
n = int(input())
m = [list(map(int,input().split())) for _ in range(int(input()))]
visited = [0] * (n+1)
virus = [1]

for i in m:
    if i[0] in virus:
        visited[i[1]] = 1
        virus.append(i[1])
print(sum(visited))
# 틀림

# DFS 방법

n = int(input())
m = int(input())
com = [[] for i in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    x,y = map(int,input().split())
    com[x] += [y]
    com[y] += [x]
def dfs(start):
    visited[start] = 1
    for j in com[start]:
        if visited[j] == 0:
            dfs(j)
dfs(1)
print(sum(visited)-1)

# 4963 섬의 개수
import sys
input = sys.stdin.readline

d = [(1,1),(1,0),(0,1),(-1,-1),(-1,0),(0,-1),(1,-1),(-1,1)]

while True:
    w,h = map(int,input().split())
    if w == h == 0:
        break
    
    world = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if world[i][j]:
                stack = [(i,j)]
                world[i][j] = 0
                cnt += 1

                while stack:
                    x,y = stack.pop()
                    for a,b in d:
                        dx=x+a
                        dy=y+b
                        if h>dx>=0 and w>dy>=0 and world[dx][dy]:
                            stack.append((dx,dy))
                            world[dx][dy] = 0
    print(cnt)