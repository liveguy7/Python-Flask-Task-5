from flask import Blueprint, render_template, url_for, request, redirect
from werkzeug.security import generate_password_hash
from .models import User
from . import _db
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)


@auth.route('/signup')
def signup():
  return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
  name = request.form.get('name')
  email = request.form.get('email')
  password = request.form.get('password')
  #print(name,email,password)

  user = User.query.filter_by(email=email).first()

  if user:
    return redirect(url_for('auth.signup'))

  new_user = User(name=name, email=email, password=password)
  _db.session.add(new_user)
  _db.session.commit()
  for i in User.query.all():
    print(i.name, i.email, i.password)
    
  return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
  return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
  email = request.form.get('email')
  password = request.form.get('password')
  remember = True if request.form.get('remember') else False

  user = User.query.filter_by(email=email).first()
  
  if not user:
    print(User.query.all())
    return redirect(url_for('home.index'))
  
  login_user(user, remember=remember)
  print(User.query.all())
  return redirect(url_for('home.profile'))

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('home.index'))









