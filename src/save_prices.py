from prcolors import prLightGray, prRed, prGreen, prLightOrange
from URLs import GAMES, PRODUCT
import json
from shutil import copy2
import os
from scrapper import get_game_price, get_game_prev_price
import random
from multiprocessing.dummy import Pool as ThreadPool

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

# Function that saves the game price on the json file
def save_price(game):
    # If it is discounted
    if get_game_prev_price(PRODUCT+GAMES[game]):
        print(' -> '+game)
        return (get_game_prev_price(PRODUCT+GAMES[game]).replace(',','.'),get_game_price(PRODUCT+GAMES[game]).replace(',','.'))
    else:
        print(' -> '+game)
        return (get_game_price(PRODUCT+GAMES[game]).replace(',','.'),None)

# Function that saves all the prices
def save_prices():
    res = {}
    games = list(GAMES.keys())
    random.shuffle(games)
    with ThreadPool(len(games)) as pool:
        prices = pool.map(save_price,games)
        for i,game in enumerate(games):
            res[game] = prices[i]
    try:
        prices = open(DATA_PATH+'prices.json','w+')        
        prices.write(json.dumps(order_alphabetically(res), indent=4))
        prGreen(f"Data successfully saved")
    except Exception as e:
        prLightOrange(e)
    
# Save prices
save_prices()