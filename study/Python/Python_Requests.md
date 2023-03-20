# KDT 2기 1월 113일 학습내용
## Requests

- 파이썬을 통해 주소로 요청을 보내고 응답 결과를 파이썬으로 조작할 수 있는 외부 함수

    - `requests` 라이브러리를 활용한 API 요청 코드를 작성할 수 있다.
    - 응답 데이터의 구조를 분석해서 문제 해결에 적용할 수 있다.

```py

응용 예시 1.

import requests

url = "https://api.bithumb.com/public/ticker/BTC_KRW"
# 정보를 가지고 올 url (빗썸)
info = requests.get(url).json()
# 해당 url의 제이슨 형식의 정보를 가지고 옴
print(info['data']['prev_closing_price'])
# 가지고 온 정보중에 전일 종가 정보 출력
```

```py

응용 예시 2.

import requests
import os
from dotenv import load_dotenv

load_dotenv()
key = os.environ.get('api_key')
# dotenv 를 활용해 노출을 원하지 않는 값을 숨길 수 있다.

def popular_count():
    url = f'https://api.themoviedb.org/3/movie/popular'
    param = {
    'api_key' : {key}
    'language' : 'ko-KR',
    'region' : 'KR' 
  }
# params 를 이용해 url 뒤에 붙을 옵션 정보를 추가 할 수 있다.
    info = requests.get(url,params=param).json()  
    data = info['results']
    return len(data)

if __name__ == '__main__':
    print(popular_count())
```

## API

- Application Programming Interface
- 컴퓨터와 컴퓨터 프로그램 사이의 연결 일종의 소프트웨어 인터페이스 이며,<br/> 다른 종류의 소프트웨어에 서비스를 제공한다.

### API 활용시 확인 사항

- 요청하는 방식에 대한 이해
    - 인증 방식
    - URL 생성
    1. 기본 주소
    2. 원하는 기능에 대한 추가 경로
    3. 요청 변수 (필수와 선택)_옵션
- 응답 결과에 대한 이해
    - 응답 결과 타입(JSON)
    - 응답 결과 구조

    
[오늘 내용 참고 상세사항](https://requests.readthedocs.io/en/latest/)