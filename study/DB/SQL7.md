# SQL_Advanced
## Transactions
- 여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방법
- 다 성공 혹은 다 실패 해야하는 작업 
- ex) 계좌이체 - 인출 이후 입금이 안되면 처음부터 없었던 거래로 만들어야 한다.

### Transaction Syntax
- START TRANSACTION
    - 트랜잭션 구문의 시작을 알린다.
- COMMIT
    - 모든 작업이 정상적으로 완료되면 한꺼번에 DB에 반영
- ROLLBACK
    - 부분적으로 작업이 실패하면 모든 연산을 취소하고 실행 전으로 되돌림
```sql
START TRANSACTION;
state_ments;
... -- 변경 할 사항 입력
[ROLLBACK|COMMIT]; 

-- Mysql은 자동으로 commit 됨으로 
-- SET autocommit = 0 입력하여 해당 기능을 off 해야한다.
```

```sql
-- 예시
START TRANSACTION;

INSERT INTO users (name)
VALUES ('DAMI'),('DAM');

ROLLBACK;|COMMIT;

SELECT * FROM users;

-- ROLLBACK 일 경우 삽입 명령이 임시 데이터이기 때문에 명령문 실행 이전 테이블로 조회 된다.

-- COMMIT 일 경우 임시데이터가 DB에 반영되어 해당 값이 삽입된 결과가 조회 된다.
```

## Triggers
- 특정 이벤트에 대한 응답으로 자동으로 실행 되는 것
### Triggers Syntax
- CREATE TRIGGER 키워드 다음에 생성하려는 트리거의 이름을 지정
- 각 레코드의 어느 시점에 트리거가 실행 될 지 지정(삽입,수정,삭제 전/후)
- ON 키워드 뒤에 트리거가 속한 테이블의 이름을 지정
- 트리거가 활성화 될 때 실행할 코드를 TRIGGER_BODY에 지정
    - 여러 명령문을 실행하려면 BEGIN END 키워드로 묶어서 사용
```sql
[DELIMITER //] -- //은 다른 기호로 입력 가능
CREATE TRIGGER trigger_name
{BEFORE|AFTER} {INSERT|UPDATE|DELETE}
ON table_name FOR EACH ROW
[BEGIN] -- 명령문이 여러개 일 경우
trigger_body; -- DELIMITER 를 사용하여 명령문 마다 끝에 ;를 사용
...;
...;
[END//]
[DELIMITER;]
```

- SHOW TRIGGERS; (트리거 목록 확인)
- DROP TRIGGER trigger_name; (해당 트리거 삭제)

```sql
-- 예시
DELIMITER//
CREATE TRIGGER mytrigger
    BEFORE UPDATE
    ON users FOR EACH ROW
BEGIN
    SET NEW.updatedAt = CURRENT_TIME();
END//
DELIMITER ;
-- users 테이블에 업데이트를 하면 업데이트한 행의 updatedAt속성의 시간을 최신 시간으로 변경한다.
```
```sql
-- 예시 2
DELIMITER//
CREATE TRIGGER recordLogs
    AFTER INSERT -- users 테이블에 튜플이 삽입되면
    ON users FOR EACH ROW
BEGIN
    INSERT INTO usersLogs (description, createdAt) 
    -- usersLogs 테이블의 열(속성)
    VALUES('글이 작성 되었습니다', CURRENT_TIME());
    -- usersLogs 테이블에 글이 작성되었다는 내용과 작성 시간이 삽입됨.
END//
DELIMITER ;
