# SQL_JOIN
- 테이블을 분리하면 관리는 용이해지나 출력 할때는 테이블 한 개만을 출력 할 수 밖에 없어 다른 테이블과 연력지어 출력하는 것이 필요하다.

## JOIN clause
- 둘 이상의 테이블에서 데이터를 검색하는 방법
- INNER JOIN, OUTER JOIN (LEFT,RIGHT) 이 있다.

## INNER JOIN clause
- 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환.

### INNER JOIN syntax
- FROM 절 이후 메인 테이블을 지정
- INNER JOIN 절 이후 메인 테이블과 조인할 테이블을 지정
- ON 키워드 이후 조인 조건을 작성
    - JOIN 조건은 두 테이블 간의 레코드를 일치시키는 규칠을 지정
```sql
SELECT -- 출력할 열 선택
    select_list 
FROM
    table1
INNER JOIN  table2
  ON table1.fk = table2.pk;
-- fk = foreign key , pk = primary key
```

## LEFT JOIN clause
- 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환.
### LEFT JOIN syntax
- FROM 절 이후 왼쪽 테이블 지정
- LEFT JOIN 절 이후 오른쪽 테이블 지정
- ON 키워드 이후 조인 조건을 작성

``` sql
SELECT
    select_list 
FROM
    table1
LEFT [OUTER] JOIN table2 -- OUTER 생략가능
  ON table1.fk = table2.pk;
```
- 왼쪽 테이블 레코드는 무조건 표시하고 매치되는 오른쪽 레코드가 없으면 NULL 표시
- 왼쪽 테이블 한개의 레코드에 오른쪽 테이블의 여러 레코드가 일치할 경우, 왼쪽 해당 레코드를 여러 번 표시

## RIGHT JOIN clause
- 왼쪽 테이블의 일치하는 레코드와 함께 오른쪽 테이블의 모든 레코드 반환
### RIGHT JOIN syntax
- FROM 절 이후 왼쪽 테이블 지정
- LEFT JOIN 절 이후 오른쪽 테이블 지정
- ON 키워드 이후 조인 조건을 작성

``` sql
SELECT
    select_list 
FROM
    table1
RIGHT [OUTER] JOIN table2 
  ON table1.fk = table2.pk;
```
- 오른쪽 테이블 레코드는 무조건 표시하고 매치되는 왼쪽 레코드가 없으면 NULL 표시
- 오른쪽 테이블 한개의 레코드에 왼쪽 테이블의 여러 레코드가 일치할 경우, 오른쪽 해당 레코드를 여러번 표시

### WHERE 절 사용

- WHERE 절을 사용하여 조회시 조건을 사용 할 수 있다.

``` sql
SELECT
    select_list 
FROM
    table1
RIGHT [OUTER] JOIN table2 
  ON table1.fk = table2.pk
WHERE table1.fk IS NULL;

-- 왼쪽 테이블의 값이 없는 경우만을 출력시켜 table2 에서 교집합 부분을 제외한 나머지를 확인 할 수 있다.
```

