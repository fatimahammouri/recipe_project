from flask import Flask, render_template, request, flash, session, redirect, jsonify
from jinja2 import StrictUndefined
from model import connect_to_db
import crud
import requests
import seed

app = Flask(__name__)
app.secret_key = "recipe"
app.jinja_env.undefined = StrictUndefined
##########################################################################


@app.route('/')
def homepage():
    return render_template('homepage.html')


##########################################################################

@app.route("/results/<cuisine>")
def show_results(cuisine):

    url = 'https://api.spoonacular.com/recipes/complexSearch'
    params = {'apiKey': '10908696a3b54d32b5925b490b9a43be',
               'fillIngredients': True,
                'addRecipeInformation': True,
                'instructionsRequired': True,
                'cuisine':cuisine, # how to get it from the clicked cuisine????????? 
                'number' : 10}
                
    response = requests.get(url, params)
    data = response.json()
    results = data['results']

    all_recipes_results = []

    for recipe in results:

        recipe_results = seed.parse_api_results(recipe)
        all_recipes_results.append(recipe_results)
        return jsonify(all_recipes_results)


if __name__ == '__main__':

    connect_to_db(app, echo=False)
    app.run(host='0.0.0.0', debug=True, port=5000)