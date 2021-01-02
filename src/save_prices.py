from prcolors import prLightGray, prRed, prGreen, prLightOrange
from URLs import GAMES, PS_PRODUCT, STM_PRODUCT
import json
from shutil import copy2
import os
from scrapper import get_game_price_ps, get_game_price_st
import random
from multiprocessing.dummy import Pool as ThreadPool

DATA_PATH = os.getenv('GDS')+'/data/'

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
    print(' -> '+game)
    if not GAMES[game]['ps']:
        return (get_game_price_ps(None),get_game_price_st(STM_PRODUCT+GAMES[game]['st']))
    if not GAMES[game]['st']:
        return (get_game_price_ps(PS_PRODUCT+GAMES[game]['ps']),get_game_price_st(None))
    return (get_game_price_ps(PS_PRODUCT+GAMES[game]['ps']),get_game_price_st(STM_PRODUCT+GAMES[game]['st']))
# Function that saves all the prices randomly and concurrently
def save_prices():
    res = {}
    games = list(GAMES.keys())
    random.shuffle(games)
    with ThreadPool(len(games)) as pool:
        prices = pool.map(save_price,games)
        for i,game in enumerate(games):
            res[game] = {'ps':prices[i][0],'st':prices[i][1]}
    try:
        prices = open(DATA_PATH+'prices.json','w+')        
        prices.write(json.dumps(order_alphabetically(res), indent=4))
        prGreen(f"Data successfully saved")
    except Exception as e:
        prLightOrange(e)    

# Save prices call
save_prices()