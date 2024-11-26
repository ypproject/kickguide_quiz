from flask import Flask
from flask import render_template, request, redirect, url_for, session, g
from forms import QuestionForm
from models import Questions, Marks
import json
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'

# 문제 데이터 불러오기
with open('questions.json', 'r') as f:
    QUESTIONS = json.load(f)

@app.route('/')
def home():
    session['marks'] = 0
    return render_template('index.html', title='Home')


@app.route('/question/<int:id>', methods=['GET', 'POST'])
def question(id):
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
    form.options.choices = [(q.a, q.a), (q.b, q.b), (q.c, q.c), (q.d, q.d)]
    return render_template('question.html', form=form, q=q, title='Question {}'.format(id))


@app.route('/score/<int:marks>')
def score(marks):
    m = Marks(marks)
    return render_template('score.html', title='Final Score')

app.run(debug=True, host='127.0.0.1')