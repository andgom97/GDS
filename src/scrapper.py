import requests
from bs4 import BeautifulSoup
from URLs import PSSTR_SEARCH
from prcolors import prLightOrange, prRed
from shutil import copy2
import json
from const import MONTHS


# Function that returns the object from the http request
def get_resource(url):
    try:
        page = requests.get(url)
        if not page.ok:
            prRed(f"Error getting resource: {url}")
            prLightOrange(f"Response code: {page}")
            return None
        return page
    except Exception as e:
        prRed('Error getting resource')
        prLightOrange(e)
        return None

# Function that gets the name of a game
def get_game_name(url):
    page = get_resource(url)
    try:
        soup = BeautifulSoup(page.content,'html.parser')
        game_name = soup.find('h2',class_='pdp__title')
        return game_name.text
    except AttributeError:
        prLightOrange(f"Wrong url: {url}")
        return None

# Function to search the url of a game giving its name on the Playstation store
def search_game(game):
    search = get_resource(PSSTR_SEARCH+game)
    game_url = ''
    try:
        soup = BeautifulSoup(search.content,'html.parser')
        game_field = soup.find('div',class_='grid-cell grid-cell--game')
        for ref in game_field.find_all('a',href=True):
            game_url = ref['href']
    except AttributeError:
        prLightOrange(f"Game: {game} couldn't be found")
    finally:
        return game_url

# Function to get game price from the Playstation store (if discounted the function returns a dictionary with the following strucure:
# {'original':og_price_value,'final':fn_price_value,'countdown':countdown_value})
def get_game_price_ps(url):
    if not url:
        return None
    page = get_resource(url)
    try:
        soup = BeautifulSoup(page.content,'html.parser')
        price_section = soup.find('label',attrs={'data-qa':'mfeCtaMain#offer0'})
        # Extract standard price
        fn_game_price = price_section.find('span',class_='psw-h3')
        # Extract final price
        og_game_price = price_section.find('span',class_='psw-h4 psw-c-secondary psw-text-strike-through')
        if not og_game_price: # If not discounted
            return fn_game_price.text[:-2].replace(',','.')
        # Extract discount countdown
        countdown_str = price_section.find('span',class_='psw-p-l-xs psw-body-2 psw-text-medium psw-c-secondary psw-m-x-3xs psw-m-y-4xs')
        countdown_value = countdown_str.text.split()[-1:][0].split('/')
        # Translate number to name of the month
        countdown_month = MONTHS.get(int(countdown_value[1]), None)
        return (og_game_price.text[:-2].replace(',','.'),fn_game_price.text[:-2].replace(',','.'),countdown_value[0]+'-'+countdown_month) 
    except AttributeError:
        return None

# Function to get game price from Steam (if discounted the function returns a dictionary with the following strucure:
# {'original':og_price_value,'final':fn_price_value,'countdown':countdown_value})
def get_game_price_st(url):
    if not url:
        return None
    page = get_resource(url)
    try:
        soup = BeautifulSoup(page.content,'html.parser')
        price_area = soup.find('div',class_='game_area_purchase_game_wrapper')
        # Extract standard price
        price = price_area.find('div',class_='game_purchase_price price')
        if not price: # If discounted
            # Extract original and final prices
            og_price_value = price_area.find('div',class_='discount_original_price')
            fn_price_value = price_area.find('div',class_='discount_final_price')
            # Extract countdown
            countdown_str = price_area.find('p',class_='game_purchase_discount_countdown').text
            countdown_value = countdown_str.split()[-2:]
            return (og_price_value.text[:-1].replace(',','.'),fn_price_value.text[:-1].replace(',','.'),countdown_value[0]+'-'+countdown_value[1])
        return price.text[9:14].replace(',','.')
    except AttributeError:
        return None