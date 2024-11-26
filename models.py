
class Marks():
    marks = 0
    
    def __init__(self, m):
        self.marks = m
    
    def __repr__(self):
        return '{}'.format(self.marks)

class Questions():
    q_id = 0
    ques = None
    a = None
    b = None
    c = None
    d = None
    ans = None
    
    def __init__(self, Question, q_id):
        self.q_id = q_id
        
        question = Question[q_id-1]
        self.ques = question['question']
        self.a = question['options'][0]
        self.b = question['options'][1]
        self.c = question['options'][2]
        self.d = question['options'][3]
        self.ans = question['answer']

    def __repr__(self):
        return '<Question: {}>'.format(self.ques)