from flask import render_template, request, redirect, url_for, session
from app import app, db
from app.models import User
import hashlib

def encrypt_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = format(session['username'])
        return render_template('dashboard.html', username=username)
    return 'You are not logged in'
    

@app.route('/login', methods=['GET','POST'])
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    elif request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        hashed_password = encrypt_password(password)
        user = User.query.filter_by(username=username,password=hashed_password).first()
        if user is not None:
            # login successful
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid Username and Password')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user_with_same_username = User.query.filter_by(username=request.form['username']).first()
        user_with_same_email = User.query.filter_by(email=request.form['email']).first()

        if user_with_same_username is not None or user_with_same_email is not None:
            return render_template('register.html', error='Username or email already exists')

        # Encrypt the password
        hashed_password = encrypt_password(request.form['password'])

        # Create a new user
        new_user = User(username=request.form['username'], email=request.form['email'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        return render_template('register.html')