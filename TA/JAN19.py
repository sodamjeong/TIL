# 2576 홀수
s = []
for i in range(7):
    if (n:=int(input())) % 2 == 1:
        s.append(n) # 입력된 숫자 중 2로 나눈 나머지가 1이면 리스트에 삽입
if len(s)==0: # 리스트 길이가 0일때, 즉 홀수가 없으면
    print('-1') # -1 을 출력한다.
else:
    print(f'{sum(s)}\n{min(s)}') # 홀수가 있으면 전부 더한 값 그리고 그중 작은 수를 출력하도록 했다.

# 10822 더하기
print(sum(map(int,input().split(',')))) # ',' 기준으로 요소를 나눠주고 전부 더하도록 했다.

# 2754 학점계산

n = list(input())
i = float('FDCBA'.index(n[0])) # 학점을 입력하면 해당 학점의 인덱스를 소수화 시켰다.

if len(n)==1: # F 는 길이가 1이므로 바로 0.0이 출력 될 수 있도록 했다.
    print(i)
else: # F 가 아니라면
    if n[1] == '+': # 학점 점수에 0.3을 더하거나 빼는 계산을 하도록 했다.
        print(i+0.3)
    elif n[1] == '-':
        print(i-0.3)
    else:
        print(i)

# 5622 다이얼

n = input()
m = {
    'ABC':3,'DEF':4,'GHI':5,
    'JKL':6,'MNO':7,'PQRS':8,
    'TUV':9,'WXYZ':10
}
time = [] 
for x in n:
    for y in m: # 입력한 단어의 알파벳 하나하나 값을 찾아
        if x in y: # 리스트에 넣어 더한 값을 출력 하도록 했다.
            time.append(m.get(y))
print(sum(time))

# 2577 숫자의 개수

n = [int(input())for i in range(3)]
m = str(n[0]*n[1]*n[2]) # 입력한 숫자 3개를 리스트로 만들어 모두 곱하여  string 으로 변경하고

for i in range(10): # 0~9 까지의 숫자가 
        print(m.count(str(i))) # 몇번 들어가 있는지 카운트하는 메소드를 사용하여 출력하도록 했다.

# 7785 회사에 있는 사람

import sys
input = sys.stdin.readline
office = {} # 빈 딕셔너리에

for i in range(int(input())):
    log = input().split()
    if log[0] not in office: # 아직 딕셔너리에 없는 이름은 값을 추가하고
        office[log[0]] = 1
    else: # 이미 딕셔너리에 있는 이름이 또 나온다면 떠난다는 의미이므로
        del office[log[0]] # 삭제시켰다.

print(*sorted(office)[::-1],sep='\n') # 이름을 역순으로 정렬하여 한줄씩 출력하도록 했다.