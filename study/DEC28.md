# KDT 2기 12월 28일 학습내용

 ## GITHUB
 - 원격저장소를 제공하는 서비스
 - git, github 모두 버전을 관리한다.

### 원격저장소 연결하기
1. github 사이트에서 저장소를 만든다.
2. 저장소 URL을 확인한다.
3. git remote add origin url (명령어입력)
4. git remote -v (원격저장소 정보확인)
* url 잘못 입력시 - git remote rm origin

```python
# origin - 원격저장소 이름 (통상 origin 사용)
```

### 원격저장소에 업로드 하기

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

### 원격저장소에서 다운로드 하기
변경이 반영된 파일을 가지고 와서 작업
가장 최근 버전의 파일이 반영된다.

- $ git pull origin master
- $ git pull <원격저장소><브랜치이름>


