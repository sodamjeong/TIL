# HTML,CSS_Basic
## Web page
- World Wide Web (WWW) : 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간
- Web site : 인터넷에서 여러개의 Web page가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간
- Web page : HTML, CSS, JavaScript등의 웹 기술을 이용하여 만들어진, 하나의 인터넷 문서
    - HTML : Structure, 웹 페이지의 구조 구축
    - CSS : Styling, 웹 페이지의 스타일 컨트롤
    - Javascript : Behavior, 웹 페이지 구성요소들의 동작을 변경할 수 있는 도구를 제공
## HTML
- HyperText Markup Language : 웹 페이지의 의미와 구조를 정의하는 언어
    -Hypertext : 웹 페이지를 다른 페이지로 연결하는 링크, 참조를 통해 다른 문서로 즉시 접근할 수 있는 텍스트
    -Markup Language : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어 (HTML,Markdown..)
### HTML Element
- 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성된다.<br>
```예시) <p>text</p>```
- 닫는 태그는 태그 이름 앞에 슬래시가 포함되며 닫는 태그가 없는 태그도 존재한다.(설정,이미지등) 
### HTML Attributes
1. 규칙
    - 요소 이름 다음에 바로 오는 속성은 요소 이름과 속성 사이에 공백이 있어야 함
    - 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
    - 속성 값은 열고 닫는 따옴표로 감싸야함<br>
    ```예시) <p class="editor-note">TEXT</P>```
2. 목적
    - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
    - CSS가 해당 요소를 선택하기 위한 값으로 활용됨
### HTML 문서의 구조
- <!DOCTYPE html> : 해당 문서가 html로 문서라는 것을 나타냄
- <html></html> : 전체 페이지의 콘텐츠를 포함
- <title></title> : 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
- <head></head> : HTML 문서에 관련된 설명, 설정 등.. 사용자에게는 보이지 않는다
- <body></body> : 페이지에 표시되는 모든 콘텐츠

### 대표적인 HTML Text structure
- Heading & Paragraphs : h1~6(헤드 사이즈), p(본문)
- Lists : ol(순서가 있는 리스트), ul(순서 없는 리스트), li(리스트)
- Emphasis & Importance : em(기울이기), strong(굵게)
```html
<!-- 예시 -->
<body>
    <h1>Main Heading</h1>
    <h2>Suv Heading</h2>
    <p>Text body</p>
    <p>Text <em>body</em></p>
    <p>Text <strong>>body</strong></p>
    <ol>
        <li>하나</li>
        <li>둘</li>
        <li>셋</li>
    </ol>
</body>
```
#### HTML 관련 사항
- HTML 요소 이름은 대소문자를 구분하지 않지만 소문자 사용을 권장
- HTML 속성의 따옴표는 '," 구분하지 않지만 "큰 따옴표" 권장
- HTML은 프로그래밍 언어와 달리 에러를 반환하지 않기 때문에 작성 시 주의
## CSS
- Cascading Style Sheet 웹 페이지의 디자인과 레이아웃을 구성하는 언어
### CSS 적용 방법
1. 인라인(Inline) 스타일
- body 해당 내용에 직접 적용
```html
<!-- 예시 -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1 style = "color: blue; background-color: yellow;">
    Hello World!</h1>
    <!-- 해당부분 스타일 지정 -->
</body>
</html>
```
2. 내부(Internal) 스타일 시트
- head에 정의
```html
<!-- 예시 -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style> /* style 정의 */
        h1 {
            color: blue; 
            background-color: yellow;
        }
    </style>
</head>
<body>
    <h1> Hello World!</h1>
</body>
</html>
```
3. 외부(Extenal) 스타일 시트
- 별도의 CSS 파일 생성 후 불러오기
```html
<!-- 예시 -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <!-- CSS파일 불러오기 -->
    <title>Document</title>
</head>
<body>
    <h1> Hello World!</h1>
</body>
</html>

<!-- style.css -->
<!-- 별도의 CSS 파일 생성-->

h1 {
    color: blue;
    background-color: yellow;
}
```

### CSS Selectors
- HTML 요소를 선택하여 스타일을 적용할 수 있도록 함

### CSS Selectors 종류
- 기본 선택자
    - 전체(*) 선택자<br>
        : 전체 
    - 요소(tag) 선택자<br>
        : 지정한 모든 태그를 선택
    - 클래스(class) 선택자<br>
        : 주어진 클래스 속성을 가진 모든 요소를 선택 <br>
        ex) .index는 class="index"를 가진 모든 요소를 선택
    - 아이디(id) 선택자<br>
        : 주어진 아이디 속성을 가진 요소 선택 아이디를 가진 요소가 하나만 있어야 한다.<br>
        ex) #index 는 id="index"를 가진 요소를 선택
    - 속성(attr) 선택자
- 결합자 (Combinators)
    - 자손 결합자(""(space))<br>
        : 첫 번째 요소의 자손 요소들 선택(하위 레벨 상관 없이)<br>
        ex) p span은 ```<p>``` 안에 있는 모든 ```<span>```를 선택
    - 자식 결합자(>)<br>
        : 첫 번째 요소의 직계 자식만 선택(한단계 아래 자식들만)<br>
        ex) ul > li 은 ```<ul>``` 안에 있는 모든 ```<li>```를 선택

### CSS 우선순위
- 동일한 우선순위 일 때 CSS에서 마지막에 나오는 규칙이 사용된다.
```html
h1 {
    color: red;
}

h1 {
    color: blue;
}
<!-- blue 적용됨 -->
```
- 우선 순위가 높은 순서
1. Importance (!important)
    - 모든 우선순위 점수 계산을 무효화하고 가장 높은 우선순위 특수한 경우가 아니라면 사용되지 않는다.
2. 우선 순위
    - 인라인 스타일 > id 선택자 > class 선택자 > 요소 선택자
3. 소스 코드 순서

### 상속
- 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속함<br>
이를 이용해 코드의 재사용성을 높인다.
    - 상속 되는 속성 : Text 관련 요소(font,color,text-align), opacity, visibility 등..
    - 상속 되지 않는 속성 : Box model 관련 요소(width,heigh,margin,padding,border,box-sizing,display),<br>
    position 관련 요소(position,top/right/bottom/left/,z-index)등