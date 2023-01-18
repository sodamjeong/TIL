# 9085 더하기
for i in range(int(input())): # 테스트 케이스 수 입력
    _ = input() # 자연수 개수
    print(sum(a := (list(map(int,input().split())))))
# 바다코끼리를 사용하여 a 변수에 입력하는 자연수의 리스트 부여하고 sum 하여 출력

# 10824 네수

n = list(input().split()) # 숫자 4개를 문자열로 입력받는다
a = n[0]+n[1] # 첫번째 두번째 문자를 합친다.
b = n[2]+n[3] # 세번째 네번째 문자를 합친다.

print(int(a)+int(b)) # 정수로 변환하여 합쳐 출력한다.

# 3009 네 번째 점

x = {} # 직사각형은 두개의 x 좌표와 
y = {} # 두개의 y 좌표가 필요하다.

for i in range(3): # 세번의 숫자를 입력받는다.
    a, b = list(map(int,input().split()))
    if a not in x:
        x[a] = 1 # 빈 딕셔너리에 x 좌표 값과 
    else:
        x[a] +=1 # x 좌표의 개수를 채운다.
    if b not in y:
        y[b] = 1 # 마찬가지로 y 좌표값,
    else:
        y[b] += 1 #  y 좌표의 개수를 채운다.

for v in x:
    if x[v] == 1: # x 좌표값이 한번 입력된 키 출력
        print(v,end=' ') # 한줄에 출력될 수 있게 end=' ' 추가
        for v2 in y: 
            if y[v2] == 1: # y 좌표값이 한번 입력된 키 출력
                print(v2)

# 10952 A+B - 5

while 1: 
    a, b = map(int,input().split()) # 두 개의 정수를 입력 받고
    if a + b > 0: # 결과가 0보다 클 경우 a + b 값을 출력한다.
        print(a+b)
    if a + b == 0: # 0 0 이 입력되면 break
        break

# 1110 더하기 사이클

n = int(input())
m = n # while 문에서 break 조건문을 걸기 위한 복사본을 만든다.
cnt = 0

while 1:
    a = m // 10 # a 변수에 m을 10으로 나누었을 때 몫을 부여 (10의 자리수)
    b = m % 10 # b 변수에 m을 10으로 나누었을 때 나머지를 부여(1의 자리수)
    m = (b * 10) + ((a + b) % 10) # 1의 자리수에 10을 곱해 10의 자리수가 될 수 있도록 한다.
    # m의 10의 자리수, 1의자리수를 더했을 때 1의 자리수를 구해 더해준다.
    cnt += 1 # 사이클 한번을 돌 때 마다 1을 더해준다.
    if m == n: # 원래 입력했던 값과 복사본의 값이 같으면
        print(cnt) # 사이클의 길이를 출력하고 break
        break