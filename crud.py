from model import (db, User, Recipe, Cuisine, Ingredient,
                Ingredient_recipe, recipe_cuisine, connect_to_db)



def create_cuisine(cuisine_name):

    cuisine = Cuisine(cuisine_name=cuisine_name) 
    db.session.add(cuisine)
    db.session.commit()

    return cuisine

##########################################################################

def get_all_cuisines():
    return Cuisine.query.all()