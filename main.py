from flask.json import jsonify
from project1 import create_app
from project1 import _db



app = create_app()



if(__name__ == '__main__'):
  #with app.app_context():
    #_db.create_all()
  
  app.run('0.0.0.0', port=81)

