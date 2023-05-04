#!/usr/bin/env python
from flask import Flask, request, make_response, render_template, send_file
from database import search
from os.path import exists

# -----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')

# -----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():

    html = render_template('index.html')
    response = make_response(html)
    return response

# -----------------------------------------------------------------------


@app.route('/<imagename>.jpg', methods=['GET'])
def get_image(imagename):
    image_path = imagename + '.jpg'
    print(image_path)
    if exists(image_path):
        return send_file(image_path, mimetype='image/jpg')
    else:
        return send_file('NotFound.jpg', mimetype='image/jpg')

@app.route('/searchresults', methods=['GET'])
def search_results():
    books = search()
    html = '''<br>'''
    pattern = '''<p hidden>%.0f</p> <h2><strong>%s</strong></h2> <h3><strong>%s</strong></h3> <br> <ul>%s</ul>'''

    for book in books:
        obj_id, title, artist, agent_string = book.to_tuple()
        agent_list = agent_string.split(',')
        agent_list_items = ''.join(
            f'<li>{agent.split(" ")[-1].strip("()")}: {agent.rsplit(" ", 1)[0].strip()}</li>' for agent in agent_list)
        html += pattern % (obj_id, title, artist, agent_list_items)

    response = make_response(html)
    return response
