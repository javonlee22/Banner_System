from flask import Flask, request, jsonify,render_template,redirect,url_for,session
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import os

app = Flask(__name__)
#Connection to the MySQL database instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:goaggiepride22@localhost:3306/banner_system'
db = SQLAlchemy(app)
#Creates a random secret key for encryption
app.secret_key = os.urandom(24)

#User object that encapsulates all of the database columns
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

#Home route of the website that redirects to the login page or the dashboard
@app.route('/')
def index():
    #Checks if there is already a user defined in the session
    if 'user' in session:
        #Automatically redirects to the dashboard page
        return redirect(url_for('dashboard'))
    #Renders the login page
    return render_template('login.html')

#Login route that handles the login requests from the client
@app.route('/login', methods=['POST'])
def login():
    #Form data from the login request is stored into banner and password variables
    banner = request.form['banner']
    password = request.form['password']

    #Query the user by Banner ID
    user = User.query.filter_by(banner=banner).first()
    #Continues if there is a query result
    if user:
        #Checks the password
        if user.password == password:
            #Sets the banner ID and isFaculty flag of the session in the form of a cookie
            session['user'] = user.banner
            session['isFaculty'] = user.isFaculty
            #Redirects to the dashboard 
            return redirect(url_for('dashboard'))
        else:
            #Returns rejection response
            return '<h1>Invalid Banner/Password</h1><br/><h3>Please Go Back to Retry</h3>'

#Dashboard route that renders the dashboard page
@app.route('/dashboard')
def dashboard():
    #Checks if the user has successfully logged in
    if 'user' in session:
        isFaculty = session['isFaculty']
        banner = session['user']
        user = User.query.filter_by(banner=banner).first()
        #Creates a timestamp of the login request
        now = datetime.now()
        #Renders the student and instructor page depending on the isFaculty flag
        if isFaculty:
            #Queries all student users
            students = User.query.filter_by(isFaculty=False)
            #Renders the instructor page
            return render_template('instructor.html',first=user.first_name,last=user.last_name,banner=user.banner,
                email=user.email,address=user.address,phone=user.phone_number,students=students,time=now)
        else:
            #Queries all faculty users
            professors = User.query.filter_by(isFaculty=True)
            #Renders the student page
            return render_template('student.html',first=user.first_name,last=user.last_name,banner=banner,
                address=user.address,email=user.email,phone=user.phone_number,balance=user.balance,professors=professors,
                city=user.city,zip_code=user.zip_code,state=user.state,time=now)

#Create student route the handles requests to create student accounts
@app.route('/create_student', methods=['POST'])
def create_student():
    #Takes on the form data from the request
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
    try:
        #Creates a new User Object
        user = User(first,last,banner,password,False,address,phone,city,email,state,zip_code,dob,balance,gpa,credit_hours)
        #Commits the new user to the database
        db.session.add(user)
        db.session.commit()
    #Catches the IntegrityError the occurs when a non-unique banner ID is entered
    except IntegrityError:
        #Cancels the commit to the database
        db.session.rollback()
        #Returns the error message
        return "<h1>Banner already exists please go back and input a new number</h1>"
    #Refreshes the page
    return redirect(url_for('dashboard'))

#Student Update route that handles student requests to update their personal information
@app.route('/student_update', methods=['POST'])
def student_update():
    #Checks if user is logged in
    if 'user' in session:
        #Proccesses form data from request
        banner = session['user']
        address = request.form['popAddress']
        city = request.form['popCity']
        state = request.form['popState']
        zip_code = request.form['zip']
        phone = request.form['popPhone']
        #Queries the database
        user = User.query.filter_by(banner=banner).first()
        #Updates the fields of the User object
        user.address = address
        user.city = city
        user.state = state
        user.zip_code = zip_code
        user.phone_number = phone
        #Commits the update to the database
        db.session.commit()
        #Refreshes the page
        return redirect(url_for('dashboard'))

#Instructor update route that allows faculty to update student academic information
@app.route('/instructor_update', methods=['POST'])
def instructor_update():
    #Checks if user is logged int
    if 'user' in session:
        #Processes form data from request
        banner = request.form['popBanner']
        gpa = request.form['gpa']
        balance = request.form['balance']
        credit = request.form['credithours']
        #Queries the database
        user = User.query.filter_by(banner=banner).first()
        #Updates the fields of the User object
        user.gpa = gpa
        user.balance = balance
        user.credit_hours = credit
        #Commits the update to the database
        db.session.commit()
         #Refreshes the page
        return redirect(url_for('dashboard'))
