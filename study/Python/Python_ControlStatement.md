# KDT 2기 1월 03일 학습내용

## String Formatting

1. % formatting : 오래된 방법 (c style)
2. String formatting : 새로운 스타일의 방법<br/>
{}에 대응하는 것을 format()에 입력하여 전달

3. f-string: 문자열에 변수를 활용하여 만드는 방법<br/>
변수를 직접 입력하기 때문에 가독성이 좋음

ex)
```python
name = "dami"
score = 4.5

print('hello %s, my grade %.1f' % (name, score))     # 1
print('hello {}, my grade {}'.format(name, score)) # 2
print(f'hello {name}, my grade {score}')
  # 3
```

## 형 변환(Typecasting)

1. 암시적 형 변환 (파이썬 내부적으로 자료형 변환)
- bool
- Numeric type (int,float, complex)

ex)
```python
True + 3 #4
3 + 5.0 #8.0
3 + 4j + 5 #(8+4j)
```

2. 명시적 형 변환(특정 함수 활용 의도적 변형)

- int
    - str, float -> int
```python
int('3') + 4 #7
```

- float
    - str, int -> float
```python
float('3.5') + 5 #8.5
```

- str
    -int,float, list tuple, dict -> str

<br/>

> str -> int,float : 형식에 맞는 문자열만 가능 

<br/>

 ## 제어문  
 - 파이썬은 위에서부터 아래로 순차적으로 명령 수행하여
 특정 상황에 따라 코드를 선택적(분기,조건) 혹은 계속적(반복) 실행하는 제어가 필요함.
 >제어문은 순서도 표현이 가능

 1. 조건문
  - 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용
  
```
if<참/거짓 조건식>:
    #참인 경우 실행 되는 코드
else:
    #이외의 경우 실행 되는 코드
```    

2. 복수 조건문
- 복수의 조건식일 경우 elif를 활용
```
if<참/거짓 조건식>:
    #참인 경우 실행 되는 코드
elif<참/거짓 조건식>:
    #참인 경우 실행 되는 코드
else:
    #이외의 경우 실행 되는 코드
```    

3. 중첩 조건문
- 조건문은 다른 조건문에 중첩되어 사용될 수 있음

```
if<참/거짓 조건식>:
    #참인 경우 실행 되는 코드
    if<참/거짓 조건식>:
        #참인 경우 실행 되는 코드
else:
    #이외의 경우 실행 되는 코드
```    
> 들여쓰기 주의해서 입력해야 한다.


```python
#예시

dust = int(input('오늘의 미세먼지 농도는?'))
if dust > 150:
    print('매우나쁨')
    if dust > 300:
        print('실외 활동을 자제하세요.')
        # 300이 넘을 경우 매우나쁨,실외 활동을 자제하라는 내용이 출력된다.
elif dust >80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    if dust >= 0 :
        print('좋음') 
    else: # 0보다 작은 값은 잘못 입력되었다고 출력 (중첩 조건문)
        print('잘못 입력 되었습니다.')
```
4. 반복문
> 특정 조건을 도달할 때까지, 계속 반복되는 문장
- while 문
    - 조건식이 참인 경우 반복적으로 코드를 실행 (종료조건이 반드시 필요)
```python
# 예시
# 1부터 입력한 정수까지의 총합을 구하는 코드
n = int(input())
m = 0
total = 0

while m <= n: # 입력된 정수와 같거나 작은 동안 계속 반복
    total += m # 0 1 3 6 ...
    m += 1 # 0 1 2 3 ...
print(total)
```
- for 문
    - 시퀀스(Sting, tuple, list, range)를 포함한 순회가능한 객체요소를 모두 순회
    (별도의 종료조건 필요없음,마지막 값까지 계속 반복)

```python
# 문자열 순회 예시
1. 반복가능한 객체 요소
n = input() # hi

for N in n:
    print(N)  #h
              #i -> 한글자씩 세로로 출력
2. range 인덱스화
n = input() #hi

for idx in range(len(n)):
    print(n[idx]) #h
                  #i -> 입력한 문장 글자수의 길이 만큼 순회하여 출력
```
### 반복문 제어
1. break : 반복문을 종료

```python
# 예시

for i in range(10):
    if i > 1: 
        print('0과 1만 필요해')
        break
    print(i)

-> 실행

'''
0
1
0과 1만 필요해 
''' # i가 1 보다 클 때 출력 후 break 한 모습
```


2. continue : 다음 반복을 수행

```python
# 예시

for i in range(6):
    if i % 2  == 0:
        continue
    print(i)

-> 실행

'''
1
3
5
''' # continue로 인해 짝수가 출력 되지 않고 다음 반복을 실행, continue가 없었다면 짝수가 출력 되었을 것이다. 
```

3. for-else : 반복문 실행 후 else문 실행

```python
# 예시

1.
for n in 'apple':
    if n == 'b':
        print('b!')
        break
else:
    print('b가 없습니다.')

-> 실행

'''
b가 없습니다.
''' # for문에서 break 되지 않아 else문 실행

2.
for n in 'banana':
    if n == 'b':
        print('b!')
        break
else:
    print('b가 없습니다.')

-> 실행

'''
b!
''' # b를 만나 break 되어 else문 실행 되지 않음
```
> for문에서 break로 중단되었는지 여부에 따라 실행


## 레인지(range)
 ``` - 숫자의 시퀀스를 나타내기 위해 사용되며 변경이 불가능하나 반복 가능하다.```
1. 기본형
range(n) : 0~n-1 까지의 숫자 시퀀스
2. 범위 지정
range(n,m) : n~m-1 까지의 숫자 시퀀스
3. 범위, 스텝 지정
range(n,m,s) : n~m-1 까지 s 스탭의 숫자 시퀀스
