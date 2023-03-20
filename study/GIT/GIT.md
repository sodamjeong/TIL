# KDT 2기 12월 27일 학습내용

## 1. MARKDOWN
- markdown 해당 내용 별도 폴더로 작성

## 2. CLI
 ### CLI란 ?
 
```python
# 커맨드 라인 인터페이스 (명령어 인터페이스)

가상터미널 또는 텍스트 터미널을 통해 사용자와
컴퓨터가 상호작용 하는 방식

그래픽 기반의 인터페이스(GUI) 와 다른
명령 기반의 인터페이스
```
### CLI를 제공하는 프로그램(명령줄 해석기,셸)
   - 유닉스셸(sh, ksh, csh, tcsh, bash)과 CP/M, 도스의 command.com("명령 프롬프트")등..

### 기초 파일 시스템 명령어
 - **pwd** (print working directory) : 현재 디렉토리 출력
 - **cd 파일명**(change directory) : 디렉토리 이동
    - cd . : 현재 디렉토리, cd .. : 상위 디렉토리
- **ls**(list) : 목록
- **mkdir**(make directory) : 디렉토리 생성
- **touch** : 파일 생성
- **rm 파일명**(remove) : 파일 삭제
    - **rm -r 폴더명** : 폴더 삭제

## 3. GIT
### GIT란?
```- 분산버전관리시스템으로 코드의 버전을 관리하는 도구```

\- 2005년 리눅스 커널을 위한 도구로 리누스 토르발스가 개발

```- 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 파일들의 작업을 조율할 수 있어 협업이 가능하다```

### 버전 기록
1. **git init** : 특정폴더에 .git 폴더 생성 (git bash에서 (master)표기가 되는 것을 볼 수 있다.)
2. **작업(수정) 활동** : working directory
3. **git add** : staging area에 commit 할 파일을 모음
4. **git commit -m '버전이름'** : 버전으로 기록
```python
# 이름 지정시 변경 사항을 확인 할 수 있도록 명확하게 작성 해야함.
```
### 버전 관리

- git은 데이터를 파일 시스템의 스냅샷으로 관리하고 크기가 매우 작다.
- 파일 변경 사항이 없으면 새로 저장하지 않는다.

    ```
    ver1 : file a + file b + file c
  file a, file b, file c 내용 수정
  git add file a
  git add file c
  git commit -m 'ver2'
  -> ver2 : file a1 + file b + file c1
  
  git add file b
  git commit -m 'ver3'
  -> ver3 : file a1 + file b1 + file c1
  ```

### 현재 상태 명령어
- **git log** : 현재 저장소에 기록된 commit 조회
    
    - 다양한 옵션을 통해 로그 조회 가능

     ex) git log -1, git log --oneline, git log -2 --oneline..

- **git status** : git 저장소에 있는 파일 상태 확인 
    - untracked : 버전으로 관리된 적 없는 파일
    (untracked files) - 새로만든 파일
    - tracked : 버전으로 관리되고 있는 파일
    - unmodified : git status에 나타나지 않음
    - modified : 변경사항있으나 commit 되기 위해 add 되지 않은 상태 (changes not staged for commit)
    - staged : commit 되기 위해 add 된 상태 
    (changes to be committed)
    - Noting to commit, working tree clean : 모두 commit 됐고 작업 중인 파일 없음

### GIT config 
```python
# 필수 설정 정보

- 사용자 정보 (commit author) : commit 하기 위해 반드시 필요함.

1. git config --global user.name "유저네임"
2. git config --global user.email "email"

- 설정 확인 방법

* git config -l
* git config --global -l
* git config user.name

