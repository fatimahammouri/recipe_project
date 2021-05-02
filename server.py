from flask import Flask, render_template, request, flash, session, redirect
from jinja2 import StrictUndefined
from model import connect_to_db
import crud


app = Flask(__name__)
app.secret_key = "recipe"
app.jinja_env.undefined = StrictUndefined
##########################################################################


@app.route('/')
def homepage():
    return render_template('homepage.html')


##########################################################################

if __name__ == '__main__':

    connect_to_db(app, echo=False)
    app.run(host='0.0.0.0', debug=True, port=5000)