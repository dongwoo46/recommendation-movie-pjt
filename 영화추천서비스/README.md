# 팀원 정보 및 업무 분담 내역
1. 김동우 / 석민혁 
   - 서로 번갈아 가면서 네비게이터와 드라이버 역할을 수행
   - django와 vue 구현
   - 모델, serializer, views django에서 같이 구현
   - vue를 통해 화면 출력

김동우 : vue css /  석민혁: django 커뮤니티 추가 기능 구현 및 프로필 이미지 

# 목표 서비스 구현 및 실제 구현 정도
2. 목표 서비스 구현 
   - community에서 각각의 특색있는 게시판으로 사람끼리 소통
   - profile에서 다른 유저들의 정보를 얻기
   - profile에서 유저들의 댓글 달기기능
   - 영화 디테일에서 유저들의 리뷰 달기 기능
   - 장르별로 영화 추천
   - 프로필에 이미지 넣기
   - 

# 데이터 베이스 모델링



# 영화 추천 알고리즘에 대한 기술적 설명
- 영화 장르별로 분류해서 영화 추출


# 서비스 대표 기능에 대한 설명
## 왜 구현하였는가? 
- 영화 진흥원에 따른 데이터를 보았을 때 코로나 이후 영화관의 관객 수가 줄어듦
  코로나가 종식되고도 회복되지 않음
  -> 그 이유가 무엇일까? ->
 영화는 사람들이랑 같이 보는 사람들이 많은데 코로나 이후 ott서비스나 다른 사람들과의 관계가 끊어짐에 따라 영화를 볼 사람이 없음
 -> 솔로도 증가 

 따라서 사람들과의 만남 소통이 필요함!!

 ### 서비스 기능
 - 커뮤니티를 여러개로 나눠서 해당 게시판의 목적에 맞는 글을 올려서 소통함
 - 사람들의 참여를 높임
- 프로필에 사람들의 개개인의 정보를 넣어서 유저들이 다른 유저들의 정보를 보면서 다른 사람에 대한 정보를 get
-  관심있는 사람들을 팔로우 언팔로우해서 나중에도 연락할 수 있도록
-  프로필에 이미지를 띄워서 자신을 표현 할 수 있도록
-  프로필에도 댓글을 달아서 특정인물에게 자신을 어필 할 수 있도록


# 기타
1. 느낀점 - 김동우
   하루에 코딩을 최소 12시간씩 컴퓨터만 보고 있었더니 눈알이 빠질거같다 하지만 페어 프로그래밍 하면서 소통을 통해 모르는 부분을 동료가 같이 잡아주고 어려운 부분을 얘기하면서 정보를 나누니 즐겁다.

2. 











# 목적
- 영화 추천
- 영화 취향 맞는 사람 찾기
- 같이 영화 볼 사람 구인
## 무엇을 어떻게 왜?
무엇을 -> 영화추천과 사람구인 / 미공개 스틸컷 보기
어떻게 -> 모임게시판과 쪽지보내기로 or 특별 코스프레 감상
왜 -> 영화는 혼자보기 심심함/ 이용자를 모으기 위해(트래픽 올리기)    

# 기본 기능
- 로그인 & 로그아웃 & 회원가입 & 회원탈퇴
- 영화 검색
- 박스오피스 랭킹순 영화 추천
- 장르별 영화 추천
- 커뮤니티


# 추가 기능
## 영화
- 조회 수, 댓글 수에 따른 영화 랭킹 (ex : top10) (하)
- 영화 위시 리스트 (중)
  - 영화 디테일에서 위시리스트 버튼을 클릭하면 유저 위시리스트에 자동 등록
  - 새로고침해도 없어지지 않도록 localStorage에 넣기
  - 홈페이지에 유튜브 예고편

## 프로필
- 회원탈퇴기능
    - 회원탈퇴 시도시 경고 알림!!

- 유저 프로필(사진, 성별, 인적사항) => 공개 비공개 가능 (중)
  - 자기소개(인스타링크, 액션좋아합니다 저랑 같이 보실분?)
  - 자기가쓴 댓글, 게시글 목록 보여주기  

- 유저 랭킹 (중)
  - 경험치에 따라 랭킹 메기기
  - 유저 (친구, 친구 추천)기능, 커뮤니티 이용 등 경험치와 코인 획득
  
- 랭커 사용자에게 아이콘 로고 입력 및 닉네임 색 변경
  - 별달아주기(챌린져처럼)

- 유저 프로필 잔디 기능 (상)
  - 백준 스택쌓아서 30일연속이면 코인주기 (일주일 한달 두달 석달... 1년지나면주고 리셋)


## 커뮤니티
- 번개 모임 게시판 (모임 형성시 포인트 획득) (하)
  - 게시판 이름만 정하기  
- 활동량에 따른 유저 레벨
  - 경험치 주기
- 익명기능
  - 온오프 하기
- 포인트로 1:1 채팅 신청 기능 or (쪽지 보내기 기능) (상)
  - django-messages 사용 (https://django-messages.readthedocs.io/en/latest/)
    - 만약 구현 못하면 코인은???? ->  구독서비스로 사진을 보여줌(사진갤러리를 따로 만들어야함 일정량의 코인은 현금으로 교환 + 캐시샵 )
# 페이지 구조
- Home
  - movie_detail -> 영화 클릭 시 
  - community -> 유저가 게시판 생성 가능하도록 (게시판 안에 게시판 만들어버리기)
    - 게시판
    - 게시판
    - 게시판
      - 유저가 쓴 글
  - logout
- login - 창으로 만들기 
  - 로그인을 안하면 게시글/댓글 작성 불가 (로그인을 안하고 댓글 작성시도시 로그인페이지로 이동) ps) 로그인 안해도 볼수는 있음
- signup 
  - 로그인 되어 있으면 숨기기
- 게임페이지
  - 숫자카드? 골라서 값이 큰 쪽이 이기기 
  - 자기가 가지고 있는 코인을 얼마 넣을지 정해서 이긴쪽이 가저감 
  - 코인이 없으면 코인을 가져오라는 경고창띄우기

- Profile
  - 인적사항
  - 친구 / 친구 추천
  - 코인
  - 자기가 쓴 게시글, 댓글


# 디자인
배경 - 검은색
글자 색 - 나중에 rgb로 고르기
영화추천 - 슬라이드형태

디테일 -> 평점 , 포스터 , 제목, 리뷰댓글, TMDB링크 더보기, 등장인물(출연배우)


fontawesome : https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css
bootstarp : 
```python
npm install vue bootstrap-vue bootstrap

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
```

# loadash
[vue lodash 쓰는법]

아래 명령어를 써서 lodash를 깔아주기
$ npm i -g npm
$ npm i --save lodash

script 상단에 아래의 코드를 넣어주기
import _ from 'lodash'


# 토큰
npm install vuex-persistedstate

# axios
npm install axios


# 나중에 구현할 내용
로그인시 비밀번호 *로 출력

# 덤프 데이터 생성
$ python manage.py dumpdata -- indent 4 articles.article > articles.json


# 2023-05-18 계획
- 화면 전체 검정색으로 채우기 (완)
- navbar 꾸미기 (로그인시 이름 및, 사진 출력) (완)
- 어플리케이션 로고 왼쪽 상단에 삽입 (완)
- profile 페이지 꾸미기 (내용 추가) (완)


# 2023-05-19 계획
- Login, Signup 폼으로 구현 (완)
- Django에서 게시글 생성 기능 구현 (완)
- 영화 상세정보에 유튜브 예고편 영상 삽입
  - articles(제목-> 게시판 이름)-article(제목, 내용)-comment
- 영화 디테일에 comment 달기 기능 


- 영화 디테일 하트 토글형식으로 바꾸기
- django로 like moive 만들기
- 프로필 사진 업로드 비동기화 -> 동기화로 바꾸기
- 프로필 이미지 디폴트 데이터 추가


Community
- CommunityView.vue : 게시판
- CreateView : 게시판 생성

- BoardView.vue : 게시글
- BoardCreate.vue : 게시글 생성

- BoardDetailView.vue : 게시글 상세 정보

Components
- ArticleList : 게시판 목록
- ArticleListItem : 단일 게시판

- BoardList : 게시글 목록
- BoardListItem : 단일 게시글

# 개선
- 로그인 비동기화 -> 동기화로 변경
- API KEY : .env.local로 사용, django API_KEY -> git에 안 올라가게

# 2023-05-23 계획
- 영화 디테일 review에 유저 정보 가져와서 사용
- 커뮤니티 구현
- 프로필 구현 (DB에 저장된 데이터 가져와서 사용 및 post로 DB 수정)
  - 수정 폼에서 기존 데이터 default값으로 설정


# 야근 할 것
- 커뮤티니 게시판, 게시물, 댓글 구현
  - django에 댓글 모델, 함수 구현
  - 게시판(CommunityView), 게시판생성(CreateView)
    - 게시물(BoardView), 게시물생성(CreateBoardView) - 제목 / 내용 / 댓글 수 / 유저이름
      - 댓글(CommentView), 댓글생성(form으로 구현, MovieDetail 참고) - 댓글(유저명)
  - CommunityView(detail) -> BoardView -> BoardView(detail) -> CommentView
- 프로필 DB와 연결 (django의 accounts model 및 serializer)
- 영화 디테일, 커뮤니티 CRUD

### 로그인/로그아웃, 로그인 동기화, 유저 팔로우, 영화 좋아요 기능

# 20230524
1. 로그인 / 로그아웃 버그 수정!! (완)
2. 프로필 수정(views,urls)
3. 프로필 DB랑 VUE 연결해서 출력하기
4. 유저 팔로우(유저 팔로워 보기, 유저 팔로잉 보기)
5. Community 구현
6. 영화 디테일 CRUD(삭제), Community CRUD(삭제)
7. 프로필 comment (프로필 주인만 볼수있게)


# 야근 할 것
- 커뮤니티
  - Article (모델에 type 추가 -> 게시판 종류 판별)
  - Comment
- 프로필에 댓글 기능(완)
  - user 모델에 comment
- 영화 좋아요 기능
  - 프로필에 영화 좋아요 리스트 출력


community 게시판을 보여주고 게시물리스트까지 보여줌
해당 게시물에 들어가면 해당 게시물의 상세페이지로 들어감-> component(자유게시판, 연애게시판, 비밀게시판, 친구게시판)
상세페이지에서 내용 제목 유저이름을 보여줌 -> 
거기서 댓글 달수있게함 


# 20230525 
- community commponet(게시판 복제) (완)
- 프로필 이미지 넣기( 중요!!!!!!) (완)
- css (완)
- 영화좋아요 리스트(영화 좋아요 구현)
- 팔로우팔로잉 비동기화


- updated_at 시간 제대로 나오게하기
- follow following 버튼 토글
- 프로필 댓글 (보이게 안보이게)

- signup /login/ board content / comment / 
