<img src="https://capsule-render.vercel.app/api?type=soft&color=006F3F&height=80&section=header&text=☕BrewStar☕&fontSize=50&fontColor=D1E7E0"/>

# BrewStar - Backend

### 👥 Developers
- 안희웅: 고려대학교 컴퓨터학과 19학번
- 송한이: KAIST 전산학부 21학번

### 💻 Tech Stacks
<![image](https://github.com/MadCamp-2ndWeek-BrewStar/BrewStar_backEnd/assets/102745492/aa296902-a309-4b79-8f89-f2341082f734)/>
- minSdkVersion: 26
- targetSdkVersion: 34

## 📢 Description

***Summary***
몰입캠프 2주차 안드로이드 앱 제작 프로젝트입니다.
본 프로젝트는 두 개의 탭으로 구성된, 서버와 통신하는 안드로이드 앱 개발을 다루고 있습니다.

---

### 📱 MainActivity
![MainActivity](https://github.com/MadCamp-2ndWeek-BrewStar/BrewStar_FrontEnd/assets/112535704/1e6d4c5c-1ac2-428f-b74d-08bb938b8f16)
***Main Features***
- 심플한 스플레시 화면을 만들었습니다.
- "Start By Using KakaoTalk"을 눌러 카카오톡으로 로그인합니다.
- 화면 상단의 네비게이션 바를 이용하여 탭을 전환할 수 있습니다. 슬라이드로도 가능합니다.
- 화면 상단의 로고를 누르면 로그아웃을 할 수 있습니다.

***Technical Description***
- Kakaotalk Developers에서 제공하는 Kakao 로그인 API를 사용하였습니다.
- 카카오톡이 설치되어 있으면 카카오톡 앱으로 로그인, 아니면 카카오계정으로 로그인하도록 구현했습니다.
- 로그인에 성공했을 때, 로그인에 실패했을 때 Toast Message를 띄워 볼 수 있게 하였습니다.

---

### ✌️ TAP1: My Page
![Tab1](https://github.com/MadCamp-2ndWeek-BrewStar/BrewStar_FrontEnd/assets/112535704/63a67328-1d2c-443b-a955-e1dd5fd73553)
***Main Features***
- Favorite Customs 부분에는 "좋아요"를 누른 item들만 뜨도록 했습니다.
  화면 오른쪽의 스위치가 꺼져 있으면 세 개의 종류별로 분류를 해두었고, 각 카테고리를 클릭하면 카테고리 별로 "좋아요"를 누른 item들을 볼 수 있습니다.
  스위치를 켜면 모든 item들을 가로 스크롤을 통해 볼 수 있습니다.
  각 item들을 클릭하면, 팝업창이 뜨면서 상세정보를 볼 수 있습니다.
  각 항목 우측 상단의 별로 표현되어있는 "좋아요" 버튼을 눌러 취소하면, Favorite Customs에서 제외됩니다.
- My Customs 부분은, 사용자가 직접 만든 item들을 나열했습니다.
  각 항목 우측 하단의 수정 버튼을 누르면 해당 item의 내용을 수정할 수 있습니다.
- 화면 하단의 +버튼을 누르면, 팝업창이 뜨면서 새로운 item을 추가할 수 있습니다. Name, Menu, Custom, Description을 입력하게 됩니다.
- 모든 item들은 일정 길이 이상으로 글을 입력하게 되면 ...으로 줄여 나타납니다.
- My Customs에 있는 하나의 item을 왼쪽으로 스와이프하면 삭제할 수 있습니다.
- 모든 업데이트 상황은 전체 화면을 스와이프하여 새로고침을 하면 반영됩니다.

***Technical Description***
- API와 안드로이드 스튜디오를 연결하여, 사용자의 TokenID를 넘겨주면 사용자의 Favorite Customs와 My Customs를 모두 받을 수 있도록 구현하였습니다.
- 또한, 기존의 custom을 수정하거나 새로운 custom을 만들 때 POST 요청을 보내어 서버 DB에 저장될 수 있도록 했습니다.
- AlertDialog.Builder를 이용하여 팝업창을 구현했습니다.
- SwipeRefreshLayout을 통해 스와이프하면 새로고침을 할 수 있습니다.
- 각 항목은 모두 recyclerView로 구현하였습니다.
