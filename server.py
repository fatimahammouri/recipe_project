from flask import Flask, render_template, request, flash, session, redirect, jsonify
from jinja2 import StrictUndefined
from model import connect_to_db
import crud
import requests
import parse_function
import model
import cloudinary.uploader
import os

# CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
# CLOUDINARY_KEY_SECRET = os.environ['CLOUDINARY_SECRET']

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

    title = request.json.get("title")
    # print(title)
    cuisine = request.json.get("cuisine")
    instructions = request.json.get("instructions")
    servings = request.json.get("servings")
    ingredients = request.json.get("ingredients")
    ready_in_minutes= request.json.get("ready_in_minutes")
    image = request.json.get("image")
    # user_file = request.json.get("file")
    # print(user_file)
    # result = cloudinary.uploader.upload(user_file,
                    # api_key=CLOUDINARY_KEY,
                    # api_secret=CLOUDINARY_KEY_SECRET,
                    # cloud_name='dplmlgxqq')
    # image = result['secure_url']
    
    # print(request.json)

    # from user input get the cuisine_id
    # cuisine_id = crud.get_cuisine_id_from_name(cuisine)
    
    recipe = crud.create_recipe(title, servings, ready_in_minutes, instructions, ingredients, cuisine, image)

    return render_template("create_recipe_card.html", title=title, cuisine=cuisine,
                            instructions=instructions, servings=servings, image=image, 
                            ingredients=ingredients, ready_in_minutes=ready_in_minutes)


if __name__ == '__main__':

    connect_to_db(app, echo=False)
    app.run(host='0.0.0.0', debug=True, port=5000)