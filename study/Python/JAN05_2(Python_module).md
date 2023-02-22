# KDT 2기 1월 05일 학습내용 #2
## 파이썬 표준 라이브러리
- [파이썬에 기본적으로 설치된 모듈과 내장 함수](https://docs.python.org/ko/3/library/index.html)


---
module : 다양한 기능을 하나의 파일로 만든 모듈<br/>
^<br/>
package : 다양한 파일을 하나의 폴더로 만든 패키지(여러 모듈의 집합)<br/>
^<br/>
library: 다양한 패키지를 하나의 묶음으로 만든 라이브러리<br/>
^<br/>
pip: 이 것을 관리하는 관리자
    
---
### 1. 모듈
 - 특정 기능을 하는 코드를 파이썬 파일(.py)단위로 작성한 것
    - 활용 방법 : 
    import module (모듈 불러오기)<br/>
    from module import function (모듈에서 함수 불러오기)<br/>
    from package.module import function (패키지 모듈에서 함수 불러오기)<br/>
    from package import module (패키지에서 모듈 불러오기)
> function 외 var,Clas 등등.. 불러오기 가능하다.

```모듈 예시```

1. **random** (임의 숫자 생성, 무작위 요소 선택)<br/>
    ```py
    1-1. random.randint(a, b)
        : a 이상 b 이하의 임의의 정수를 반환
    1-2. ranodom.choice(seq)
        : 비어 있지 않은 시퀀스에서 임의의 요소 반환
    1-3. random.shuffle(seq)
        : 시퀀스 요소를 그자리에서 랜덤으로 섞음
    1-4. random.sample(population, k)
        : population 내에서 k 길이의 리스트 반환

    ex) 
    import random

    n = (1, 5, 6, 6, 12, 5, 123, 5, 4)

    print(random.randint(4,15)) # 4~15 임의 수 
    print(random.choice(n)) # n 리스트 중 임의 수
    random.shuffle(n) # 리스트 요소 섞기
    print(n) # 출력 ex) [5, 6, 123, 4, 1, 5, 6, 12, 5]
    print(random.sample(n, 2)) # ex) [1, 4]
    ```
2. **datetime** (날짜와 시간을 조작하는 객체 제공)
    ```py
    2-1. datetime.date(year, month, day)
        : 모든 인자 필수, 인자는 특정 범위에 있는 정수여야 함
    2-2. datetime.date.today()
        : 현재 지역의 날짜를 반환
    2-3. datetime.datetime.today()
        : 현재 지역 datetime 반환 / now() - 타임존 설정 가능
    
    ex)
    import datetime

    
    print(datetime.date(2023, 1, 5)) # 2023-01-05
    print(datetime.date.today()) # 2023-01-05
    print(datetime.datetime.today()) # 2023-01-05 23:12:46.581255 
    ```
### 2. 패키지
- 특정 기능과 관련된 여러 모듈의 집합, 패키지 안에는 또 다른 서브 패키지가 포함 되어있다.

<br/>

#### 파이썬 패키지 관리자(pip)
- ```pyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템```

```py
# 패키지 활용 명령어 (bash,cmd 환경에서 사용)

1. 설치

pip install SomePackage # 최신 버전 패키지 설치
pip install SomePackage==1.0.5 # 특정 버전 패키지 설치
pip install 'SomePackage>=1.0.4' # 최소 버전 명시하여 설치

이미 설치되어 있는 경우 이미 설치되어 있음을 알려줌

2. 삭제

pip uninstall SomePackage # 특정 패키지 삭제

3. 목록 및 정보 확인

pip list # 패키지 목록 및 버전 확인
pip show SomePackage # 특정 패키지 정보 확인

4. 관리

pip freeze # 설치된 패키지의 목록
pip freeze > requirements.txt  # .txt 생성 _ 나의 python 라이브러리, 버전 목록을 텍스트 파일로 생성 (패키지를 기록하는 파일의 이름은 일반적으로 requirements.txt로 정의)
pip install -r requirements.txt  # .txt 설치 _ requiremenrs의 사항에 맞는 모든 라이브러리를 설치
```



