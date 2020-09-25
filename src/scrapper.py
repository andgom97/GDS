import requests
from bs4 import BeautifulSoup
from URLs import SEARCH_FOR_GAME
from prcolors import prLightOrange, prRed
from shutil import copy2
import json

# Function that returns the object from the http request
def get_resource(url):
    try:
        page = requests.get(url)
        if not page.ok:
            prRed(f"Error getting resource: {url}")
            prLightOrange(f"Response code: {page}")
            return None
        return page
    except Exception as e:
        prRed('Error getting resource')
        prLightOrange(e)
        return None

# Function that gets the price of a game
def get_game_price(url):
    page = get_resource(url)
    try:
        soup = BeautifulSoup(page.content,'html.parser')
        game_price = soup.find('h3',class_='price-display__price')
        return game_price.text[:-2] 
    except AttributeError:
        return None

# Function to search the url of a game giving its name
def search_game(game):
    search = get_resource(SEARCH_FOR_GAME+game)
    game_url = ''
    try:
        soup = BeautifulSoup(search.content,'html.parser')
        game_field = soup.find('div',class_='grid-cell grid-cell--game')
        for ref in game_field.find_all('a',href=True):
            game_url = ref['href']
    except AttributeError:
        prLightOrange(f"Game: {game} couldn't be found")
    finally:
        return game_url

