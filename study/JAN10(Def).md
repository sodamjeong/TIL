# KDT 2기 1월 10일 학습내용
## 사용자 정의 함수

### 함수 기본 구조
1. 선언과 호출(Define & Call)
 - 함수의 선언은 ```def``` 키워드를 활용함<br/> 들여쓰기를 통해 실행 될 코드를 블록을 작성한다.<br/> 함수는 동작 후 return을 통해 결과값을 전달한다.<br/> 함수는 함수명으로 호출
```py
 ex)
 def add(a,b):
    return a + b

print(add(5,4)) # 9
```

2. 입력 (Input)
- Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
- Argument : 함수를 호출 할 때 넣어주는 값 <br/>
소괄호 안에 할당 function(argument)
    - 필수 Arg : 반드시 전달되어야 하는 Arg
    - 선택 Arg : 값을 전달하지 않아도 되는 경우는 기본 값이 전달


```py
ex)
def cook(parameter):
    return 'good'

print(cook('argument')) # good
```

- def function_name(*args) : 여러개의 argument 들을 입력할 때 <br/>parameter에 *을 붙여 표현  Argument 들은 튜플로 묶여 처리
- def function_name(**kwargs) : kwargs = Keyword Arguments<br> parameter에 **를 붙여 표현 Arg 들은 딕셔너리로 묶여 처리

```py
ex)
def number(*x):
        print(x)

number(1,2,3,4,5) # (1,2,3,4,5)

def family(**x):
    for key, value in x.items():
        print(key, ':', value)

family(father = 'dong', mother = 'lee', me = 'dami', brother = 'sung')

#father : dong
#mother : lee
#me : dami
#brother : sung
```

3. 범위 (Scope)

- 함수는 코드 내부에 local scope를 생성, 그외 global scope
local scope 에서 정의된 변수는 함수가 호출 될 때 생성, 종료 될 때 까지 유지된다.

```py
def fun():
    a = 20
    print(a) 

fun() # 20
print(a) # NameError: name 'a' is not defined
```
- 이름(식별자)를 찾아 나가는 순서(LEGB Rule)
1. Local scope : 함수
2. Enclosed scope : 특정 함수의 상위 함수
3. Global scope : 함수 밖의 변수, Import 모듈
4. Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성

- global문
    - 현재 코드 블록 전체에 적용, 나열된 식별자가 global에서 정의된 변수임을 나타낸다.

```py
a = 10
def fun():
    global a
    print(a)
    a = 3 # 글로벌 변수 변경도 가능하다

fun() # 10
print(a) # 3
```


4. 결과값 (Output)

- 함수는 값을 하나만 return함 (명시적 return이 없다면 None 반환)<br/> return과 동시에 실행이 종료됨.

```py
ex)
def cube(x,y):
    return x + y, x - y

print(cube(3,5)) # (8, -2) 튜플 반환
```

