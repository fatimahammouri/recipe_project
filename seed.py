import os 
import crud 
import model
import server
import requests 

os.system('dropdb recipe')
os.system('createdb recipe')

model.connect_to_db(server.app)
model.db.create_all()

cuisines_list = ['american', 'african', 'caribbean', 'chinese', 
                'european', 'cajun', 'french', 'greek', 'indian',
                'italian', 'mediterranean', 'mexican', 'thai'] 

for cuisine in cuisines_list:
    cuisine = crud.create_cuisine(cuisine)

##########################################################################

"""creat a helping function parse the complex API response 
    then forms a simpler dictionary of only the data needed 
    from the API response"""

def parse_api_results(complex_results):

    recipe_details = {}

    recipe_details['title'] = complex_results['title']
    recipe_details['image'] = complex_results['image']
    recipe_details['servings'] = complex_results['servings']
    recipe_details['readyInMinutes'] = complex_results['readyInMinutes']
    recipe_details['sourceUrl'] = complex_results['sourceUrl']
    # recipe_details['instructions'] = complex_results['instructions']..we need a different way to get the steps

    for each_step in complex_results['analyzedInstructions'][0]['steps']:
        instructions = each_step['step']
        recipe_details['instructions'] = instructions

    ingredients = []
    for each_ingredient in complex_results["extendedIngredients"]:
        ingredient = each_ingredient["originalString"]
        ingredients.append(ingredient)
        recipe_details["ingredients"] = ingredients

    return recipe_details

