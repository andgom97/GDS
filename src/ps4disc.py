from scrapper import get_game_price
from prcolors import prLightGray, prRed, prGreen, prLightOrange
from URLs import GAMES, PRODUCT
import json
from shutil import copy2
import os

DATA_PATH = os.getenv('PS4_DISC_DATA')

# Function that first replaces the old_prices and then saves the new ones
def save_prices():
    res = {}
    # Loop to make the scrapping
    for game in GAMES:
        res[game] = get_game_price(PRODUCT+GAMES[game]).replace(',','.')
    
    # Try to 
    try:
        # Replace the old prices
        copy2(DATA_PATH+'new_prices.json',DATA_PATH+'old_prices.json')
        
    # If exception occurs
    except FileNotFoundError:
        # Create the json file were the new prices will be saved
        open(DATA_PATH+'new_prices.json','w+')
        
        # Replace the old prices
        copy2(DATA_PATH+'new_prices.json',DATA_PATH+'old_prices.json')

    # If other exception occurs, print it
    except Exception as e:
        prLightOrange(e)
    
    finally:
        # open the new_prices.json file and save the results 
        new_prices = open(DATA_PATH+'new_prices.json','w')
        new_prices.write(json.dumps(res, indent=4))
        prGreen(f"Data was successfully saved")

# Main function to display info in the terminal
def print_prices():
    # Open json files with new and old prices
    new_prices_file = open(DATA_PATH+'new_prices.json','r')
    old_prices_file = open(DATA_PATH+'old_prices.json','r')

    # Convert them to dictionaries
    new_prices = json.load(new_prices_file)
    old_prices = json.load(old_prices_file)

    # For each game check if the price got reduced, increased or its the same and print it
    for game in new_prices:
        try:
            old_price = float(old_prices[game])
            new_price = float(new_prices[game])
            if old_price < new_price:
                prRed(f"{game[:1].upper()+game[1:].replace('-',' ')} : {new_price} ↑")
            elif old_price > new_price:
                prGreen(f"{game[:1].upper()+game[1:].replace('-',' ')} : {new_price} ↓")
            else:
                prLightGray(f"{game[:1].upper()+game[1:].replace('-',' ')} : {new_price} -")
        except KeyError:
            prLightGray(f"{game[:1].upper()+game[1:].replace('-',' ')} : {new_price} -")
    

# Exec
print_prices()
