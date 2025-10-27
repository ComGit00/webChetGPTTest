# ChatGPT 웹 채팅 프로그램

Python, Node.js, React를 활용한 ChatGPT 웹 채팅 애플리케이션입니다.

## 🚀 기능

- 실시간 AI 채팅
- 대화 기록 저장
- 반응형 디자인
- 타이핑 인디케이터
- 아름다운 UI/UX
- React 기반 모던 프론트엔드
- TypeScript 지원

## 📋 필수 요구사항

- Node.js (v14 이상)
- Python (v3.8 이상)
- React (v18 이상)
- OpenAI API 키

## 🛠️ 설치 방법

### 1. Python 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. React 의존성 설치

```bash
cd client
npm install
```

### 3. 환경 변수 설정

`.env.example` 파일을 `.env`로 복사하고 OpenAI API 키를 입력하세요:

```bash
cp .env.example .env
```

`.env` 파일을 열고 `OPENAI_API_KEY`를 입력합니다:

```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

## 🎯 실행 방법

### 빠른 시작

**1. Python 서버 시작:**
```bash
python chat_server.py
```

**2. React 개발 서버 시작 (새 터미널):**
```bash
cd client
npm start
```

### 브라우저 접속

**http://localhost:3000** 에서 React 앱이 자동으로 열립니다.

## 📁 프로젝트 구조

```
webChet/
├── chat_server.py         # Python FastAPI 서버 (ChatGPT 연동)
├── requirements.txt       # Python 의존성
├── .env                  # 환경 변수 (생성 필요)
├── README.md             # 프로젝트 문서
├── public/               # 기존 HTML 파일 (백업)
└── client/               # React 애플리케이션
    ├── src/
    │   ├── App.tsx       # 메인 React 컴포넌트
    │   ├── App.css       # 스타일
    │   └── index.tsx     # 진입점
    ├── build/            # 빌드된 파일 (프로덕션)
    └── package.json      # React 의존성
```

## 🔧 기술 스택

### Backend (Python)
- FastAPI: 고성능 웹 프레임워크
- OpenAI: ChatGPT API 클라이언트
- Uvicorn: ASGI 서버
- CORS: Cross-Origin Resource Sharing

### Frontend
- React 18
- TypeScript
- CSS3 (모던 디자인)
- React Hooks

## 📝 API 엔드포인트

### POST /api/chat

채팅 메시지를 전송합니다.

**Request:**
```json
{
  "message": "안녕하세요!",
  "conversationHistory": [
    {
      "role": "user",
      "content": "이전 메시지"
    },
    {
      "role": "assistant",
      "content": "이전 응답"
    }
  ]
}
```

**Response:**
```json
{
  "response": "안녕하세요! 무엇을 도와드릴까요?",
  "role": "assistant"
}
```

## 🎨 주요 특징

- **그라데이션 디자인**: 세련된 UI
- **반응형 레이아웃**: 모바일/데스크톱 지원
- **대화 기록 관리**: 컨텍스트 유지
- **실시간 피드백**: 타이핑 인디케이터

## ⚙️ 환경 변수

- `OPENAI_API_KEY`: OpenAI API 키 (필수)
- `PORT`: Node.js 서버 포트 (기본값: 3000)
- `PYTHON_API_URL`: Python 서버 URL (기본값: http://localhost:8000)

## 🔑 OpenAI API 키 발급 방법

1. https://platform.openai.com 에서 계정 생성
2. API Keys 메뉴로 이동
3. "Create new secret key" 클릭
4. 생성된 키를 `.env` 파일에 입력

## 📝 라이선스

MIT License

## 🤝 기여

이슈와 풀 리퀘스트를 환영합니다!

