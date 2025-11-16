from flask import Flask, jsonify, render_template

app = Flask(__name__)

# --- 1. 6개 '웹페이지' 라우터 ---
# (PDF 요구사항 1)

@app.route('/main')
def main_page():
    # 'templates' 폴더의 'main.html' 파일을 렌더링
    return render_template('main.html')

@app.route('/subject')
def subject_page():
    return render_template('subject.html')

@app.route('/rationale')
def rationale_page():
    return render_template('rationale.html')

@app.route('/features')
def features_page():
    return render_template('features.html')

@app.route('/environment')
def environment_page():
    return render_template('environment.html')

@app.route('/team')
def team_page():
    return render_template('team.html')

@app.route('/readme')
def readme_page():
    try:
        # (수정) 'README.md' -> 'readme.MD' (파일 이름과 100% 동일하게)
        with open('README.md', 'r', encoding='utf-8') as f: 
            content = f.read()
        return f"<pre>{content}</pre>"
    except FileNotFoundError:
        return "'readme.MD' 파일을 찾을 수 없습니다.", 404


# --- 2. 'API' 라우터 ---
# (PDF 요구사항 2: /api/<페이지명>)
@app.route('/api/subject')
def api_subject():
    return jsonify({
        "-제목":"옵티마오더",
        "-요약":"Prophet과  날씨 API를 이용한 무인매장 자동 발주 시스템",
    
    })

@app.route('/api/rationale')
def api_rationale():
    return jsonify({
        "-문제":"무인매장에서 발생하는 인건비와 시간낭비 문제",
        "-근거(수치)":"2021년이후 무인매점의 점포수는 2025년 1만개를 돌파",
        "-기대가치":"재고 최적화, 운영비 절감, 고객만족도 향상",
    })

@app.route('/api/features')
def api_features():
    return jsonify({
        "기능1": "재고 목록보기,등록 및 수정",
        "기능2": "판매현황 확인,발주목록확인",
        "기능3": "AI기반 최적화 재고추천 및 자동발주"
    })

@app.route('/api/environment')
def api_environment():
    return jsonify({
        "-Front-End(프론트엔드)": "React Native,TypeScript,Expo go",
        "-Back-End": "Node.js, TypeScript, Prisma",
        "-Runtime(런타임)":"ai_model_manager.py,predict.py",
        "-Deployment(배포)":"로컬(저번주에 실수로 EC2를 켜놓고가서 거의다 써버렸습니다..)",
        "ai_engine": "Python, Prophet, Pandas",
        "database": "PostgreSQL",
        "api": "Kakao Geocoding, Open-Meteo"
    })


@app.route('/api/team')
def api_team():
    # '팀원 목록' (List/Array)
    team_members = [
        # (수정) 1번 오류(문법)를 '개별' 딕셔너리로 해결
        { 
            "이름": "조빌립", 
            "역할": "AI개발" 
        },
        { 
            "이름": "송상혁", 
            "역할": "프론트앤드 및 백엔드 개발" 
        },
        { 
            "이름": "황선우", 
            "역할": "자료수집 및 프론트엔드 개발" 
        }
    ]

# (subject, rationale, team API도 동일하게 만듦)


if __name__ == '__main__':
    # Docker로 실행할 때는 'gunicorn'을 사용하고, 
    # PC에서 테스트할 때는 'python app.py'로 실행
    app.run(host='0.0.0.0', port=5000, debug=True)