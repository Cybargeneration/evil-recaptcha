from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Route to the login page
@app.route('/')
def login():
    return render_template('login.html')

# Route to the CAPTCHA page after login
@app.route('/captcha')
def captcha():
    return render_template('captcha.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

