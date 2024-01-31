from . import _db
from flask_login import UserMixin




class User(_db.Model, UserMixin):
  id = _db.Column(_db.Integer, primary_key=True)
  name = _db.Column(_db.String(80))
  email = _db.Column(_db.String(80), unique=True)
  password = _db.Column(_db.String(80))


