import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
from openai import OpenAI
from dotenv import load_dotenv

# 환경 변수 로드 (.env 파일의 절대 경로 지정)
env_path = Path(__file__).parent / '.env'
print(f"[INFO] .env 파일 경로: {env_path}")
print(f"[INFO] .env 파일 존재 여부: {env_path.exists()}")

load_dotenv(dotenv_path=env_path)

# OpenAI API 키 확인
api_key = os.getenv('OPENAI_API_KEY')
print(f"[INFO] 로드된 API 키: {api_key[:20] + '...' if api_key else 'None'}")

if not api_key:
    print("[ERROR] OPENAI_API_KEY가 설정되지 않았습니다!")
    print("해결 방법:")
    print("1. 프로젝트 루트에 .env 파일을 생성하세요")
    print("2. .env 파일에 다음 내용을 추가하세요:")
    print("   OPENAI_API_KEY=your_openai_api_key_here")
    print("3. OpenAI API 키를 발급받으세요: https://platform.openai.com/api-keys")
    raise ValueError("OPENAI_API_KEY 환경 변수가 설정되지 않았습니다. .env 파일을 확인하세요.")

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=api_key)
print(f"[SUCCESS] OpenAI API 키가 로드되었습니다. (키: {api_key[:20]}...)")

app = FastAPI(title="ChatGPT Chat Server")

# CORS 설정 (React 개발 서버 및 프로덕션 모두 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React 개발 서버
        "http://localhost:3001",  # 대체 포트
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 요청/응답 모델
class ChatRequest(BaseModel):
    message: str
    conversationHistory: List[Dict] = []

class ChatResponse(BaseModel):
    response: str
    role: str = "assistant"

@app.get("/")
async def root():
    return {"message": "ChatGPT Chat Server is running"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # OpenAI API로 요청 전송
        messages = []
        
        # 대화 기록 추가
        for item in request.conversationHistory:
            messages.append({
                "role": item.get("role", "user"),
                "content": item.get("content", "")
            })
        
        # 현재 메시지 추가
        messages.append({
            "role": "user",
            "content": request.message
        })
        
        # ChatGPT API 호출
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )
        
        assistant_message = response.choices[0].message.content
        
        return ChatResponse(
            response=assistant_message,
            role="assistant"
        )
    
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"ChatGPT API 오류: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

