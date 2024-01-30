from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET KEY'] = 'hiy348ghfurj'

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signup', methods = ['GET', 'POST'])
def about():
    return render_template('signup.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

