# SQL Basics

- 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
- Structure Query Language<br/>
(테이블의 형태로 구조화된 관계형 데이터베이스에게 요청을 질의(요청))
- Query(질의,질문) : 데이터베이스로부터 정보를 요청 하는 것
- 일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라고 한다.
- 컴퓨터와의 대화를 프로그래밍 언어로 한다면 관계형 데이터베이스와의 대화를 SQL로 한다고 볼 수 있다.

## SQL Syntax

- SQL 키워드는 대소문자를 구분하지 않으나 대문자로 작성하는 것을 권장한다.
- 각 SQL Statements의 끝에는 세미콜론 (;)이 필요하다.
( 세미콜론은 각 SQL Statements을 구분하는 방법이다.)

## SQL Statements
- SQL 언어를 구성하는 가장 기본적인 코드 블록
```SQL
SELECT column_name FROM table_name;

-- 해당 예시 코드는 SELECT Statement 라고 부른다.
-- 이 Statement는 SELECT,FROM 2개의 keyword로 구성된다.
```
- SQL Statements 유형
    - 데이터베이스에서 수행 목적에 따라 대체로 4가지 범주로 나뉜다.
    1. DDL - 데이터 정의
    (Data Definition Language)<br/> 
    데이터의 기본 구조 및 형식 변경<br/>
    ```keyword - CREATE, DROP, ALTER ```
    2. DQL - 데이터 검색
    (Data Query Language)<br/>
    ```keyword - SELECT```
    3. DML - 데이터 조작(추가, 수정, 삭제)
    (Data Manipulation Language)<br/>
    ```keyword - INSERT, UPDATE, DELETE```
    4. DCL - 데이터 제어
    (Data Control Language)<br/>
    데이터 및 작업에 대한 사용자 권한 제어<br/>
    ```keyword - COMMIT, ROLLBACK, GRANT, REVOKE```

### SQL 표준

- SQL은 미국 국립 표준 협회(ANSI)와 국제 표준화 기구(ISO)에 의해 표준이 채택되었다.
- 널리 사용되는 모든 RDBMS에서 SQL 표준을 지원한다.
- RDBMS별로 독자적인 기능에 따라 표준을 벗어나는 문법도 존재하니 주의해야 한다.

 
