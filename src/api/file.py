import json, os, sys

SRC_PATH = os.getenv('GDS')+'/src/'
DATA_PATH = os.getenv('GDS')+'/data/'

sys.path.insert(1, SRC_PATH)
from prcolors import prLightGray, prLightOrange

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