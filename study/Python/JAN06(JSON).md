# KDT 2기 1월 06일 학습내용
## 파일 입출력 활용

- open (file, mode='', encoding='UTF8')
    - file : 파일명
    - mode : 텍스트 모드
    - encoding : 인코딩 방식(일반적으로 utf-8활용)

모드 list

Mode|Mean
---|---
'r'|open for reading(읽기전용)
'w'|open for writing (쓰기,파일이 없으면 생성됨)
'x'|open for exclusive creation,falling if the file already exists<br/>(파일이 없을 때만 생성)
'a'|open for writing, appending to the end of file if it exists <br/>(쓰기전용, 파일의 마지막에 새로운 내용 추가)
'b'|binary mode(바이너리로 처리)
't'|text mode (기본 텍스트)
'+'|open for updating(reading and writing)<br/>'r+' - 읽고 쓰기/ 'w+' - 읽고 쓰기 (기존 파일은 삭제)

### 파일 객체 활용

1. f = open('file.txt', 'w') ~~~ / f.close() - 편집 후 호출 종료 해야함

2. with open('file.txt', 'w') as f:<br/>
   </t>read_file = f.read()

```py
# 일반적으로 with 키워드를 활용


.read() : 파일 전체를 읽음
.readline() : 명령때마다 한 줄 씩 읽음
.readlines() : 한 줄씩 전체를 읽음

'''텍스트 파일 개행 문자(\n) 같이 출력됨'''

# \n 삭제 방법
with open ('data/fruits.txt', 'r') as f:
    fruits = f.read().split('\n') # 1 .read() 를 이용한 것
    print(fruits)

with open ('data/fruits.txt', 'r') as f:
    fruits = f.readlines()        # 2 .readlines() 를 이용한것 
fruits = [line.rstrip('\n') for line in fruits]
print(fruits)

with open ('data/fruits.txt', 'r') as f:
    fruits = f.readlines()      # 2-1 for 문 사용
    for fruit in fruits:
        fruit = fruit.strip()
        print(fruits)

```
## JSON
-JSON 은 자바스크립트 객체 표기법으로 개발환경에서 많이 활용되는 데이터 양식으로 웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용함

- 문자 기반(텍스트) 데이터 포멧으로 다수의 프로그래밍 환경에서 쉽게 활용 가능함
    - 텍스트를 언어별 데이터 타입으로 변환시키거나 언어별 데이터 타입을 적절하게 텍스트로 변환


```PY
# 객체 ->JSON
import json
x = [1, 'dami', 'list']
json.dumps(x)
'[1, "dami", "list"]'

# JSON -> 객체

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

```