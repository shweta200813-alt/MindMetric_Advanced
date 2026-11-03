from flask import Flask, render_template, request, jsonify
from scoring import QUESTIONS, assess_answers
from ml_demo import run_demo
app = Flask(__name__)
@app.route('/')
def home(): return render_template('index.html', question_count=len(QUESTIONS))
@app.route('/assessment', methods=['GET','POST'])
def assessment():
    if request.method == 'GET': return render_template('assessment.html', questions=QUESTIONS)
    answers = {}
    for q in QUESTIONS:
        v=request.form.get(q['id'])
        if v not in {'0','1','2','3','4'}: return render_template('assessment.html',questions=QUESTIONS,error='Please answer every question.')
        answers[q['id']]=int(v)
    safety=request.form.get('safety')
    if safety not in {'no','yes','unsure'}: return render_template('assessment.html',questions=QUESTIONS,error='Please answer the safety question.')
    return render_template('result.html',result=assess_answers(answers,safety))
@app.route('/mood')
def mood(): return render_template('mood.html')
@app.route('/assistant')
def assistant(): return render_template('assistant.html')
@app.route('/ml-lab')
def ml_lab(): return render_template('ml_lab.html')
@app.route('/api/ml-demo')
def ml_api():
    try: return jsonify(run_demo())
    except Exception as e: return jsonify({'error':str(e)}),500
@app.route('/health')
def health(): return jsonify({'status':'ok'})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
