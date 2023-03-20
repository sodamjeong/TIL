# KDT 2기 1월 11일~12일 학습내용
## Class
- '객체 지향 프로그래밍'을 위해 필요한 개념. 기본적인 코딩방법은 절차 지향방식 순서대로 코드를 작성하는 방식
- C++ 이나 파이썬은 Class 개념이 있다.

### Class 개념

- 과자 틀 → 클래스 (class)<br/>
- 과자 틀에 의해서 만들어진 과자 → 객체 (object)

클래스(class)란 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 과자 틀,<br/> 객체(object)란 클래스로 만든 과자 틀을 사용해 만든 과자

클래스로 만든 객체는 객체마다 고유한 성격을 가진다는 특징이 있다.<br/> 과자 틀로 만든 과자를 조금 베어 먹더라도 다른 과자에는 아무 영향이 없는 것과 마찬가지로 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않는다.

### Class 객체 만들기

- 객체는 클래스를 이용하여 만든다. 객체는 해당 클래스의 결괏값을 돌려받는다. class 로 만들어진 객체를 해당 class의 인스턴스라고 한다.

```py
class Cookie:
    pass

a = Cookie() # Cookie 의 인스턴스 a, b
b = Cookie()
```

```py

# class 만들어 보기 예시

class calculator: # 클래스 이름 지정
    pi = 3.14 # class 속성도 정의 할 수 있다.
    def data (self, x, y): # 클래스 안에 구현된 함수는 메서드(매개변수)
        self.x = x # 메서드의 수행문 
        self.y = y # 메서드의 수행문
    def add(self): # add 메서드 생성
        result = self.x + self.y # 지정 값을 더해라
        return result # 결과 반환


a = calculator() # 해당 클래스의 인스턴스 a 생성
print(type(a)) # <class '__main__.calculator> 해당 클래스 타입

a.data(4, 2) # 인스턴스 a에 연산을 수행할 값 지정하기
print(a.x) # 4
print(a.y) # 2
print(a.add()) # 4 + 2 (결괏값 6 반환)


b = calculator() # 해당 클래스의 인스턴스 b 생성
b.data(3, 8) # b에 값 지정하기
print(b.pi) #  3.14 (class 변수값)
b.pi = 3.1415
print(b.pi) # 3.1415 (class의 변수값과 별개로 인스턴스의 변수를 설정 할 수 있다.)
print(a.pi) # 3.14

```

1. class 이름 지정
2. class 에 동작할 메서드 만들기 (def 를 이용)
 ```py
class calculator:
    def __init__(self, x, y): # self 생성되는 객체, x = 첫번째 객체 변수, y = 두번째 객체 변수
        self.x = x
        self.y = y

a = calculator(4,2) 

# 메서드 이름을 __init__으로 할 경우 인스턴스 생성과 동시에 값 지정을 할 수 있다.

__init__ 이 아니라면 a = calculator a.data(4, 2) 두번의 명령으로 값 지정
```
3. 객체 생성 (해당 class의 인스턴스)

### Class의 상속
 - class 는 이전 정의된 class 의 기능을 물려 받을 수 있다.

 ```py
 class morecalculator(calculator):
    def mul(self):
        return x * y

a = morecalculator(5, 7)
print(a.add()) # 12 (calculator의 기능을 상속 받아 add 메서드를 사용 할 수 있다.)
print(a.mul()) # 35 
```
- 기능을 상속 받은 class에서 다시 기능을 설정 할 수 있다.

```py
 class morecalculator(calculator):
    def add(self):
        result = self.x + self.y + 1
        return result

a = morecalculator(5,7)
print(a.add()) # 13 (이전의 결과 12가 아닌 + 1 이 추가된 기능이 실행된다.)

