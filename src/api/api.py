from flask import request, jsonify

from file import read_prices
from errors import *

games = read_prices()

def get_game(name):
    for game in games:
        if game==name:
            return game
    return None

@app.route('/api/v1', methods=['GET'])
def home():
    html ='''<h1>PS4 discount scrapper API 1.0</h1>
            <p>Backend API for PS4 discount scrapper application.</p>'''
    return html

@app.route('/api/v1/resources/games', methods=['GET'])
def get_games():
    query_parameters = request.args
    name = query_parameters.get('name')
    res = games
    if name:
        res = list(filter(lambda game: game.startswith(name),res))
    return jsonify({game:games[game] for game in res})

@app.route('/api/v1/resources/games/<name>', methods=['GET'])
def get_game_info(name):
    game = get_game(name)
    if game:
        return jsonify({game:games[game]})
    return page_not_found(404)