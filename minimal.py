from flask import Flask, render_template

app = Flask(__name__) 


@app.route('/')
def homepage():
    return render_template('react_test.html')



app.run(host='0.0.0.0', debug=True, port=5000)