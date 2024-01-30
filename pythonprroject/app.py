from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signup', methods = ['GET', 'POST'])
def about():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
