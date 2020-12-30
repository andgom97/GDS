import json, os, sys
sys.path.insert(1, '../')
from prcolors import prLightGray, prLightOrange

DATA_PATH = os.getenv('PS4_DISC')+'/data/'

# Function that reads the prices allocated in ../data/prices.json
def read_prices():
    prices = None
    try:
        prices_file = open(DATA_PATH+'prices.json','r')
        prices = json.load(prices_file)
    except FileNotFoundError:
        prLightOrange(f"Data needs to be downloaded first")
    except Exception as e:
        prLightOrange(e)
    return prices