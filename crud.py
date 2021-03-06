from model import (db, Cuisine, connect_to_db, Recipe)



def create_cuisine(cuisine_name):

    cuisine = Cuisine(cuisine_name=cuisine_name) 
    db.session.add(cuisine)
    db.session.commit()

    return cuisine

##########################################################################

def get_all_cuisines():

    cuisine_list = []

    for cuisine in Cuisine.query.all():
        cuisine_list.append(cuisine.cuisine_name)
    return cuisine_list

##########################################################################

def create_recipe(title, servings, ready_in_minutes, instructions, ingredients, cuisine, image):
    recipe = Recipe(title=title,   
                    servings=servings, 
                    ready_in_minutes=ready_in_minutes,
                    instructions=instructions,
                    ingredients=ingredients, 
                    cuisine=cuisine,
                    image=image)
    db.session.add(recipe)
    db.session.commit()

    return recipe 

##########################################################################

def get_cuisine_id_from_name(cuisine_name):
    cuisine = Cuisine.query.filter(Cuisine.cuisine_name == cuisine_name).first()
    return cuisine.cuisine_id