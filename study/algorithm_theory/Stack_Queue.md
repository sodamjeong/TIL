# 스택과 큐

## 스택 자료구조 (Stack)

- 먼저 들어 온 데이터가 나중에 나가는 형식(선입후출)의 자료 구조
- 입구와 출구가 동일한 형태로 스택을 시각화 할 수 있다.<br/>

```py

# ex) 박스쌓기

stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() # 마지막에 쌓은 7 삭제
stack.append(1)
stack.append(4)
stack.pop() # 마지막에 쌓은 4 삭제

print(stack[::-1]) # 최상단 기준 출력 [1, 3, 2, 5]
print(stack) # 최하단 기준 출력 [5, 2, 3, 1]
```

## 큐 자료구조 (Queue)

- 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료 구조
- 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있다.

```py
from collections import deque
# 큐 구현 시 deque 라이브러리를 사용해야 한다.

 queue = deque()

 queue.append(5)
 queue.append(2)
 queue.append(3)
 queue.append(7)
 queue.popleft() # 가장 먼저 들어온 요소 5 삭제
 queue.append(1)
 queue.append(4)
 queue.popleft() # 두번째로 들어온 요소 2가 삭제된다.

print(queue) # 먼저 들어온 순서대로 출력 deque([3, 7, 1, 4])
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력 deque([4, 1, 7, 3])
```

## 우선순위 큐(Priority Queue)

- 우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료 구조
- 우선순위 큐는 데이터를 우선순위에 따라 처리하고 싶을 때 사용한다.

### 구현하는 방법
1) 단순히 리스트를 이용하여 구현 할 수 있다.
2) 힙(heap)을 이용하여 구현 할 수 있다.

- 데이터의 개수가 N개 일 때, 구현 방식에 따라서 시간 복잡도가 다르다.

우선순위 큐 구현 방식 | 삽입 시간 | 삭제 시간
---|---|---
리스트|O(1)|O(N)
힙(Heap)|O(logN)|O(logN)

## 힙(Heap)의 특징

- 힙은 완전 이진 트리 자료구조의 일종이다.
- 힙에서는 항상 루트 노드(root node)를 제거한다.
1) 최소 힙(min heap)
    - 루트 노드가 가장 작은 값을 가진다.
    - 값이 작은 데이터가 우선적으로 제거된다.
2) 최대 힙(max heap)
    - 루트 노드가 가장 큰 값을 가진다.
    - 값이 큰 데이터가 우선적으로 제거된다.

### 완전 이진 트리 (Complete Binary Tree)
- 완전 이진 트리 :  루트(root)노드 부터 시작해 왼쪽, 오른쪽 자식 노드 순서대로 데이터가 차례대로 삽입되는 트리

### 최소 힙 구성 함수 (Min - Heapify())
- 상향식으로 부모 노드로 거슬러 올라가며 부모노드가 자신보다 값이 더 작을 경우 위치를 교체 한다.

### heapq 모듈 사용하기 (Python)

```py
import heapq
# 파이썬 내장 모듈 heapq 불러오기

heap = [] # 빈 리스트 생성

heap.heappush(heap,1)
heap.heappush(heap,4)
# heap.heappush(리스트명,삽입 원소) 원소를 삽입한다.

print(heap) # [1, 4]

print(heapq.heappop(heap)) # [1]
print(heap) # [4]
# heapq.heappop(리스트명) 원소를 삭제 (최솟값을 삭제한다.)

# 삭제하지 않고 최솟값 출력 시 print(heap[0]) 
# 최소값이 가장 위로 오는 이진 트리 구조로 heap[1] 이 두 번째로 작은 원소는 아니다.
```