from flask import Flask, request, jsonify,render_template,redirect,url_for,session
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import BIGINT
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:goaggiepride22@localhost:3306/banner_system'
db = SQLAlchemy(app)
app.secret_key = os.urandom(24)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    first_name = db.Column('first_name',db.String(20),nullable=False)
    last_name = db.Column('last_name',db.String(50),nullable=False)
    banner = db.Column('banner',db.Integer,nullable=False, unique=True)
    password = db.Column('password',db.String(20),nullable=False)
    isFaculty = db.Column('isFaculty',db.Boolean,nullable=False)
    address = db.Column('address',db.String(45),nullable=False)
    phone_number = db.Column('phone_number',BIGINT(unsigned=True),nullable=False)
    city = db.Column('city',db.String(45),nullable=False)
    email = db.Column('email',db.String(45),nullable=False)
    state = db.Column('state',db.String(45),nullable=False)
    zip_code = db.Column('zip_code',db.Integer,nullable=False)
    dob = db.Column('dob',db.String(45),nullable=False)
    balance = db.Column('balance',db.Float,nullable=False)
    gpa = db.Column('GPA',db.Float,nullable=False)
    credit_hours = db.Column('credit_hours',db.Float,nullable=False)


    def __init__(self,first_name,last_name,banner,password,isFaculty,address,phone_number,city,email,state,zip_code,dob,balance,gpa,credit_hours):
        self.first_name = first_name
        self.last_name = last_name
        self.banner = banner
        self.password = password
        self.isFaculty = isFaculty
        self.address = address
        self.phone_number = phone_number
        self.city = city
        self. email = email
        self.state = state
        self.zip_code = zip_code
        self.dob = dob
        self.balance = balance
        self.gpa = gpa
        self.credit_hours = credit_hours


@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    banner = request.form['banner']
    password = request.form['password']

    user = User.query.filter_by(banner=banner).first()
    if user:
        if user.password == password:
            session['user'] = user.banner
            session['isFaculty'] = user.isFaculty
            return redirect(url_for('dashboard'))
        else:
            return '<h1>Invalid Banner/Password</h1><br/><h3>Please Go Back to Retry</h3>'

@app.route('/dashboard')
def dashboard():
    isFaculty = session['isFaculty']
    banner = session['user']
    user = User.query.filter_by(banner=banner).first()
    if isFaculty:
        students = User.query.filter_by(isFaculty=False)
        return render_template('instructor.html',first=user.first_name,last=user.last_name,banner=user.banner,
            email=user.email,address=user.address,phone=user.phone_number,students=students)
    else:
        professors = User.query.filter_by(isFaculty=True)
        return render_template('student.html',first=user.first_name,last=user.last_name,banner=banner,
            address=user.address,email=user.email,phone=user.phone_number,balance=user.balance,professors=professors)

@app.route('/create_student', methods=['POST'])
def create_student():
    banner = request.form['banner']
    first = request.form['first_name']
    last = request.form['last_name']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip_code']
    email = request.form['email']
    phone = request.form['phone_number']
    dob = request.form['dob']
    password = request.form['password']
    balance = request.form['balance']
    gpa = request.form['gpa']
    credit_hours = request.form['credit_hours']
    user = User(first,last,banner,password,False,address,phone,city,email,state,zip_code,dob,balance,gpa,credit_hours)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('dashboard'))

    

@app.route('/update_student', methods=['POST'])
def update_student():
    pass