from app import app
from wikiAPI import *
from graph import a_star, heuristic_0, heuristic_1, heuristic_2
from flask import Flask, render_template, request


def err():
    return ["You are seeing this page in error."]


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
        if request.form.get('action1') == 'BFS':
            data = a_star(start, end, heuristic_0)
        elif request.form.get('action2') == 'Intro Semantic':
            data = a_star(start, end, heuristic_2)
        elif request.form.get('action3') == 'Article Semantic':
            data = a_star(start, end, heuristic_1)
        else:
            data = err()
        links = {title: get_url(title) for title in data}
        length = (len(data) - 2)
    if swap:
        return render_template('graph.html', data=data, links=links, length=length)
    else:
        return render_template('index.html', errors=errors, results=results)

