import json
import os
from prcolors import prLightGray, prLightOrange

DATA_PATH = os.getenv('GDS')+'/data/'

# Main function to display info in the terminal
def display_prices():
    try:
        prices_file = open(DATA_PATH+'prices.json','r')
        prices = json.load(prices_file)
        for game in prices:  
            if isinstance(prices[game]['ps'],list):
                original = prices[game]['ps'][0]
                final = prices[game]['ps'][1]
                countdown = prices[game]['ps'][2]
                print(f"\033[97m -> {game.replace('-',' ').capitalize()}:\033[00m \033[91m{original}\033[00m \033[97m->\033[00m \033[92m{final}\033[00m (Until: {countdown})")
            else:
                prLightGray(f"{game.replace('-',' ').capitalize()}: {prices[game]['ps']}")
    
    except FileNotFoundError:
        prLightOrange(f"Data needs to be downloaded first")
    except Exception as e:
        prLightOrange(e)

# Display prices
display_prices()