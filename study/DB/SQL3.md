# SQL_DDL(Data Definition Language,데이터의 기본 구조 및 형식 변경)

## Create a table

### CREATE TABLE statement
- 테이블 생성

### CREATE TABLE syntax

- 각 필드에 적용할 데이터 타입(data type) 작성
- 테이블 및 필드에 대한 제약조건(constraints) 작성 

```sql
CREATE TABLE table_name(
    column_1 data_type,
    column_2 data_type,
    ...
);
```
```sql
-- 예시)

CREATE TABLE examples (
	examId INT AUTO_INCREMENT,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    PRIMARY KEY (examId)
);

SHOW COLUMNS FROM examples;

-- INT,VARCHAR(50) : 데이터 타입
-- NOT NULL, PRIMARY KEY : 제약 조건
-- AUTO_INCREMENT : 속성
-- SHOW COLUMNS FROM : 해당 TABLE 구조 확인
```
#### 대표적인 MySQL Data Types

- 숫자형 (Numeric) : INT, FLOAT, ...
- 문자형 (String) : VARCHAR, TEXT, ...
- 날짜형 (Date and Time) : DATE, DATETIME, ...

### Constraint (제약 조건)
- 데이터 무결성을 지키기 위해 데이터를 입력 받을 때 실행하는 검사 규칙

#### 대표적인 MySQL Constraint
- PRIMARY KEY
    - 해당 필드를 기본 키로 지정
- NOT NULL
    - 해당 필드에 NULL 값을 저장하지 못하도록 지정

### AUTO_INCREMENT attribute
- 테이블의 기본 키에 대한 번호 자동 생성
- 기본 키 필드에 사용 (고유한 숫자를 부여)
- 시작 값은 1이며 데이터 입력시 값을 생략하면 자동으로 1씩 증가
- 이미 사용한 값을 재사용하지 않음
- 기본적으로 NOT NULL 제약 조건을 포함

## Delete a table

### DROP TABLE statement
- 테이블 삭제

### DROP TABLE syntax
- DROP TABLE statement 이후 삭제할 테이블 이름 작성

```sql
DROP TABLE table_name;
```

## Modifying table fields

### ALTER TABLE statement
- 테이블 필드 조작 (생성, 수정, 삭제)
- ALTER TABLE ADD 필드 추가
- ALTER TABLE MODIFY 필드 속성 변경
- ALTER TABLE CHANGE COLUMN 필드 이름 변경
- ALTER TABLE DROP COLUMN 필드 삭제

### ALTER TABLE syntax

- ADD 키워드 이후 추가하고자 하는 새 필드 이름과 데이터 타입 및 제약 조건 작성
- MODIFY 키워드 이후 변경하고자 하는 필드 이름 그리고 데이터 타입 및 제약 조건 작성
- CHANGE COLUMN 키워드 이후 기존 필드 이름, 변경하고자 하는 필드 이름 그리고 데이터 타입 및 제약조건 작성
- DROP COLUMN 키워드 이후 삭제하고자 하는 필드 이름 작성

```sql
ALTER TABLE
    table_name
ADD
    new_column_name column_definition
MODIFY
    column_name column_definition
CHANGE COLUMN
    original_name new_name column_definition
DROP COLUMN
    column_name;
```

