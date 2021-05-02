from flask import Flask, render_template, request, flash, session, redirect
from jinja2 import StrictUndefined
from model import connect_to_db
import crud
import requests

app = Flask(__name__)
app.secret_key = "recipe"
app.jinja_env.undefined = StrictUndefined
##########################################################################


@app.route('/')
def homepage():
    return render_template('homepage.html')


##########################################################################

@app.route("/results/<cuisine>")
def show_results():

    url = 'https://api.spoonacular.com/recipes/complexSearch'
    params = {'apiKey': '10908696a3b54d32b5925b490b9a43be',
               'fillIngredients': True,
                'addRecipeInformation': True,
                'instructionsRequired': True,
                'cuisine':"american" , # how to get it from the clicked cuisine????????? 
                'number' : 10}
                
    response = requests.get(url, params)
    data = response.json()

if __name__ == '__main__':

    connect_to_db(app, echo=False)
    app.run(host='0.0.0.0', debug=True, port=5000)