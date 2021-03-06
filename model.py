"""Models for side project"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()


####################################################################################

class Cuisine(db.Model):
    """Cuisines table"""
    __tablename__ = 'cuisines'

    cuisine_id = db.Column(db.Integer, primary_key=True,
    autoincrement=True)
    cuisine_name = db.Column(db.String(50))


    def __repr__(self):
        return f'<<Cuisine cuisine_id={self.cuisine_id} name={self.cuisine_name}>>'

####################################################################################

class Recipe(db.Model):
    """Recipes Table"""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, primary_key=True,
                        autoincrement=True)
    title = db.Column(db.String)
    image = db.Column(db.String)
    servings = db.Column(db.Integer)
    ready_in_minutes = db.Column(db.Integer)
    instructions = db.Column(db.Text)
    ingredients = db.Column(db.Text)
    cuisine = db.Column(db.String)
    # cuisine = db.relationship('Cuisine', backref='recipes')
    
    def __repr__(self):
        return f'<<Recipe recipe_id={self.recipe_id} name={self.recipe_name}>>'

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
