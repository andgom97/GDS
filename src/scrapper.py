import requests
from bs4 import BeautifulSoup
from URLs import *
from prcolors import *

# Function that returns the object from the http request
def get_resource(url):
    # Http request to https://store.playstation.com
    try:
        page = requests.get(url)
        # If not 200 return None
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