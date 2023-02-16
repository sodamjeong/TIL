# SQL_Subquery
## Subquery
- 단일 쿼리문에 여러 테이블의 데이터를 결합하는 방법
- 조건에 따라 하나 이상의 테이블에서 데이터를 검색하는데 사용
- SELECT, FROM, WHERE, HAVING 절 등에서 다양한 맥락에서 사용
```sql
SELECT *
FROM table1
WHERE table_fk = (
    -- subquery
    SELECT table_fk
    FROM table2
    WHERE ...
);
```
## EXISTS
- 쿼리 문에서 반환된 레코드의 존재 여부를 확인
### EXISTS syntax
- subquery가 하나 이상의 행을 반환하면 EXISTS 연산자는 true를 반환하고 그렇지 않으면 false를 반환
- 주로 WHERE절에서 subquery의 반환 값 존재 여부를 확인하는데 사용
```sql
SELECT
    select_list
FROM
    table
WHERE
    [NOT] EXISTS (subquery);
```
## CASE
- SQL문에서 조건문을 구성
### CASE syntax
- case_value가 when_value와 동일한 것을 찾을 때 까지 순차적으로 비교
- when_value 와 동일한 case_value를 찾으면 해당 THEN절의 코드를 실행
- 동일한 값을 찾지 못하면 ELSE절의 코드를 실행
    - ELSE절이 없을 때 동일한 값을 찾지 못하면 오류 발생
```sql
CASE case_value
    WHEN when_value1 THEN statements
    WHEN when_value2 THEN statements
    ...
    [ELSE else-statements]
END CASE;
```

```sql
-- 예시
-- customers 테이블에서 customerNumber와 creditLimit 그리고 
-- 고객들의 creditLimit에 따라 VIP, Platinum, Bronze 등급을 매겨 조회 
-- VIP = 100,000 초과, Platinum = 70,000 초과 그외 Bronze
SELECT customerNumber, creditLimit,
    CASE
        WHEN creditLimit > 100000 THEN 'VIP'
        WHEN creditLimit > 70000 THEN 'Platinum'
        ELSE 'Bronze'
    END AS grade -- 해당 속성 이름 설정
FROM customers;
```