from flask import Flask
from flask import render_template, request, redirect, url_for, session, g
from forms import QuestionForm
from models import Questions, Marks
import json
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'

# 문제 데이터 불러오기
with open('questions.json', 'r', encoding='UTF-8') as f:
    QUESTIONS = json.load(f)

@app.route('/')
def home():
    return render_template('index.html', title='Home')


@app.route('/question/<int:id>', methods=['GET', 'POST'])
def question(id):
    if id == 1:
        session['marks'] = 0
    form = QuestionForm()
    try:
        q = Questions(QUESTIONS, id)
    except Exception:
        return redirect(url_for('score', marks=session['marks']))
    
    if request.method == 'POST':
        option = request.form['options']
        if option == q.ans:
            session['marks'] += 10
        return redirect(url_for('question', id=(id+1)))
    form.options.choices = [(q.a, q.a), (q.b, q.b), (q.c, q.c), (q.d, q.d), (q.e, q.e)]
    return render_template('question.html', form=form, q=q, title='Question {}'.format(id))


@app.route('/score/<int:marks>')
def score(marks):
    m = Marks(marks)
    s="킥보드 안전수칙의 마스터!"
    if m.marks <= 80:
        s="킥보드 안전수칙 지킴이!"
    if m.marks <= 70:
        s="안전수칙 숙지가 필요합니다!"
    return render_template('score.html', title='Final Score', status=s)

app.run(debug=True, host='127.0.0.1')