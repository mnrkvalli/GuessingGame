from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    secret_number = random.randint(1, 100)
    return render_template('index.html', secret_number=secret_number)

@app.route('/guess', methods=['POST'])
def guess():
    guess = request.form['guess']
    secret_number = request.form['secret_number']

    if guess == '' or secret_number == '':
        message = 'Please enter a number.'
    else:
        guess = int(guess)
        secret_number = int(secret_number)

        if guess < secret_number:
            message = 'Too low! Try again.'
        elif guess > secret_number:
            message = 'Too high! Try again.'
        else:
            message = 'Congratulations! You guessed the number.'

    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
