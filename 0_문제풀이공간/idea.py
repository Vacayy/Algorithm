import random
arr = [
    "커피숍",
    "스마트홈",
    "웰니스",
    "가상현실 (VR)",
    "블록체인",
    "친환경 여행",
    "드론 배송",
    "워크프롬홈",
    "건강 추적기",
    "로컬 푸드",
    "게임 스트리밍",
    "온라인 교육",
    "팟캐스트",
    "인공지능 (AI)",
    "전기차",
    "3D 프린팅",
    "사물인터넷 (IoT)",
    "크라우드펀딩",
    "유튜브 크리에이터",
    "미니멀리즘",
    "스트리트 푸드",
    "셀프 케어",
    "스포츠 피트니스",
    "전자책",
    "모바일 결제",
    "원격 의료",
    "스타트업",
    "라이브 스트리밍",
    "패션 테크",
    "도시 농업",
    "애완동물 케어",
    "소셜 미디어",
    "데이터 분석",
    "클라우드 컴퓨팅",
    "가상현실 여행",
    "텔레프레즌스",
    "사이버보안",
    "로보틱스",
    "디지털 아트",
    "착용 가능한 기술",
    "지속 가능한 패션",
    "리사이클링",
    "스마트시티",
    "유저 경험 디자인",
    "푸드 테크",
    "비디오 게임",
    "언택트 서비스",
    "홈 피트니스",
    "디지털 마케팅",
    "비대면 교육",
    "자전거 공유",
    "미세먼지 대응",
    "명상 앱",
    "푸드 데스크",
    "모바일 게임",
    "스마트워치",
    "홈 오토메이션",
    "패스트 패션",
    "학부모 커뮤니티",
    "디지털 노마드",
    "코워킹 스페이스",
    "여행 플래너",
    "버추얼 피트니스 클래스",
    "소규모 농부",
    "온라인 튜터링",
    "글로벌 물류",
    "스트리트 아트",
    "도시 탐험가",
    "소프트웨어 개발자",
    "스마트 키친 기기",
    "독립 음악가",
    "프리랜서 디자이너",
    "홈 브루잉",
    "시니어 테크",
    "스타트업 멘토",
    "핸드메이드 제품",
    "콘텐츠 크리에이터",
    "어반 컬쳐",
    "비건 라이프스타일",
    "디지털 웰니스",
    "헬스케어 혁신",
    "영어 학습 앱",
    "지역사회 봉사",
    "직장인 요가",
    "인터랙티브 미디어",
    "지속 가능한 여행",
    "가상 교육",
    "아웃도어 액티비티",
    "웹툰 작가",
    "도시 재생",
    "푸드 딜리버리 서비스",
    "마이크로 모빌리티",
    "셀프 임프루브먼트",
    "원격근무 관리자",
    "친환경 패키징",
    "로컬 커뮤니티",
    "스마트 농업",
    "글로벌 뉴스",
    "DIY 프로젝트",
    "취미 클래스"
]


for i in range(50):
    random_selection = random.sample(arr, 3)
    print(random_selection)
