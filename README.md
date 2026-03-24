# ☁️ Cloud9 Care

개인 건강 기록과 AI가 분석한 처방전·진료기록으로 개인 맞춤 복약 및 생활습관 가이드를 생성하는 **종합 AI 헬스케어 웹 플랫폼**입니다.
구름 위에 오른듯한 건강한 일상, **Cloud9 Care**가 함께합니다.

## 🚀 서비스 소개 (Introduce)

복잡한 병원 기록과 처방전 관리부터 매일의 복약 관리, 식단/운동 가이드까지 한 곳에서 제공하는 스마트 헬스케어 솔루션입니다. 최신 AI 모델과 RAG(검색 증강 생성) 기술, 자체 스케줄링 워커를 결합하여 사용자에게 꼭 맞는 능동적인 건강 관리 경험을 선사합니다.

---

## 🖼️ 서비스 미리보기

> 주요 기능 화면
### 🏠 랜딩페이지 & 로그인 & 회원가입
<p align="center">
  <img src="./docs/landing-main.png" width="30%">
  <img src="./docs/auth-login.png" width="30%">
  <img src="./docs/auth-signup.png" width="30%">
</p>

### 📊 대시보드
<p align="center">
  <img src="./docs/dashboard-main.png" width="45%">
</p>

### 📋 AI 생활 안내 가이드
<p align="center">
  <img src="./docs/guide-health.png" width="45%">
</p>

### ⏰ 알람
<p align="center">
  <img src="./docs/alarm.png" width="30%">
  <img src="./docs/alarm-bp.png" width="30%">
  <img src="./docs/alarm-bst.png" width="30%">
</p>

### 💊 처방전 & 알약 업로드
<p align="center">
  <img src="./docs/ocr-prescription-upload.png" width="45%">
  <img src="./docs/ocr-pill-upload.png" width="45%">
</p>

### 🧠 건강정보
<p align="center">
  <img src="./docs/health-info-profile.png" width="30%">
  <img src="./docs/health-info-allergy.png" width="30%">
  <img src="./docs/health-info-med.png" width="30%">
</p>

### 🩸 혈당수첩
<p align="center">
  <img src="./docs/glucose-log.png" width="45%">
  <img src="./docs/glucose-log2.png" width="45%">
</p>

### ❤️ 혈압수첩
<p align="center">
  <img src="./docs/blood-pressure-log.png" width="45%">
  <img src="./docs/blood-pressure-log2.png" width="45%">
</p>

### ✅ 하루 건강 미션
<p align="center">
  <img src="./docs/daily-mission.png" width="45%">
</p>

### 💬 건강 상담 챗봇
<p align="center">
  <img src="./docs/chat-assistant.png" width="45%">
</p>

### 👤 마이페이지
<p align="center">
  <img src="./docs/mypage-profile.png" width="45%">
  <img src="./docs/mypage-password.png" width="45%">
</p>

---

## ✨ 핵심 기능 (Key Features)

### 📄 1. 처방전 및 진단서 AI 자동 분석 (OCR & Multimodal)
- **손쉬운 기록 업로드**: 처방전이나 병원 진단서를 사진으로 업로드하면 AI가 핵심 의료 정보를 자동으로 추출 및 분석합니다.
- **데이터 정형화**: 복잡한 약품 이름과 복약 지시사항, 진단 질환을 사용자 프로필에 깔끔하게 자동 등록합니다.

### 🌟 2. AI 맞춤형 헬스케어 가이드 (RAG & LLM)
- **3대 영역 가이드 생성**: 사용자의 건강 데이터를 기반으로 `[복약 안내]`, `[주요 질환 관리]`, `[생활습관(식단/운동) 추천]` 세 가지 영역의 맞춤형 가이드를 제공합니다.
- **RAG 기반 전문성**: 전문 의료 및 건강 문서들을 ChromaDB 벡터 저장소에 임베딩하여, 환자 상태에 맞는 검증된 정보를 기반으로 LLM이 가이드를 생성합니다.
- **개인 맞춤 건강 관리**: 사용자 상태에 따라 필요한 정보만 선별 제공하여, 불필요한 정보 없이 실질적인 건강 관리 행동으로 이어지도록 설계했습니다.

### ⏰ 3. 스마트 복약 알람 및 플랜 체크 (AI Worker & FCM)
- **복약 일정 자동화**: 등록된 처방전을 바탕으로 복약 스케줄을 자동 생성합니다.
- **백그라운드 스케줄러**: 백엔드와 분리된 전용 AI Worker(`alarm_scheduler`)가 지정된 시간에 푸시 알림(FCM 연동)을 발송하여 약 복용을 잊지 않게 돕습니다.

### 💬 4. 실시간 건강 상담 챗봇 (Interactive Chat)
- 언제 어디서든 건강에 관한 궁금증이나 현재 섭취 중인 약에 대한 주의사항을 즉각적으로 물어보고 AI의 답변을 받을 수 있습니다.

### 📊 5. 직관적인 대시보드 및 마이페이지
- **데일리 인사이트**: 날씨 정보 및 오늘의 건강 상태, 캘린더 일정을 대시보드에서 한눈에 파악할 수 있습니다.
- **모던 반응형 UI**: PC, 태블릿, 모바일에 완벽하게 호환되는 세련된 카드 레이아웃과 동적인 디자인 시스템을 적용했습니다.

---

## 🏗️ 시스템 아키텍처 및 기술 스택 (Architecture & Tech Stack)

### 🖥️ Frontend
- **Tech**: HTML5, CSS3, Vanilla JS, Jinja2 (서버 사이드 템플릿)
- **UI/UX**: 전체 페이지 완벽한 반응형(Responsive) 웹 디자인, CSS Grid / Flexbox 기반 Модᅥᆫ 레이아웃 구현

### ⚙️ Backend (API Server)
- **Framework**: Python 3.13+, **FastAPI** (비동기 처리 기반으로 AI 응답 대기 시간 최소화)
- **ORM & DB**: Tortoise ORM, MySQL (비동기 ORM으로 성능 확보, Redis로 캐싱 및 상태 관리)
- **Router 모듈화**: Auth, User, OCR, Multimodal, Dashboard, Chat, Guide 등 도메인별 세분화된 API 설계

### 🤖 AI Worker & Data
- **AI Worker 분리**: 무거운 추론 작업과 알람 스케줄링(`alarm_scheduler.py`) 작업을 별도의 컨테이너로 분리하여 API 서버 응답 지연 방지
- **AI Models**: GPT-4o-mini, 외부 OCR API 연동
- **Vector DB**: ChromaDB (RAG 문서 임베딩 및 검색)

### 🚢 DevOps & 인프라
- **Container**: Docker, Docker-Compose (전체 서비스 원클릭 실행)
- **Package Manager**: UV (초고속 파이썬 의존성 및 가상환경 관리)
- **Deploy & CI**: AWS EC2 기반 자동 배포 쉘 스크립트, Nginx 리버스 프록시, Certbot(HTTPS), Ruff/Mypy/Pytest 기반 품질 검증

---

## 🔥 기술적 도전과 해결 (Engineering Highlights)

### 1. RAG 파이프라인 성능 최적화 (가이드 생성 시간 3배 단축)
방대한 데이터를 조회하고 LLM을 호출하는 과정의 긴 대기 시간을 획기적으로 개선했습니다.
- **병목 분석 및 프롬프트 경량화**: 구간별 지연 시간(Latency)을 측정하여 불필요한 컨텍스트 토큰을 줄이고 단일 응답 시간을 35% 단축했습니다.
- **비동기 병렬 처리 (`asyncio.gather`)**: 3개 섹션(복약/질환/생활습관)을 동시에 생성하여 순차 대기 시간을 없앴습니다.
- **MD5 캐싱**: 유저 데이터에 변경 사항이 없을 시 LLM 호출을 생략하고 캐시를 즉시 반환(0초)하여 비용과 속도를 모두 잡았습니다.

### 2. 백그라운드 Worker를 통한 안정적인 스케줄링
수백 명의 사용자가 동시에 복약 알람을 받아야 하는 상황을 고려하여, FastAPI 웹 서버와 알람 발송 서버(AI Worker)를 물리적/논리적으로 분리했습니다. 이를 통해 웹 서버의 응답 지연 없이 안정적으로 푸시 알림(FCM) 트래픽을 소화할 수 있습니다.

---

## 📂 프로젝트 구조 (Repository Structure)

```text
.
├── ai_worker/          # 알람 스케줄링 + AI 추론 처리 (서버 부하 분리 핵심)
├── app/                # 메인 서비스 (API 서버 + 프론트엔드)
│   ├── apis/           # 도메인별 API 라우터 (확장성과 유지보수 고려한 구조)
│   ├── core/           # 글로벌 설정 (CORS, pydantic-settings 등)
│   ├── db/ & models/   # Tortoise 비동기 ORM 및 MySQL 스키마
│   ├── services/       # 핵심 비즈니스 로직 (LLM, RAG 처리 로직 집중)
│   ├── static/         # 통합 CSS, JS, 미디어 에셋 리소스
│   ├── templates/      # Jinja2 동적 렌더링 HTML View
│   └── main.py         # 애플리케이션 진입점 및 미들웨어
├── envs/               # 배포 환경/로컬 환경별 분리된 .env 변수
├── nginx/              # Nginx 웹 서버 및 리버시 프록시 라우팅 설정
├── scripts/            # 배포(deployment.sh), SSL(certbot.sh) 및 CI 자동화 쉘 스크립트
├── docker-compose.yml  # 로컬/운영 통합 컨테이너 오케스트레이션
└── pyproject.toml      # UV 기반 의존성 추적 및 패키지 설정
```

---

## 🛠️ 시작하기 (Getting Started)

### 1. 패키지 설치
UV 패키지 매니저를 사용하여 시스템 의존성을 설치합니다.
```bash
uv sync                # 전체 설치
uv sync --group app    # API 서버용 모듈만
uv sync --group ai     # AI Worker용 모듈만
```

### 2. 환경 변수 세팅
```bash
cp envs/example.local.env envs/.local.env
# 이후 팀에서 공유된 DB/API 키값 등을 입력하세요.
```

### 3. 로컬 서버 실행
```bash
# FastAPI 서버 실행
uv run uvicorn app.main:app --reload

# 코드 포맷팅 및 정적 검증
./scripts/ci/code_fommatting.sh
```

### 4. Docker Compose 전체 스택 실행
API 서버, AI Worker, DB 셋업, Nginx 등이 모두 묶인 프로덕션 레벨의 스택을 가동합니다.
```bash
docker-compose up -d --build
```
- API 접속 문서: [http://localhost/api/docs](http://localhost/api/docs)
- 실제 외부망 배포 시 기본 제공되는 `scripts/deployment.sh` 스크립트를 통해 AWS 환경에 손쉽게 올릴 수 있습니다.

---

## 🔧 개선 예정 (Future Work)

- 웨어러블 기기 연동을 통한 실시간 건강 데이터 반영
- 개인 맞춤형 식단 추천 알고리즘 고도화
- 복약 순응도(약 잘 먹는지) 기반 피드백 시스템 도입
- 의료 데이터 정확도 검증 및 신뢰성 강화

---

**COPYRIGHT(C) CLOUD9_CARE. ALL RIGHT RESERVED.**
