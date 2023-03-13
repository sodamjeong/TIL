# Box & Positioning
## Box Model
- 모든 HTML 요소를 박스로 표현
- 박스에 대한 크기, 여백, 테두리 등의 스타일을 지정하는 디자인 개념 (CSS)

### BOX의 구성
- Margin : 이 박스와 다른 요소 사이의 공백, 가장 바깥쪽 영역
- Border : 콘텐츠와 패딩을 감싸는 테두리 영역
- Padding : 콘텐츠 주위에 위치하는 공백 영역
- Content : 콘텐츠가 표시되는 영역

### BOX구성의 방향 별 명칭
- width : 폭
- height : 높이
- left : box 구성의 왼쪽 구역, 해당 영역이 커질 수록 오른쪽으로 이동하게 된다.
- right : box 구성의 오른쪽 구역, 해당 영역이 커질 수록 왼쪽으로 이동하게 된다.
- top : box 구성의 상단 구역, 해당 영역이 커질 수록 하단으로 이동하게 된다.
- bottom : box 구성의 하단 구역, 해당 영역이 커질 수록 상단으로 이동하게 된다.

### box-sizing
- content-box : 폭(width)과 높이(height)의 범위는 내용 영역에 한정. 패딩(padding)과 보더(border)는 그 폭과 높이에 포함되지 않고, 다른 폭과 높이가 됨. content-box는 초기 값으로, 요소의 크기는 width, padding, border로 계산
- border-box : 내용 영역의 폭(width)와 높이(height)는 패딩(Padding)과 보더(Border)를 포함한 범위.

## Position
- Normal Flow에서 요소를 끄집어내서 다른 위치로 배치하는 것.
- CSS Position은 전체 페이지에 대한 레이아웃을 구성하는 것이 아닌 페이지 특정 항목의 위치를 조정하는 것.

### Position 유형
- static
    - 기본값
    - 요소를 Normal Flow에 따라 배치
- relative
    - 요소를 Normal Flow에 따라 배치
    - 자기 자신을 기준으로 이동
    - 요소가 차지하는 공간은 static 일 때와 같다.
- absolute
    - 요소를 Normal Flow에서 제거
    - 가장 가까운 relative 부모 요소를 기준으로 이동
    - 문서에서 요소가 차지하는 공간이 없어짐
- fixed
    - 요소를 Normal Flow에서 제거
    - 현재 화면 영역을 기준으로 이동
    - 문서에서 요소가 차지하는 공간이 없어짐
- sticky
     - 요소를 Normal Flow에 따라 배치
     - 가장 가까운 block 부모 요소를 기준으로 이동
     - 요소가 특정 임계점에 스크롤 될 때 그 위치에서 고정됨
     - 만약 다음 sticky 요소가 나오면 다음 요소가 이전 요소의 자리를 대체

### Z-index
- 요소가 겹쳤을 때 어떤 요소 순으로 위에 나타낼지 결정
- z-index : 정수 / 정수 값을 사용해 순서를 지정 
- 정수 값이 더 큰 요소가 앞으로 온다.