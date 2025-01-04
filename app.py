import os
from dotenv import load_dotenv
from openai import OpenAI

# (1) .env 파일 로드
load_dotenv()  # 기본적으로 현재 프로젝트 루트/실행 위치의 .env를 탐색합니다.

# (2) 환경변수에서 키 가져오기
api_key = os.environ.get("OPENAI_API_KEY")

# (3) OpenAI 클라이언트 생성
client = OpenAI(api_key=api_key)

def main():
    try:
        # (4) ChatCompletion API 호출
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model="gpt-4o-mini",
        )
        # 결과 출력
        print(chat_completion)
    
    except Exception as e:
        print("알 수 없는 오류 발생:", e)

if __name__ == "__main__":
    main()

