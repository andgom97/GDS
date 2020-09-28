import json
import os
from prcolors import prRed, prGreen, prLightGray, prLightOrange

DATA_PATH = os.getenv('PS4_DISC')+'/data/'

# Main function to display info in the terminal
def print_prices():
    try:
        new_prices_file = open(DATA_PATH+'new_prices.json','r')
        old_prices_file = open(DATA_PATH+'old_prices.json','r')

        new_prices = json.load(new_prices_file)
        old_prices = json.load(old_prices_file)

        for game in new_prices:
            try:
                new_price = float(new_prices[game])
                old_price = float(old_prices[game])
                if old_price < new_price:
                    prRed(f"{game[:1].upper()+game[1:].replace('-',' ')} : {new_price} ↑")
                elif old_price > new_price:
                    prGreen(f"{game[:1].upper()+game[1:].replace('-',' ')} : {new_price} ↓")
                else:
                    prLightGray(f"{game[:1].upper()+game[1:].replace('-',' ')} : {new_price} -")
            except KeyError:
                prLightGray(f"{game[:1].upper()+game[1:].replace('-',' ')} : {new_price} -")
    except FileNotFoundError:
        prLightOrange(f"Data needs to be downloaded first")

# Display prices
print_prices()