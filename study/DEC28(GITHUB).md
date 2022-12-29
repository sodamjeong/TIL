# KDT 2기 12월 28일 학습내용

 ##  GITHUB
 - 원격저장소를 제공하는 서비스
 - git, github 모두 버전을 관리한다.

### 1. 원격저장소 연결하기
1. github 사이트에서 저장소를 만든다.
2. 저장소 URL을 확인한다.
3. git remote add origin url (명령어입력)
4. git remote -v (원격저장소 정보확인)
* url 잘못 입력시 - git remote rm origin

```python
# origin - 원격저장소 이름 (통상 origin 사용)
```

### 2. 원격저장소에 업로드 하기

원격저장소는 파일,폴더가 아닌 버전을 관리

-  $ git push origin master (명령어)
-  $ git push <원격저장소이름><브랜치이름>
``` bash
$ git push origin master
Enumerating objects: 17, done.
Counting objects: 100% (17/17), done.
Delta compression using up to 8 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (17/17), 138.97 KiB | 11.58 
MiB/s, done.
Total 17 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.       
To https://github.com/sodamjeong/TIL.git
 * [new branch]      master -> master
 ```
  ```-원격저장소로 push 한 모습```

### 3. 원격저장소에서 다운로드 하기
변경이 반영된 파일을 가지고 와서 작업.

가장 최근 버전의 파일이 반영된다.

- $ git pull origin master
- $ git pull <원격저장소><브랜치이름>

```brush
$ git pull origin master 
From https://github.com/sodamjeong/TIL
 * branch            master     -> FETCH_HEAD     #해당 url에서 가지고옴
Already up to date. # 이미 불러져있는 상태
```
```-원격저장소로 pull 한 모습```

프로젝트에 참여하고 싶을 때

1. 해당 프로젝트의 원격저장소 주소를 확인
2. git clone 원격저장소주소 (명령어입력)

```-이전버전까지 확인이 가능하여 협업하여 프로젝트를 진행 할 수 있다.```

### 4. push conflict
협업 시, 로컬과 원격저장소의 버전이 다른 경우가 발생할 때가 있다.

- 해결 방법
1. 원격저장소의 마지막 버전을 pull 해온다.
2. 로컬에서 두 버전을 합친다.
3. 다시 원격저장소로 push

### 5. gitignore

- 버전관리와는 상관이 없는 파일 관리
- .gitignore 파일을 생성하고 해당 내용을 관리한다

ex) 개인정보 및 비밀, 개발자에게만 필요한 내용
 - 특정 파일 : a.txt (a라는 모든 텍스트 파일), study/a.txt (study폴더의 a.txt)
- 특정 폴더 : /폴더명
- 특정 확장자 : *.exe (exe확장자인 모든 파일)
    - 예외처리 : !b.exe (b 파일은 예외)

```python
# 이미 커밋된 파일에는 적용 되지 않으니 프로젝트 시작전에 미리 꼭 설정 해야한다
```
```-일반적으로 ignore하는 파일 ```
- 개발 언어 ex)파이썬,자바...
- 개발 환경 ex)운영체제(window, mac...),텍스트 에디터/IDE(VS CODE...)
- https://www.toptal.com/developers/gitignore/
에서 간단히 확인할 수 있다.  

