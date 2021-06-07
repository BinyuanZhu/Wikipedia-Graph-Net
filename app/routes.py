from app import app
from wikiAPI import *
from graph import a_star, heuristic_0, heuristic_1, heuristic_2
from flask import Flask, render_template, request


def test(start: str, end: str):
    return [start, "1", "2", "3", end]


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    swap = False
    if request.method == "POST":
        # get url that the user has entered
        swap = True
        start = request.form['start']
        end = request.form['end']
        data = output(start, end)
        links = {title: get_url(title) for title in data}
        length = (len(data) - 2)
    if swap:
        return render_template('graph.html', data=data, links=links, length=length)
    else:
        return render_template('index.html', errors=errors, results=results)

