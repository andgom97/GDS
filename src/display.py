import json
import os
from prcolors import prRed, prGreen, prLightGray, prLightOrange

DATA_PATH = os.getenv('PS4_DISC')+'/data/'

# Main function to display info in the terminal
def print_prices():
    try:
        prices_file = open(DATA_PATH+'prices.json','r')
        prices = json.load(prices_file)

        for game in prices:  
            base = prices[game][0]
            disc = prices[game][1]
            if disc:
                print(f"\033[97m -> {game[:1].upper()+game[1:].replace('-',' ')} :\033[00m \033[91m{base}\033[00m \033[97m -> \033[00m \033[92m{disc}\033[00m")
            else:
                prLightGray(f"{game[:1].upper()+game[1:].replace('-',' ')} : {base}")
    
    except FileNotFoundError:
        prLightOrange(f"Data needs to be downloaded first")
    except Exception as e:
        prLightOrange(e)

# Display prices
print_prices()