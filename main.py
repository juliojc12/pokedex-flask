from models.pokemon import Pokemon
from flask import Flask, render_template
import requests
import logging

logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    resquest = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
    print(resquest.json())

    pokemons = []
    for pokemon in resquest.json()['results']:
        pokemons.append(
            Pokemon(pokemon['name'], pokemon['url']))
    return render_template('index.html', pokemons=pokemons)


@app.route('/<name>/')
def about(name=None):
    return render_template('about.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
