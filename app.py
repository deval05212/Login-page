import ollama
from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html', response='')

@app.route('/submit', methods= ['POST'])
def submit():
    user_input = request.form.get('message')
    print("Entered Text: ",user_input)

    response = ollama.generate(model='llama2', prompt=f'create caption on this {user_input}', stream=True)

    output = ''
    for i in response:
        output += i['response']
    print('Answer: ',output)
    
    return render_template('base.html', response=output)

if __name__ == "__main__" :
    app.run(debug=True)