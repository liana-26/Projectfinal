from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/page_2')
def page_2():
    return render_template('page2.html')

@app.route('/page_3')
def page_3():
    return render_template('page3.html')

@app.route('/page_4')
def page_4():
    return render_template('page4.html')

@app.route('/page_5')
def page_5():
    return render_template('page5.html')

@app.route('/page_6')
def page_6():
    return render_template('page6.html')

@app.route('/page_7')
def page_7():
    return render_template('page7.html')

@app.route('/page_8')
def page_8():
    return render_template('page8.html')

@app.route('/page_9')
def page_9():
    return render_template('page9.html')

@app.route('/page_10')
def page_10():
    return render_template('page10.html')

@app.route('/submit_suggestion', methods=['POST'])
def submit_suggestion():
    suggestion = request.form['suggestion']
    with open('suggestions.txt', 'a') as file:
        file.write(suggestion + '\n')
    return redirect('/')

@app.route('/topics', methods=['POST'])
def topics():
    answer_1 = request.form['answer_1']
    with open('answer_1.txt', 'a') as file:
        file.write(answer_1 + '\n')
    answer_2 = request.form['answer_2']
    with open('answer_2.txt', 'a') as file:
        file.write(answer_2 + '\n')
    answer_3 = request.form['answer_3']
    with open('answer_3.txt', 'a') as file:
        file.write(answer_3 + '\n')
    answer_4 = request.form['answer_4']
    with open('answer_4.txt', 'a') as file:
        file.write(answer_4 + '\n')
    answer_5 = request.form['answer_5']
    with open('answer_5.txt', 'a') as file:
        file.write(answer_5 + '\n')
    return redirect('/')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    feedbackn = request.form['feedbackn']
    feedback = request.form['feedback']
    with open('feedback.txt', 'a') as file:
        file.write(feedbackn + ':' + feedback + '\n')
    return redirect('/')

if __name__ == '__main__':
    app.run()

