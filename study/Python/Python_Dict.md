# KDT 2기 1월 05일 학습내용 #1
## 딕셔너리 (Dictionary)
- 키(key) : 값(value) 쌍으로 이루어진 모음 (개별요소는 ,로 구분) 
    - 키 : 불변 자료형만 가능(리스트,딕셔너리등 불가능)
    - 값 : 형태 상관 없음
> 키 : 값 추가/삭제 가능 , 키의 값을 변경하는 것이 가능하며 반복 가능 (키 반환)

```python
# 예시)

score = {
    'tom' : 100,
    'sally' : 95,
    'min' : 80,
}

print(score) # {'tom' : 100, 'sally' : 95, 'min' : 80}
score['tom'] # 100
score['dam'] # KeyError 없는 키 조회시 에러 발생

score['dam'] = 100 # 키 : 값 추가 
# {'tom' : 100, 'sally' : 95, 'min' : 80, 'dam' : 100}
score['min'] = 85 # 값 변경
# {'tom' : 100, 'sally' : 95, 'min' : 85, 'dam' : 100}
score.pop('sally') #키 : 값 삭제 .pop() 활용하여 삭제
# {'tom' : 100, 'min' : 85, 'dam' : 100}
```
### 딕셔너리 순회

- 딕셔너리는 기본적으로 key를 순회, key를 통해 값을 활용
- 메서드를 활용하여 순회 할 수 있다. (.key()/.values()/.items())
```python
# 예시)

grades = {'john' : 80, 'eric' : 90}

for name in grades:
    print(name) # john, eric
    print(name, grades[name]) # john 80 
                              # eric 90

* 추가 메서드
    print(grades.keys()) # dict_keys(['john', 'eric'])
    print(grades.values()) # dict_values([80, 90])
    print(grades.items()) # dict_items([('john', 80), ('eric', 90)])

for name, score in grades.items():
    print(name,score) # john 80
                      # eric 90
```


