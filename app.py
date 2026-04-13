import ollama
from flask import Flask,render_template, request

app = Flask(__name__)

# History of conversations
history = []

@app.route('/')
def home():
    return render_template('base.html', response='', history=history)

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('message')
    response = ollama.generate(
        model='llama2',
        prompt=f'create caption on this {user_input}',
        stream=True
    )

    output = ''
    for i in response:
        output += i['response']

    # Save history
    history.append({
        'user': user_input,
        'bot': output
    })

    return render_template('base.html', response=output, history=history)


if __name__ == "__main__" :
    app.run(debug=True)