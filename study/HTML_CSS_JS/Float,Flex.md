# Float & Flex
## CSS Float
- 요소를 띄워서 텍스트 및 인라인 요소가 그 주위를 감싸도록 하는 배치
- 왼쪽 혹은 오른쪽으로 띄워 Normal flow에서 벗어남
- 텍스트 열 내부에 떠다니는 이미지를 포함하면서도 해당 이미지의 좌우에 텍스트를 둘러싸는 간단한 레이아웃을 구현하기 위해 도입 되었다.
- Float는 원래 탄생 목적에서 더 나아가 웹 페이지 전체 레이아웃을 구성하는데 사용되었으나, Flex와 Grid의 등장으로 인해 다시 원래의 목적으로 돌아갔다.

```html
<!-- 예시 -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .box {
            width : 10rem;
            height : 10rem;
            border : 1px solid black;
        }            
        .float-left {
            float : left;
        }
        .float-right {
            float : right;
        }
    </style>
<body>
    <div class="box float-left">float left</div>
    <div class="box float-right">float right</div>
</body>
```

## CSS Flexbox
- 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식

### Flexbox 기본사항
- main axis(주 축)
    - flex item들이 배치되는 기본축
- cross axis(교차 축)
    - main axis에 교차되는 축
- Flex Container
    - display : flex; 혹은 display : inline-flex;가 설정된 부모 요소
    - 해당 컨테이너의 1차 자식 요소들이 Flex item이 됨
    - flexbox 속성 값들을 사용하여 자식 요소 flex item들을 배치
- Flex Item
    - Flex Container 내부에 레이아웃 되는 항목

### Flexbox 속성
- Flex Container 관련 속성
    - display
    - flex-direction
    - flex-wrap
    - justify-content
    - align-items
    - align-content

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
    <style>
        .container {
            height: 500px;
            border: 1px solid black;
            display: flex;

            /* 나열되는 방향을 지정*/
            flex-direction: row; /*행으로 나열*/
            flex-direction: column; /* 주 축 변경*/
            /* -reverse 시작 선과 끝 선이 서로 바뀜*/
            flex-direction: row-reverse; 
            flex-direction: column-reverse;
            
            /* flex item 목록이 flex container의 하나의 행에
             들어가지 않을 경우 다른 행에 배치할지 여부 설정
             화면 너비를 줄여서 확인 할 수 있다.*/
            flex-wrap: wrap;
            flex-wrap: nowrap;

            /* 주축 정렬 */
            justify-content: center;
            justify-content: flex-start;
            justify-content: flex-end;
            justify-content: space-between;
            justify-content: space-around;
            justify-content: space-evenly;
            
            /* 교차축 정렬 */
            align-content: flex-start;
            align-content: center;
            align-content: flex-end;
            align-content: space-between;
            align-content: space-around;
            align-content: space-evenly;

            /* 교차축을 따라 flex item 행을 정렬*/
            align-items: stretch;
            align-items: flex-start;
            align-items: center;
            align-items: flex-end;
        }

```

- Flex Item 관련 속성
    - align-self
    - flex-grow
    - flex-shrink
    - flex-basis
    - order

``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
    <style>
        .container {
            height: 500px;
            border: 1px solid black;
            display: flex;
        }

        .item {
            /* 교차 축을 따라 개별 flex item을 정렬*/
            align-self : stretch;
            align-self : flex-start;
            align-self : center;
            align-self : flex-end;
            
            /* 남는 행 여백을 비율에 따라 각 flex item에 분배
            flex-grow의 반대는 flex-shrink
            (넘치는 너비를 분배해서 줄임) */
            flex-grow : 1;

            /*flex item의 초기 크기 값을 지정
            flex-basis와 width 값을 동시에 적용한 경우
            flex-basis가 우선*/
            flex-basis : 300px;
            
        }
```
- justify-items 및 justify-self 속성은 없다.(margin을 통해 정렬 및 배치)


