


import os

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import func

db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hiy348ghfurj'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)



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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
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
    return render_template('login.html')


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
