from flask import Flask, url_for
# laba3.1
app = Flask(__name__)

@app.route('/')
def index(): return 'Hello!'

@app.route('/test')
def test(): return 'Just test'

@app.route('/user/<username>')
def show_profile(username):
    return 'Username: ' + str(username)

with app.test_request_context():
    print(url_for('test'))
    print(url_for('show_profile', username = 'Idea Man'))

app.run()