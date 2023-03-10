# KDT 2기 1월 02일 학습내용
### 컴퓨터(computer)
- caculation (조작)
- remember (저장)

### 프로그래밍 (programing)
- 명령어의 모음(집합)

## Python 기초

### 파이썬이란?
<br/>

#### Easy to learn
다른 프로그래밍 언어보다 문법이 간단하고 엄격하지 않음
(변수에 별도의 타입 지정이 필요 없다.)
<br/>

#### 인터프리터 언어
소스코드를 기계어로 변환하는 컴파일 과정 없이 바로 실행 가능
코드를 대화하듯 입력 실행하면 바로 확인 할 수 있다.
<br/>

#### 객체 지향 프로그래밍
파이썬은 모든 것이 객체로 이루어져 있다.

* 객체(object) : 숫자, 문자등 (물건,박스에 담기는 모든 것)

<br/>

### 변수(variable)란 ?

컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름 (박스)
박스, 객체를 담는 곳

ex)

name = '김창조'<br/>
age = 13<br/>
변수 = 객체<br/>
ㅁ<-O

변수는 할당 연산자(=)를 통해 값을 할당(assignment)
> = 는 같다라고 생각하지 않기, 할당한다라고 생각

- type()

    변수에 할당된 값의 타입

- id()

    변수에 할당된 값(객체)의 고유한 아이덴티티(identity) 값이며, 메모리주소

#### 변수 할당

- 같은 값을 동시에 할당 할 수 있음

x = y = 1004<br/>
x, y = 1 은 안됨

- 다른 값을 동시에 할당 할 수 있음

x, y = 1, 2

x = x + 1<br/> 
x = 5<br/>

: x = 6 (오른쪽 계산 먼저하고 할당, 오른쪽의 값을 왼쪽에 할당한다)

### 식별자(Identifiers)
- 파이썬 객채(변수,함수,모듈등)를 식별하는데 사용하는 이름
    - 규칙
    1. 영어,언더스코어(_),숫자로만 구성

        1-1) snake_case 
    - 파이썬에서 사용 (대문자x)

        1-2) Camel Case 
    - 자바에서 사용 (첫글자 대문자)


    2. 첫 글자에 숫자가 올 수 없음
    3. 길이제한은 없으나 대소문자 구별해야함
    4. 예약어는 사용 할 수 없음
    ```
    예약어
    False, None, True, and, as, assert, async, await,
    brask, class, continue, def, del, elif, else, except
    finally, for, from, global, if, import, in, is,
    lambda, nonlocal, not, or, pass, raise, return,
    try, while, with, yield
    ```
    5. 내장함수나 모듈등의 이름도 사용 x (동작이 안됨)

### 객체의 종류
1. 수치형
- 정수 
모든 정수의 타입은 int
- 실수 (소수점)
실수는 float 타입
> 값 비교시 실수인 경우 주의 해야함
- 복소수 (complex)
2. 불린형 (boolean)
- True, False 값을 가진 타입은 bool
- 1은 True 0 [] {} None 등등은 False

### 연산자
- 기본적인 사칙연산 및 수식 계산

연산자|내용
--- | ---
+|덧셈
-|뺄셈
*|곱셈
**|거듭제곱
/|나눗셈
//|몫
%|나머지


- 복합 연산자(연산과 할당 함께)

연산자|내용
--- | ---
a += b|a = a + b
a -= b|a = a - b
a *= b|a = a * b
a **= b|a = a ** b
a /= b|a = a / b
a //= b |a = a // b
a %= b |a = a % b

- 비교 연산자 (값을 비교 True,False 값 리턴)

연산자|내용
--- | ---
<|미만
<=|이하
```>```|초과
```>=```|이상
==|같음
!=|같지않음

- 논리 연산자 (논리식 판단 True,False 값 리턴)

연산자|내용
--- | ---
""And""|모두 True여야 True
""or""|모두 False 여야 False
Not - | True->False,False->True 

### 컨테이너
```여러 개의 값을 담을 수 있는 것(객체)```
- 컨테이너의 분류
1. 시퀀스
    - 문자열 : 문자들의 나열
    (str타입, '나 "를 이용하여 표기, 변경불가, 반복가능)
    - 리스트 : 변경 가능한 값의 나열
    - 튜플 : 변경 불가능한 값의 나열
    - 레인지 : 숫자의 나열
2. 컬렉션/비시퀀스
    - 세트 : 유일한 값들의 모음
    - 딕셔너리 : 키-값들의 모음

- 시퀀스형 주요 공통 연산자

연산|결과
---|---
s[i]|s의 i번째 항목, 0부터 시작
s[i:j]|s의 i에서 j까지의 슬라이스
s[i:j:k]|s이 i에서 j까지 스텝k의 슬라이스
s + t |s와 t 이어 붙이기
s * n |s 를 n 번 더하기
x in s |s의 항목중 하나가 x 와 같으면 True
x not in s|s의 항목중 하나가 x 와 같으면 False
len(s)|s의 길이
min(s)|s의 가장 작은 항목
max(s)|s의 가장 큰 항목

- 문자열 내에서 특정문자나 조작을 위해 \ 사용

예약문자|내용
---|---
\n|줄바꿈
\t|탭
\r|캐리지리턴
\0|널(Null)
```\\```|\
```\'```|단일인용부호(')
```\"```|이중인용부호(")

### 리스트
- 변경,반복 가능한 값들의 나열된 자료형
- 순서o, 서로 다른 타입의 요소 o
- 대괄호([]) 혹은 list() 형태, 요소는 (,) 로 구분
- .append()로 값 추가, .pop(인덱스)로 삭제 


## 코드를 작성하는 스타일 가이드

[파이썬에서 제안하는 스타일](https://peps.python.org/pep-0008/)

[기업,오픈소스에서 사용되는 스타일](https://google.github.io/styleguide/pyguide.html)
