# Dockerfile

# 1. 기본 이미지: Python 3.9 (가볍고 안정적)
FROM python:3.9-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 'requirements.txt' 먼저 복사
COPY requirements.txt .

# 4. (핵심) Flask, Gunicorn 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. 나머지 '모든' 프로젝트 파일 복사 (.py, templates/ 등)
COPY . .

# 6. (선택) 환경 변수 설정 (예: 포트)
ENV PORT 5000

# 7. (핵심) 'Gunicorn'으로 Flask 앱 실행
# (Docker는 'python app.py' 대신, 'Gunicorn'을 쓰는 것이 표준)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]