from model import (db, Cuisine, connect_to_db)



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

def create_recipe(title, image, servings, ready_in_minutes, instructions, ingredients, cuisine_name):
    recipe = Recipe(title=title, 
                    image=image, 
                    servings=servings, 
                    ready_in_minutes=ready_in_minutes,
                    instructions=instructions,
                    ingredients=ingredients, 
                    cuisine_name=cuisine_name)
    db.session.add(recipe)
    db.session.commit()

    return recipe        

    