
# Workbench 활용 가이드

- MySQL Workbench를 실행하고 새연결 만들기

1. MySQL Workbench를 다운로드하고 설치.
2. MySQL Workbench를 열고 MySQL Connections 옆의 + 기호 클릭.
3. Setup New Connection 창에서 Connection Name 부분에 연결용 이름을 입력.
4. Test Connection 버튼 클릭.
5. Connect to MySQL Server 창이 뜨면 설치 시 입력했던 Password 입력하고 OK 클릭
6. Setup New Connection 창이 뜨면 OK 클릭
7. 새로 연결된 MySQL Workbench가 실행된 화면을 확인 할 수 있다.

- Workbench에서 쿼리를 사용하는 방법 순서

1. 원하는 db선택
2. SQL아이콘 선택 (새 SQL 입력창 불러오기)
3. SQL 쿼리문 작성
4. 번개아이콘 선택 (쿼리 실행)
5. 결과 확인

- 문법 작성 순서
1. FROM :  조회 테이블 확인
쿼리의 가장 첫 번째 실행 순서는 FROM 절
FROM 절에서는 테이블의 모든 데이터를 가져온다.

2. WHERE : 데이터 추출 조건 확인
FROM절에서 읽어온 BS데이터중에서 조건에 일치하는 데이터만 가져온다.

3. GROUP BY : 컬럼 그룹화
WHERE 조건에서 읽어온 데이터를 선택한 컬럼으로 그룹화하여 단일 값으로 축소.

4. HAVING : 그룹화 조건 확인
항상 group by뒤에 위치하고 where 조건절과 마찬가지로 조건을 줄 수 있다. 
where 절은 기본적인 조건절로서 우선적으로 모든 필드를 조건에 둘 수 있지만 
having 절은 group by 된 이후 특정한 필드로 그룹화된 새로운 테이블에 조건을 줄 수 있다.

5. SELECT : 데이터 추출
여러 조건들을 처리한 후 남은 데이터에서 어떤 열을 출력할지 선택.

6. ORDER BY : 데이터 순서 정렬
마지막으로 행의 순서를 정렬.
