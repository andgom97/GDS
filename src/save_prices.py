from prcolors import prLightGray, prRed, prGreen, prLightOrange
from URLs import GAMES, PRODUCT
import json
from shutil import copy2
import os
from scrapper import get_game_price, get_game_prev_price
from alive_progress import alive_bar
from time import sleep

DATA_PATH = os.getenv('PS4_DISC')+'/data/'

# Function that orders a dictionary alphabetically
def order_alphabetically(dic):
    res = {}
    try:
        sortednames=sorted(dic.keys(), key=lambda x:x.lower())
        for game in sortednames:
            res[game] = dic[game]
        return res
    except Exception as e:
        prLightOrange(e)

# Function that saves prices on a json file
def save_prices():
    res = {}
    games = order_alphabetically(GAMES)
    with alive_bar(len(games), title='Progress', bar='classic',spinner='vertical') as bar:
        for game in games:
            # If it is discounted
            if get_game_prev_price(PRODUCT+games[game]):
                res[game] = (get_game_prev_price(PRODUCT+games[game]).replace(',','.'),get_game_price(PRODUCT+games[game]).replace(',','.'))
            else:
                res[game] = (get_game_price(PRODUCT+games[game]).replace(',','.'),None)
            sleep(0.01)
            bar()
    try:
        prices = open(DATA_PATH+'prices.json','w+')        
        prices.write(json.dumps(res, indent=4))
        prGreen(f"Data successfully saved")
    except Exception as e:
        prLightOrange(e)
    
# Save prices
save_prices()