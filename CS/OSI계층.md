# OSI 7계층

## 계층 1 - 물리계층 Physical Layer
- 0과 1의 비트 정보를 회선에 보내기 위한 신호 변환
- 프로토콜
  - RS-232
- 전송 단위 : 비트
- 장비 : 허브, 리피터

## 계층 2 - 데이터 링크 계층 Data Link Layer
- 링크의 설정, 유지, 종료 담당 및 노드 간의 회선제어, 흐름제어, 오류제어
- 프로토콜
  - HDLC : 점대점 방식이나 다중방식 통신에 사용
  - PPP : 두 통신 노드 간의 직접적인 연결
- 전송 단위 : 프레임
- 장비 : 스위치, 브리지

## 계층 3 - 네트워크 계층
- 다양한 길이의 패킷을 네트워크들을 통해 전달하고 전송 계층이 요구하는 서비스 품질을 위한 수단을 제공하는 계층
- 프로토콜
  - IP : 송수신 간의 패킷 단위, 정보를 주고받는 데 사용하는 통신 프로토콜
  - ARP : IP네트워크 상에서 MAC 주소를 알기 위해서 사용, IP 주소를 MAC 주소로 변환
  - RARP : MAC 주소는 알지만 IP주소를 모르는 경우 서버로부터 IP주소를 요청하기 위해 사용
  - ICMP: 수신지 도달 불가 메시지를 통지하는 데 사용
  - IGMP: 화상회의, IPTV에서 활용되는 프로토콜
  - 라우팅 프로토콜 : 데이터 전송을 위해 목적지까지 갓 수 있는 여러 경로 중 최적의 경로를 설정해주는 상호 통신 규약
    - RIP : AS(자율 시스템)내에서 사용하는 거리벡터 알고리즘에 기초하여 개발된 내부 라우팅 프로토콜, 최초 라우팅 프로토콜, 벨만-포드 알고리즘, 15홉 제한, IGRP
    - OSPF : RIP의 단점 개선, 최단 경로를 찾는 프로토콜, 다익스트라 알고리즘, 홉 제한 없음, ELGRP
    - BGF : 자치 시스템(AS)간 경로 정보를 교환, 링크 상태 알고리즘 사용
    - 라우팅 알고리즘
      - 거리 벡터 알고리즘: 인접 라우터와 정보를 공유하여 목적지까지의 거라와 방향을 결정하는 알고리즘, 벨만포드 사용
      - 링크 상태 알고리즘: 링크상태 정보를 모든 라우터에 전달하여 최단경로 트리를 구성하는 알고리즘, 다익스트라 알고리즘사용
- 장비 : 라우터, L3스위치

## 계층 4 - 전송 계층 transport layer
- 상위 계층들이 데이터 전달의 유효성이나 효율성을 생각하지 않게 해주면서 종단간의 사용자들에게 신뢰성 있는 데이터를 전달하는 계층, 오류 제어 방식 사용
- 프로토콜
  - TCP (신연흐혼): 옥텟을 안정적이고, 순서대로 에러없이 교환할 수 있게 해줌
    - 신뢰성, 연결성, 흐름제어, 혼잡제어
  - UDP : 비연결성, 비신뢰성, 순서화되지 않은 데이터그램 서비스 제공
- 전송 단위 : 세그먼트
- 장비 : L4스위치

## 계층 5 - 세션 계층
- 프로세스들의 논리적인 연결, 응용 프로그램 간의 대화를 유지하기 위한 구조 제공, 연결이 끊어지지 않도록 유지 시켜주는 역할 수행

## 계층 6 - 표현 계층 Presentation Layer
- 정보를 통신에 알맞은 형태로 만듦, 하위 계층에서 온 데이터를 사용자가 이해할 수 있는 형태로 만듦. 부호교환, 암복호화
- 프로토콜
  - JPEG : 이미지
  - MPEG : 멀티미디어

## 계층 7 - 응용 계층 Application Layer
- 프로토콜
  - HTTP : 하이퍼텍스트 교환
  - FTP : 서버- 클라이언트 사이의 파일을 전송
  - SMTP : 이메일 보냄
  - POP3 : 원격 서버로부터 이메일 가져옴
  - IMAP :원격 서버로부터 이메일 가져옴
  - Telnet: 인터넷이나 로컬에서 네트워크 연결에 사용
- 장비 : L7스위치

### IPv4
- 32 비트
- 8비트씩 4부분으로 나뉜 10진수
- 유니캐스트, 멀티캐스트, 브로드캐스트

### IPv6
- 128 비트
- 16비트씩 8부분으로 나뉜 16진수
- 유니캐스트, 멀티캐스트, 애니캐스트

#### 4 → 6 전환 방법
- 듀얼 스택
- 터널링
- 주소변환

### 개발환경 인프라 구성 방식
- 온프레미스(On-Pramise)방식 : 외부 인터넷망이 차단된 상태에서 인트라넷 망만을 활용하여 개발환경을 구축하는 방식
- 클라우드(Cloud)방식 : 아마존, 구글, 마이크로소프트 등 클라우드 공급 서비스를 하는 회사들의 서비스를 임대하여 개발환경을 구축하는 방식
- 하이브리드 방식 : 온프레미스 + 클라우드

### 서킷 스위칭(Circuit Swiching)
네트워크 리소스를 특정 사용 층이 독점하도록 하는 통신 방식

### 애드 혹 네트워크(Ad-hoc Network)
노드들에 의해 자율적으로 구성되는 기반 구조가 없는 네트워크

### 패킷 스위칭(Packet Switching)
작은 블록의 패킷으로 데이터를 전송하며, 데이터를 전송하는 동안만 네트워크 자원을 사용하도록 하는 통신 방식

- X.25 : 통신을 원하는 두 단말장치가 패킷 교환망을 통해 패킷을 원활히 전달하기 위한 통신 프로토콜
- 프레임 릴레이 : ISDN을 사용하기 위한 프로토콜, ITU-T에 의해 표준으로 작성됨
- ATM(Asynchronous Transfer Mode) : 비동기 전송모드, 광대역 전송에 쓰이는 스위칭 기법