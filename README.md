<img src="https://capsule-render.vercel.app/api?type=soft&color=006F3F&height=80&section=header&text=☕BrewStar☕&fontSize=50&fontColor=D1E7E0"/>

# BrewStar - Backend

📌 FrontEnd와 관련된 내용은 https://github.com/MadCamp-2ndWeek-BrewStar/BrewStar_FrontEnd 로‼️

### 👥 Developers
- 안희웅: 고려대학교 컴퓨터학과 19학번
- 송한이: KAIST 전산학부 21학번

### 💻 Tech Stacks
https://velog.velcdn.com/images/apro_xo/post/d8e816b5-64de-42c7-98b3-bf52ff04ed4c/image.PNG

- Flask 2.0.1
- db version v7.0.5
- Python 3.10.12

## 📢 Description

***Summary***

몰입캠프 2주차 안드로이드 앱 제작 프로젝트입니다.
본 프로젝트는 두 개의 탭으로 구성된, 서버와 통신하는 안드로이드 앱 개발을 다루고 있습니다.

---

### SERVER: flask
- KCloud에 접속하여, ***pip install flask***를 통해 서버에 flask를 설치하였습니다.

### DB: MongoDB(noSQL)
- ***pip install pymongo***를 통해 서버에 MongoDB를 설치하였습니다.

### ❓왜 noSQL을 사용하였는가?
- 메뉴에 따라 아주 다른 커스터마이징 가능성
- MySQL을 사용하면, attribute를 수정하기 어려움 + 정말 많은 커스터마이징 종류로 인해 null이 너무 많아짐
=> 따라서, 유연하게 속성을 다룰 수 있는 noSQL을 사용
=> 데이터의 추가/제거/편집이 아주 순조로웠음

### 📱API

***Main Features***

- **@app.route("/allCustoms", methods=['GET'])** : 모든 커스텀 메뉴 불러오기 
- **@app.route("/myCustom", methods=['GET'])** : 내가 작성한 커스텀 메뉴 불러오기 
- **@app.route("/myFavorite", methods=['GET'])** : 내가 좋아요한 커스텀 메뉴 불러오기
- **@app.route("/addCustom", methods=['POST'])** : 내가 작성한 커스텀 메뉴 추가
- **@app.route("/editCustom", methods=['POST'])** : 내가 작성한 커스텀 메뉴 수정
- **@app.route("/deleteCustom", methods=['POST'])** : 내가 작성한 커스텀 메뉴 삭제
- **@app.route("/addUser", methods = ['POST'])** : 카카오톡으로 처음 로그인한 유저 앱에 등록
- **@app.route("/getNickname", methods = ['GET'])** : 카카오톡 고유번호(토큰) 이용 사용자 닉네임 불러오기
- **@app.route("/likeCustom", methods=['POST'])** : 좋아요 누른 (좋아요 취소한) 커스텀 메뉴 내 좋아요 목록에 관리 + 좋아요 +,-1 적용 기능 


***Technical Description***

- GET, POST 메쏘드 통한 API 구현
- request.args.get (GET), request.form.get (POST) 통해 front에서 변수 받아오기
- datetime.now() 사용해서 커스텀 추가된 시간 기록 및 커스텀 시간순 나열하기
- find, update, delete, insert 명령어 통해 db 수정. 


## Collections

### user_nick (BrewStar 사용자 관리) 

- 카카오톡 인증을 통해 로그인한 유저의 카카오톡 닉네임과 고유번호 저장. 

### users (사용자별 좋아요 목록 관리)

- 카카오톡 고유번호와 좋아요한 커스텀 메뉴의 objectId 관리.

### customs (사용자들이 만든 커스텀 메뉴들)

- objectId, name, menu, category, custom, description, creator, creatornum (고유번호), likes, createdAt

### custom_guide (스타벅스에서 제공하는 메뉴별 커스토마이징 가이드) 

