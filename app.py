import os
from dotenv import load_dotenv
import google.generativeai as genai  # type: ignore

# (1) .env 파일 로드
load_dotenv()  # 기본적으로 현재 프로젝트 루트/실행 위치의 .env를 탐색합니다.

# (2) 환경변수에서 키 가져오기
api_key = os.environ.get("GEMINI_API_KEY")


def main():
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash-lite")
        chat = model.start_chat(history=[])

        while True:
            message = input("Q)")
            if message == "exit":
                break
            response = chat.send_message(message)
            print("A)")
            print(response.text)

    except Exception as e:
        print("알 수 없는 오류 발생:", e)


if __name__ == "__main__":
    main()
