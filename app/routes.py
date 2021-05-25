from app import app
from flask import Flask, render_template, request


def output(start: str, end: str):
    return[start, 'Middle', end]


@app.route('/', methods=['GET', 'POST'])
def index():
    data = ['Fill', 'Filler', 'Fillest']
    errors = []
    results = {}
    swap = False
    if request.method == "POST":
        # get url that the user has entered
        swap = True
        start = request.form['start']
        end = request.form['end']
        data = output(start, end)
    if swap:
        return render_template('graph.html', data=data)
    else:
        return render_template('index.html', errors=errors, results=results)

