from app import app
import requests
from flask import Flask, render_template, request

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        # get url that the user has entered
        try:
            start = request.form['start']
            results.append(start)
        except:
            errors.append(
                "Unable to get article. Please make sure it's valid and try again."
            )
    return render_template('index.html', errors=errors, results=results)