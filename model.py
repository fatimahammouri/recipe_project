"""Models for side project"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
db = SQLAlchemy()


####################################################################################

class Cuisine(db.Model):
"""the countries table"""

    __tablename__ = 'cuisines'

    cuisine_id = db.Column(db.Integer, primary_key=True,
    autoincrement=True)
    cuisine_name = db.Column(db.String(50))


    def __repr__(self):
    return f'<Country country_code={self.country_code} contry_name={self.contry_name}>’

####################################################################################

def connect_to_db(flask_app, db_uri='postgresql:///recipe', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app


    connect_to_db(app)
