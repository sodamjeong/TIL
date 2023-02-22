# KDT 2기 12월 29일 학습내용
## Branch
 - 독립적인 작업흐름을 만들고 관리
 
### 브랜치 주요 명령어

1. 브랜치 생성 :
git branch branch name
2. 브랜치 이동 :
git checkout 생성한 branch name
3. 브랜치 생성 + 이동 :
git checkout -b branch name
4. 브랜치 목록 :
git branch
5. 브랜치 삭제 :
git branch -d branch name

### merge

```- git merge branch name```
- 각 branch 에서 작업을 한 이후 합치기 위 해 사용
- 서로 다른 버전(commit) 취합 시, 각자 다른 파일 수정 할 경우 충돌 없이 merge commit 생성
- 같은 파일을 수정 하여 충돌이 일어날 경우 적절하게 수정하여 commit 실행

```python
# git branch를 생성하고 작업 후 커밋 해야함.
# 작업 후 master branch로 이동 후 merge
```


## Git Flow
- git 그리고 branch를 활용하여 협업하는 전략
### github flow
 - github 에서 제안하는 branch 전략 기본 원칙
 1. master branch는 배포 가능한 상태여야 함.
 2. feature branch는 각 기능의 의도를 알 수 있게 작성.
 3. commit message 는 매우 중요하므로 명확하게 작성.
 4. pull request를 통해 협업 진행.
 5. master branch에 병합하여 작업한 작업물을 반영.

### github flow models
- shared repository model
    - 동일한 저장소를 공유하여 활용하는 방식

1. 관리자는 팀원을 초대해 collaborator에 등록한다. 이메일을 통해 초대수락하여 해당 저장소의 push 권한을 부여 받고 clone 하여 협업한다.

2. 별도의 branch를 생성하여 작업하고 commit, 해당 branch를 원격저장소에 push 한다.

3. github에서 pull request 버튼을 누르고 내용을 작성하여 PR 한다.

4. 관리자는 요청된 코드를 리뷰하고 판단하여 코멘트를 달거나 병합한다.(merge)

5. 이후 로컬에서 병합이 완료된 branch 는 삭제하고 병합된 master branch를 다시 pull하여 협업과정을 반복 한다.

- fork & pull model
    - push 권한이 없을 때 github 기반의 오픈소스 참여 과정에서 쓰이는 방식

1. 작업하고자 하는 원격저장소를 fork 한다.
복제본을 내 저장소로 가져옴으로써 로컬에서 작업 후 원격저장소로 push 할 수 있게 된다.

2. clone한다.(본인 저장소인지 확인 해야함)

3. github에서 pull request 버튼을 누르고 내용을 작성하여 PR 한다.

4. 관리자는 요청된 코드를 리뷰하고 판단하여 코멘트를 달거나 병합한다.(merge)
