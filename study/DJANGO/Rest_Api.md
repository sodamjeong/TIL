# REST API

## REST
- Representational State Transfer의 약자로 자원을 이름으로 구분하여 해당 자원의 상태를 주고받는 모든 것을 의미
  - HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고,
  - HTTP Method(POST, GET, PUT, DELETE, PATCH 등)를 통해
  - 해당 자원(URI)에 대한 CRUD Operation을 적용 
  - Create : 데이터 생성(POST), Read : 데이터 조회(GET), Update : 데이터 수정(PUT), Delete : 데이터 삭제(DELETE)

### REST 구성요소

1. 자원(Resource) : HTTP URI
2. 자원에 대한 행위(Verb) : HTTP Method
3. 자원에 대한 행위의 내용 (Representations) : HTTP Message Pay Load

### REST 장단점

1. 장점 
- HTTP 프로토콜의 인프라를 그대로 사용 REST API 사용을 위한 별도의 인프라 구출 필요 없음
- HTTP 프로토콜의 표준을 최대한 활용하여 여러 추가적인 장점을 함께 가져감
- HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능
- Hypermedia API의 기본을 충실히 지키면서 범용성을 보장
- REST API 메시지가 의도하는 바를 명확하게 나타내므로 의도하는 바를 쉽게 파악 할 수 있음
- 여러 가지 서비스 디자인에서 생길 수 있는 문제를 최소화
- 서버와 클라이언트의 역할을 명확하게 분리
 
2. 단점 
- 표준 자체가 존재하지 않아 정의 필요
- HTTP Method 형태가 제한적
- 브라우저를 통해 테스트할 일이 많은 서비스라면 쉽게 고칠 수 있는 URL보다 Header 정보의 값을 처리해야 하므로 전문성이 요구됨
- 구형 브라우저(익스폴로어)에서 호환이 되지 않아 지원해주지 못하는 동작이 많다

## API
- Application Programming Interface의 약자
- 응용 프로그램에서 사용할 수 있도록, 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스
- 주로 파일 제어, 창 제어, 화상 처리, 문자 제어 등을 위한 인터페이스를 제공

## REST API
- REST API란 REST의 원리를 따르는 API를 의미

### REST API 설계 규칙

1. URL은 동사보다는 명사를, 대문자보다는 소문자를 사용
2. 마지막에 슬래시(/)를 포함하지 않음
3. 언더바 대신 하이픈
4. 파일확장자는 제외
5. 행위 제외

### REST API 응답 상태 코드

- 1XX : 전송 프로토콜 수준의 정보 교환
- 2XX : 클라이언트 요청이 성공적으로 수행됨
- 3XX : 클라이언트는 요청을 완료하기 위해 추가적인 행동을 취해야 함
- 4XX : 클라이언트의 잘못된 요청
- 5XX : 서버쪽 오류로 인한 상태코드