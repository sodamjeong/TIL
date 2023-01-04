# KDT 2기 1월 04일 학습내용
## 파이썬 함수 (Function)

- 특정한 기능을 하는 코드의 조각, 특정 명령을 수행하는 코드를 매번 작성하지 않고 필요시에 간편하게 사용 할 수 있다.

    - 함수를 사용 하는 이유? <br/>복잡한 내용을 숨기고. 기능에 집중하여 사용 가능하다.<br/>
    재사용성,가독성,생산성을 위해!

### 자주 사용 하는 함수

1. print (*objects, sep='', end='\n', file=None, flush=False)
2. len(s) : 객체의 길이를 반환
3. sum(iterable, start=0) : 왼쪽에러 오른쪽으로 합하고 합계 반환
4. max(iterable) : 가장 큰 항목 반환
5. min(iterable) : 가장 작은 항목 반환
6. abs(x) : 숫자의 절댓값을 반환
7. divmod(a, b) : 두 수를 받아 몫과 나머지를 반환
8. pow(base, exp) : base의 exp 거듭제곱 반환
9. round(number,digit) : number 반올림, digit 소수점 반영
10. all(iterable) : 모든 요소가 참이면 True 반환
11. any(iterable) : 하나라도 참이면 True
12. bin(x) : 정수를 "0b" 접두사가 붙은 이진 문자열로 반환
13. hex(x) : 정수를 "0x" 접두사가 붙은 16진수 문자열로 반환
14. oct(x) : 정수를 "0o" 접두사가 붙은 8진수 문자열로 반환
15. ord(c) : 유니코드 문자 c에 대응되는 유니코드 숫자로 반환
16. chr(i) : 유니코드 숫자가 정수 i에 대응되는 문자를 반환
17. map(function, iterable) : 순회 가능한 데이터 구조의 모든 요소에 함수를 적용하고 그 결과를 map object로 반환


[파이썬 내장 함수 확인하기!](https://docs.python.org/ko/3/library/functions.html)
