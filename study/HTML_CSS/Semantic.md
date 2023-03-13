# Semantic Web
- 웹 데이터를 의미론적으로 표현하고 연결하는 개념
## HTML Semantic Element
- 기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소 
- 검색엔진 및 개발자가 웹 페이지의 콘텐츠를 이해하기 쉽게 만들어줌
- 시각 장애 사용자가 스크린 리더기로 웹 페이지를 사용할 때 추가적으로 도움이 됨
### 대표적인 페이지 구조화를 위한 semantic element
- header : 헤더
- nav : 네비게이션
- main : 메인 공간
- article : 본문의 주 내용이 들어가는 공간
- section : 본문의 여러 내용(article)을 포함하는 공간
- aside : 사이드에 위치하는 공간
- footer : 푸터

## OOCSS
- Object-Oriented CSS
- 객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론

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
        /* 기본 카드 구조 */
        .card {
            border : 1px solid black;
            border-radius: 5px;
            padding: 1rem;
        }

        /* 카드 제목 */
        .card-title {
            font-size: 1rem;
            font-weight: bold;
        }

        /* 카드 내용 */
        .card-description {
            font-size: 0.7rem;
        }

        /* 기본 버튼 구조 */
        .btn {
            padding: 1rem;
            cursor: pointer;
        }

        .bg-red {
            background-color: crimson;
        }
        
        .bg-blue {
            background-color: lightblue;
        }

    </style>
</head>
<body>
    <div class="card">
        <p class="card-title">Card Title</p>
        <p class="card-description">This is a card description.</p>
        <button class="btn bg-red">Learn More</button>
        <button class="btn bg-blue">Learn More</button>
    </div>
</body>
</html>
```
## BEM
- Block Element Modifier
- 블록, 요소, 수정자를 사용해 클래스 이름을 구조화 하는 방법론

```html

.block {}
- 문단 전체에 적용된 요소 또는 요소를 담고 있는 컨테이너
- 재사용 가능한 독립적 블록, 가장 바깥쪽 상위요소
- 재사용을 위해 margin 또는 padding 을 적용하지 않음

.block__element{}
- block이 포함하고 있는 한 조각
- 블록을 구성하는 종속적인 하위 요소

.block--modifier{}
- block 또는 element의 속성

```

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
        /* Block */
        .card {
            display: flex;
            flex-direction: column;
        }

        /* Element */
        .card__title {
            font-size: 2rem;
        }

        .card__list {
            margin: 0;
        }

        .card__button {
            font-size: 1rem;
            padding: 1rem;
            cursor: pointer;
        }

        /* Modifier */
        .card__list--none {
            list-style: none;
        }

        .card__button--red{
            background-color: crimson;
        }

    </style>
</head>

<body>
    <div class="card">
        <h2 class="card__title">제목</h2>
        <ul class="card__list">
            <li class="card__list--none">항목 1</li>
            <li class="card__list--none">항목 2</li>
        </ul>
        <button class="card__button card__button--red">버튼</button>
    </div>
</body>
</html>
```
- 클래스를 만들 때 가장 중요한 부분은 클래스 이름이 무엇을 나타내는지 분명하게 전달 할 수 있는가에 대한 것

### OOCSS & BEM 의 목적
- 재사용 가능한 모듈로 분리함으로 써 유지보수성과 확장성을 향상 시키고 개발자 간의 협력이 향상되어 공통 언어와 코드이해를 확립