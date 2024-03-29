


import os
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, login_required, logout_user, current_user, LoginManager
from sqlalchemy import func



db = SQLAlchemy()
DB_NAME = "database.db"


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hiy348ghfurj'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    notes = db.relationship('Note')


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signup', methods = ['GET', 'POST'])
def about():
    if request.method == 'POST':
        email1 = request.form.get('email')
        password = request.form.get('password')
        new_user = User(email=email1, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
    return render_template('signup.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email1 = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email1).first()
        if user:
            if user.password == password:
                #login_user(user, remember=True)
                #message = MIMEMultipart()
                #message['From'] = email1
                #message['To'] = email1
                #message['Subject'] = 'Welcome to Sympton Tracker'
                #message.attach(MIMEText('Welcome to Sympton Tracker', 'plain'))
                #with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
                   # server.login(email1, password)
                   # server.send_message(message)
                return redirect('/sympton')
            else:
                return redirect('/login')
        else:
            return redirect('/login')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/sympton', methods=['GET', 'POST'])
def sympton():
    return render_template('sympton.html')



def create_database(app):
    if not os.path.exists(DB_NAME):
        with app.app_context():
            db.create_all()
            print('Database created')
            # Create the "user" table
            print('Creating User table')
            db.create_all()
            print('User table created')


if __name__ == '__main__':
    create_database(app)
    app.run(debug=True)
