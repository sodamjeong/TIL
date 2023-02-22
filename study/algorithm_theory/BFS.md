# BFS

## BFS란 ?
- Breadth - First Search
BFS는 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
```큐 (FIFO)``` 자료구조를 이용한다.

<컴퓨터인터넷IT용어대사전><br/>
자료의 검색, 트리나 그래프를 탐색하는 방법.<br/> 한 노드를 시작으로 인접한 다른 노드를 재귀적으로 탐색해가고 끝까지 탐색하면 다시 위로 와서 다음을 탐색하여 검색한다.

### 동작과정

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다.
3. 2번 과정을 더이상 수행 할 수 없을 때 까지 반복.


```py
from collection import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True #현재 노드를 방문처리
    while queue: # queue 가 빌 때까지 반복
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]: # 해당 인덱스의 값이 False
                queue.append(i) # 방문하지 않은 인접한 원소들을 큐에 삽입
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9 
# 방문 여부 확인하는 1차원 리스트
bfs(graph,1,visited)

# 1부터 시작
# out = 1 2 3 8 7 4 5 6
```