from flask import Flask, request, jsonify,render_template,redirect,url_for,session
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import time
import os



app = Flask(__name__)

#Connection to the MySQL database instance              #<username>:<password>
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:goaggiepride22@localhost:3306/banner_system'
db = SQLAlchemy(app)

#Encryption Class
bcrypt = Bcrypt(app)

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
    timestamp = db.Column ('timestamp',db.Numeric(20,6),nullable=True)


    def __init__(self,first_name,last_name,banner,password,isFaculty,address,phone_number,city,email,state,zip_code,dob,balance,gpa,credit_hours,timestamp):
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
        self.timestamp = timestamp

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
        if check_password_hash(user.password, password):
            #Sets the banner ID and isFaculty flag of the session in the form of a cookie
            session['user'] = user.banner
            session['isFaculty'] = user.isFaculty
            session['timestamp'] = user.timestamp
            #Creates a timestamp of the login request
            user.timestamp = time.time()
            print(time.time())
            db.session.commit()
            #Redirects to the dashboard 
            return redirect(url_for('dashboard'))
        else:
            #Returns rejection response
            return '<h1>Invalid Banner/Password</h1><br/><a href="/">Please Go Back to Retry</a>'
    else:
        return '<h1>Banner ID Does Not Exist<h1><br/><a href="/">Please Go Back to Retry</a>'

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))

#Dashboard route that renders the dashboard page
@app.route('/dashboard')
def dashboard():
    #Checks if the user has successfully logged in
    if 'user' in session:
        isFaculty = session['isFaculty']
        banner = session['user']
        timestamp = session['timestamp']
        update = None
        user = User.query.filter_by(banner=banner).first()
        if timestamp:
            last_login = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S.%f')
        else: last_login = None
        #Renders the student and instructor page depending on the isFaculty flag
        if isFaculty:
            #Queries all student users
            students = User.query.filter_by(isFaculty=False)
            #Renders the instructor page
            return render_template('instructor.html',first=user.first_name,last=user.last_name,banner=user.banner,
                email=user.email,address=user.address,phone=user.phone_number,students=students,time=last_login,update=update)
        else:
            #Queries all faculty users
            professors = User.query.filter_by(isFaculty=True)
            #Renders the student page
            return render_template('student.html',first=user.first_name,last=user.last_name,banner=banner,
                address=user.address,email=user.email,phone=user.phone_number,balance=user.balance,professors=professors,
                city=user.city,zip_code=user.zip_code,state=user.state,time=last_login,update=update)
    else: 
        return '<h1>You are not authorized to view this page.<br/>Please proceed to the login page to sign in.</h1> <a href="/">Log In</a>'

#Create student route the handles requests to create student accounts
@app.route('/create_student', methods=['POST'])
def create_student():
    if 'user' in session:
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
        pw_hash = generate_password_hash(password)
        balance = request.form['balance']
        gpa = request.form['gpa']
        credit_hours = request.form['credit_hours']
        try:
            #Creates a new User Object
            user = User(first,last,banner,pw_hash,False,address,phone,city,email,state,zip_code,dob,balance,gpa,credit_hours,None)
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
    else:
        return '<h1>You are not authorized to view this page.<br/>Please proceed to the login page to sign in.</h1> <a href="/">Log In</a>'

#Student Update route that handles student requests to update their personal information
@app.route('/student_update', methods=['POST'])
def student_update():
    #Checks if user is logged in
    if 'user' in session:
        #Proccesses form data from request
        banner = session['user']
        #Generates update timestamp
        session['lastUpdate'] = datetime.now()
        address = request.form['popAddress']
        city = request.form['popCity']
        state = request.form['popState']
        zip_code = request.form['zip']
        phone = request.form['popPhone']
        password = request.form['password']
        #Generates hash of the password
        pw_hash = generate_password_hash(password)
        #Queries the database
        user = User.query.filter_by(banner=banner).first()
        #Updates the fields of the User object
        user.address = address
        user.city = city
        user.state = state
        user.zip_code = zip_code
        user.phone_number = phone
        user.password = pw_hash
        #Commits the update to the database
        db.session.commit()
        #Refreshes the page
        return redirect(url_for('dashboard'))
    else:
        return '<h1>You are not authorized to view this page.<br/>Please proceed to the login page to sign in.</h1> <a href="/">Log In</a>'

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
        #Generates update timestamp
        session['lastUpdate'] = datetime.now()
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
    else:
        return '<h1>You are not authorized to view this page.<br/>Please proceed to the login page to sign in.</h1> <a href="/">Log In</a>'

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'),debug=True)
