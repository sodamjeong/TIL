# SQL_DQL(Data Query Language, 데이터 검색)
## Querying data
### SELECT statement
- 테이블에서 데이터를 조회

### SELECT syntax
- SELECT 키워드 다음에 데이터를 선택하려는 필드를 하나 이상 지정.
- FROM 키워드 다음에 데이터를 선택하려는 테이블의 이름을 지정.
```SQL
SELECT
    select_list -- '*' 입력시 전체 필드를 조회 할 수 있다.
FROM
    table_name;
```

- SELECT 필드이름 AS '별칭' <BR/>(AS ~ 를 사용하여 출력시 필드명을 별칭으로 지정 출력 할 수 있다.)
- SELECT product, sales * price AS '판매 총액'<BR/>(Product에 대한 price 와 sales를 곱한 필드를 조회 할 수 있다. 기본적인 사칙연산 사용 가능)
## Sorting data
### ORDER BY clause
- 조회 결과의 레코드를 정렬

### ORDER BY syntax
- FROM 절 뒤에 위치
- 하나 이상의 컬럼을 기준으로 결과를 오름차순, 내림차순으로 정렬할 수 있다.
```SQL
SELECT
    select_list
FROM
    table_name
ORDER BY
    column 1 [ASC|DESC], -- ASC : 오름차순 (기본 값)
    column 2 [ASC|DESC], -- DESC : 내림차순 
    ...;
```
- 별칭 지정 시 별칭 기준 정렬이 가능하다.
```SQL
SELECT
    Product, sales * price AS 'totalSales'
FROM
    orders
ORDER BY
    ProductCode ASC, totalSales DESC;
```
## Filtering data
### DISTINCT clause
- 조회 결과에서 중복된 레코드를 제거
### DISTINCT syntax
- SELECT 키워드 바로 뒤에 작성
- SELECT DISTINCT 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드 지정
```sql
SELECT DISTINCT
    select_list
FROM
    table_name;
```
### WHERE clause
- 조회시 특정 검색 조건을 지정
### WHERE syntax
- FROM clause 뒤에 위치
- 비교연산자 및 논리연산자를 사용하는 구문이 사용된다.
    - 연산자 종류

    종류|연산자
    ---|---
    비교|=,!=,<,>,<=,>=
    범위|BETWEEN (```~에서 ~ 까지/ BETWEEN ~ AND ~ ```)
    집합|IN, NOT IN
    패턴|LIKE (```LIKE '%555' > 555로 끝나는 항목```)<BR/>(```LIKE '___y'``` > y로 끝나는 4글자인 항목('_' 글자수))
    NULL|IS NULL, IS NOT NULL
    복합 | AND, OR, NOT 

```sql
SELECT
    select_list, select_list2
FROM
    table_name
WHERE
    select_list = 1 AND select_list2 != 'cat';
```
### LIMIT clause
- 조회하는 레코드 수를 제한
### LIMIT syntax
- LIMIT clause 하나 또는 두개의 인자를 사용한다.
- row_count는 조회할 퇴대 레코드 수를 지정

```sql
SELECT
    select_list, select_list2
FROM
    table_name
LIMIT 3, 5; -- 4 ~ 8 조회 (3 이후 5개 조회)
```
## Grouping data
### GROUP BY clause
- 레코드를 그룹화하여 요약본 생성 with 집계 함수
    - 집계함수(Aggregation Functions) : SUM, AVG, MAX, MIN, COUNT
### GROUP BY syntax
- FROM 및 WHERE 절 뒤에 배치
- GROUP BY 절 뒤에 그룹화할 필드 목록을 작성
- HAVING 절은 GROUP BY 와 주로 함께 사용 되며 집계 항목에 대한 세부 조건을 지정한다.

```SQL
SELECT
    select_list, COUNT(*) AS 'count'-- 각 그룹에 대한 집계된 값을 계산
FROM
    table_name;
GROUP BY 
    select_list;
HAVING
    'count' > 5 -- 집계된 값이 5보다 큰 경우만 조회
```
