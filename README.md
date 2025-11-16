캡스톤 프로젝트 소개 웹 (EC2 + Docker, 또는 로컬)
본 저장소는 캡스톤 프로젝트 단일 소개 페이지와 API를 제공합니다.

##1.작품주제(subject) -제목:옵티마오더 -요약:Prophet과 날씨 API를 이용한 무인매장 자동 발주 시스템

##2.실용적 근거(Rationable) -문제:무인매장에서 발생하는 인건비와 시간낭비 문제 -근거(수치):2021년이후 무인매점의 점포수는 2025년 1만개를 돌파 -기대가치:재고 최적화, 운영비 절감, 고객만족도 향상

##3.핵심근거(Features)
기능1: 재고 목록보기,등록 및 수정
기능2: 판매현황 확인,발주목록확인
기능3: AI기반 최적화 재고추천 및 자동발주

##4.구현환경(Enviroment)
-Front-End(프론트엔드): React Native,TypeScript,Expo go
-Back-End: Node.js, TypeScript, Prisma,
-Runtime(런타임):ai_model_manager.py,predict.py
-Deployment(배포):로컬 / AWS EC2 / AWS ECS
ai_engine: "Python, Prophet, Pandas
database: PostgreSQL
api: Kakao Geocoding, Open-Meteo

##5.팀원구성 및 역할 -이름:조빌립, 역할:AI개발 -이름:송상혁, 역할:프론트앤드 및 백엔드 개발 -이름:황선우, 역할:자료수집 및 프론트엔드 개발

##6.실행방법(Run)

docker compose up --build -d

# http://localhost:5000 / http://3.35.209.186
