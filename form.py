from flask import Flask, render_template, request
import os

app = Flask(__name__)
#session['username'] = request.form['username']
#session['password'] = request.form['password']
app.secret_key = os.urandom(32)

@app.route('/')
def root():
    return render_template('root.html')

@app.route('/welcome', methods = ['POST'])
def welcome():
    if request.form['password'] == 'password':
        return render_template('welcome.html', name = request.form['username'])
    else:
        return render_template('root.html', message = 'Incorrect password-please try again')
if __name__ == '__main__':
    app.debug = True
    app.run()
