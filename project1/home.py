from flask import Blueprint, jsonify
from flask.templating import render_template
from flask_login import login_required, current_user

home = Blueprint('home', __name__)


@home.route('/')
def index():
  return render_template('index.html')

@home.route('/profile')
@login_required
def profile():
  return render_template('profile.html', name=current_user.name)

@home.route('/contact')
def contact():
  return render_template('contact.html')


@home.route('/users')
def users():
  u = [{
    "id": 1,
    "name": "pan"
  }]
  return jsonify(u)


