from flask import Flask, render_template, request, flash, session, redirect, jsonify
from jinja2 import StrictUndefined
from model import connect_to_db
import crud
import requests
import parse_function
import model
import cloudinary.uploader
import os
import re

CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
CLOUDINARY_KEY_SECRET = os.environ['CLOUDINARY_SECRET']

app = Flask(__name__)
app.secret_key = "recipe"
app.jinja_env.undefined = StrictUndefined
##########################################################################


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/recipes')
def get_recipes():
    return render_template('recipes.html')
##########################################################################

@app.route("/results/<cuisine>", methods=['POST'])
def show_results(cuisine):

    url = 'https://api.spoonacular.com/recipes/complexSearch'
    params = {'apiKey': '10908696a3b54d32b5925b490b9a43be',
                'cuisine':cuisine,
                'fillIngredients': True,
                'addRecipeInformation': True,
                'instructionsRequired': True,
                'number' : 20}
                
    response = requests.get(url, params)
    data = response.json()
    results = data['results']

    all_recipes_results = []

    for recipe in results:

        recipe_results = parse_function.parse_api_results(recipe)
        all_recipes_results.append(recipe_results)
    # print(all_recipes_results)
    return render_template('results.html', all_recipes_results=all_recipes_results)

##########################################################################

@app.route("/create_recipe")
def create_recipe():
    cuisine_list = crud.get_all_cuisines()
    return render_template("create_recipe.html", cuisine_list=cuisine_list)

##########################################################################

@app.route("/create_recipe/card", methods=["POST"])
def create_recipe_card():
    # import pdb 
    # pdb.set_trace()
    title = request.form.get("title")
    # print(title)
    cuisine = request.form.get("cuisine")
    instructions = request.form.get("instructions")
    servings = request.form.get("servings")
    
    ready_in_minutes= request.form.get("ready_in_minutes")
    image_cloud = request.files.get("image")
    
    # ingredients list manipulations
    ingredient_list = request.form.get("ingredients")
    # print(ingredient_list, type(ingredient_list)) 
    # print("list :" + ingredient_list)
    # print(type(ingredient_list))
    ingredients = ingredient_list.strip('][') # to be stored in db
    # print("stored in db", ingredients, type(ingredients))
    ing_list = ingredient_list.strip('][').split(', ') #to be rendered
    # print("rendering now", ing_list, type(ing_list))
    maybe = re.sub(r'["]','',ingredients)
    # print("maybe is ", maybe, type(maybe))
    # maybe2 = maybe.split(', ')
    # print("maybe 2 ", maybe2, type(maybe2))



    if image_cloud:
        result = cloudinary.uploader.upload(image_cloud,
                    api_key=CLOUDINARY_KEY,
                    api_secret=CLOUDINARY_KEY_SECRET,
                    cloud_name='dplmlgxqq')

        image = result['secure_url']
    else:
        image = None
    
    # print(request.json)

    # from user input get the cuisine_id
    # cuisine_id = crud.get_cuisine_id_from_name(cuisine)
    
    recipe = crud.create_recipe(title, servings, ready_in_minutes, instructions, ingredients, cuisine, image)

    return render_template("create_recipe_card.html", title=title, cuisine=cuisine,
                            instructions=instructions, servings=servings, image=image, 
                            ingredients=maybe, ready_in_minutes=ready_in_minutes)


if __name__ == '__main__':

    connect_to_db(app, echo=False)
    app.run(host='0.0.0.0', debug=True, port=5000)