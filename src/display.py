import json
from prcolors import prLightGray, prLightOrange
from const import DATA_PATH

# Main function to display info in the terminal
def display_prices():
    try:
        prices_file = open(DATA_PATH+'prices.json','r')
        prices = json.load(prices_file)
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(f"\033[97m |           Videogame             |           Playstation Store           |                 Steam                 |            Epic Games Store           |\033[00m")
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
        for game in prices:  
            name = game.replace('-',' ').capitalize()
            ps_str = ''
            st_str = ''
            while len(name)<30:
                name += ' '
            
            # If the game is discounted on the ps store
            if isinstance(prices[game]['ps'],list):
                original_ps = prices[game]['ps'][0]
                final_ps = prices[game]['ps'][1]
                countdown_ps = prices[game]['ps'][2]
                ps_str = f"\033[91m{original_ps}\033[00m \033[97m->\033[00m \033[92m{final_ps}\033[00m (Until: {countdown_ps})"
                while len(ps_str)<65:
                    ps_str += ' '
            # If not
            else:
                price = prices[game]['ps']
                if not price:
                    price = '-----'
                ps_str = f"\033[97m               {price}\033[00m"
                while len(ps_str)<45:
                    ps_str += ' '
            
            # If the game is discounted on steam
            if isinstance(prices[game]['st'],list):
                original_st = prices[game]['st'][0]
                final_st = prices[game]['st'][1]
                countdown_st = prices[game]['st'][2]
                st_str = f"\033[97m|\033[91m  {original_st}\033[00m \033[97m->\033[00m \033[92m{final_st}\033[00m (Until: {countdown_st})"
                while len(st_str)<73:
                    st_str += ' '
            # If not
            else:
                price = prices[game]['st']
                if not price:
                    price = '-----'
                st_str = f"\033[97m|                 {price}\033[00m"
                while len(st_str)<48:
                    st_str += ' '
            
            # If the game is discounted on the epic games store
            if isinstance(prices[game]['ep'],list):
                original_ep = prices[game]['ep'][0]
                final_ep = prices[game]['ep'][1]
                countdown_ep = prices[game]['ep'][2]
                ep_str = f"\033[97m|\033[91m  {original_ep}\033[00m \033[97m->\033[00m \033[92m{final_ep}\033[00m (Until: {countdown_ep})  \033[97m|\033[00m"
                while len(ep_str)<73:
                    ep_str += ' '
            # If not
            else:
                price = prices[game]['ep']
                if not price:
                    price = '-----'
                ep_str = f"\033[97m|                 {price}                 |\033[00m"
                while len(ep_str)<47:
                    ep_str += ' '
            print(f"\033[97m -> {name} | \033[00m {ps_str}  {st_str}  {ep_str}")
    except FileNotFoundError:
        prLightOrange(f"Data needs to be downloaded first")
    except Exception as e:
        prLightOrange(e)

# Display prices
display_prices()