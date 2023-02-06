# 1547 공
cup = [0,1,0,0]
for i in range(int(input())):
    x, y = map(int,input().split())
    cup[x],cup[y] = cup[y],cup[x]
print(cup.index(1))


# 5576 콘테스트
score = [int(input()) for _ in range(20)]
print(sum(sorted(score[:10])[-3:]),sum(sorted(score[10:])[-3:]))

# 2846 오르막길
n = int(input())
m = list(map(int,input().split()))
up = []
road = 0
for i in range(n-1):
    if m[i] < m[i+1]:
        road += m[i+1] - m[i]
    else:
        up.append(road)
        road = 0
up.append(road)
print(max(up))
# 1251 단어 나누기

word = input()
a = chr(min(map(ord,word[:-2]))) #단어 뒤에 두개 남기고 제일 작은 알파벳
b = chr(min(map(ord,word[word.index(a)+1:-1]))) # a 이후 뒤에 한개 남기고 제일 작은 알파벳
c = word[word.index(b)+1:] # 나머지
a1 = word[:word.index(a)+1][::-1] # a까지 길이의 단어 뒤집기
b1 = word[word.index(a)+1:word.index(b)+1][::-1] # a이후 b까지 길이의 단어 뒤집기
print(a1+b1+c[::-1]) # a1,b1 그리고 c를 뒤집은 단어를 합쳐서 출력
#  틀림
# 반례  = input aabbcc output accbba 정답 aabbcc
# 이렇게 풀면 제일 작은 단어가 연속 두개 나올때 구분 할 수 가 없다.


word = input()
words = []
for i in range(1,len(word)):
    a = word[:i][::-1]
    for j in range(i, len(word)-1):
        b = word[i:j+1][::-1]
        c = word[j+1:][::-1]
        words.append(a+b+c)
print(sorted(words)[0])