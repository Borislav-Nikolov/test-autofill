from flask import Flask, render_template, request, redirect, url_for
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # username = request.form.get('usernameName')
        # password = request.form.get('password')
        # captcha = request.form.get('captcha')
        return redirect(url_for('home'))

    return render_template('index.html')


@app.route('/login_bad_username', methods=['GET', 'POST'])
def login_bad_username():
    if request.method == 'POST':
        # username = request.form.get('usernameName')
        # password = request.form.get('password')
        # captcha = request.form.get('captcha')
        return redirect(url_for('home_bad_username'))

    return render_template('indexbadusername.html')


@app.route('/cardform', methods=['GET', 'POST'])
def card_form():
    if request.method == 'POST':
        return redirect(url_for('general_success'))

    return render_template('cardform.html')


@app.route('/general_success')
def general_success():
    return render_template('generalsuccess.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/home_bad_username')
def home_bad_username():
    return render_template('homebadusername.html')


@app.route('/')
def page_selector():
    return render_template('pageselector.html')


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 8081), app)
    http_server.serve_forever()
