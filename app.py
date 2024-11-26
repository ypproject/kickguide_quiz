from flask import Flask, render_template, request, redirect, url_for
import json
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'

# 문제 데이터 불러오기
with open('questions.json', 'r') as f:
    QUESTIONS = json.load(f)

@app.route('/')
def home():
    random.shuffle(QUESTIONS)  # 문제 섞기
    return render_template('quiz.html', questions=QUESTIONS)

@app.route('/result', methods=['POST'])
def result():
    score = 0
    for i, question in enumerate(QUESTIONS):
        user_answer = request.form.get(f'answer-{i}')
        if user_answer == question['answer']:
            score += 10  # 정답 10점

    if score >= 90:
        message = "우수하다!"
    elif score >= 80:
        message = "다시 한번 풀어보자!"
    else:
        message = "다시 공부합시다!"
    
    return render_template('result.html', score=score, message=message)

if __name__ == '__main__':
    app.run(debug=True)