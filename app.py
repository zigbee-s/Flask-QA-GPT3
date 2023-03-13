from flask import Flask, render_template, request
from gpt.qa import askGPT
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def post():
    question = request.form['question']
    # Perform action on the question
    answer = "This is your answer to the question: \n" + askGPT(question) 
    return answer

if __name__ == '__main__':
    app.run(debug=True)
