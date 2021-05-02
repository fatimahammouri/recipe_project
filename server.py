from flask import Flask, render_template, request, flash, session, redirect
from jinja2 import StrictUndefined
from model import connect_to_db
import crud


connect_to_db(app, echo=False)
app.run(host='0.0.0.0', debug=True, port=5000)