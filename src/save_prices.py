from prcolors import prLightGray, prRed, prGreen, prLightOrange
from URLs import GAMES, PRODUCT
import json
from shutil import copy2
import os
from scrapper import get_game_price
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

# Function that first replaces the old_prices and then saves the new ones
def save_prices():
    res = {}
    games = order_alphabetically(GAMES)
    with alive_bar(len(games), title='Progress', bar='classic',spinner='vertical') as bar:
        for game in games:
            res[game] = get_game_price(PRODUCT+games[game]).replace(',','.')
            sleep(0.01)
            bar()
    try:
        copy2(DATA_PATH+'new_prices.json',DATA_PATH+'old_prices.json')
    except FileNotFoundError:
        old_prices = open(DATA_PATH+'old_prices.json','w+')
        old_prices.write(json.dumps(res,indent=4))
    except Exception as e:
        prLightOrange(e)
    finally:
        new_prices = open(DATA_PATH+'new_prices.json','w+')        
        new_prices.write(json.dumps(res, indent=4))
        prGreen(f"Data successfully saved")

# Save prices
save_prices()