import requests

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

from URLs import PSSTR_SEARCH
from prcolors import prLightOrange, prRed
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

# Function to get game price from the Playstation store (if discounted the function returns a tuple with the following strucure:
# ('original price value','final price value,'countdown_value'))
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

# Function to get game price from Steam (if discounted the function returns a tuple with the following strucure:
# ('original price value','final price value,'countdown_value'))
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

# Function to get game price from the Epic Games store (if discounted the function returns a tuple with the following strucure:
# ('original price value','final price value,'countdown_value'))
def get_game_price_ep(url):
    if not url:
        return None
    try:
        # Chrome options
        chrome_options = webdriver.ChromeOptions()
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        chrome_options.add_argument(f'user-agent={user_agent}') # user_agent
        chrome_options.add_argument('--headless') # headless mode
        chrome_options.add_argument('--incognito') # incognito mode
        # Webdriver
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        driver.get(url)
        # WebDriverWait() until price data is loaded
        timeout = 5
        try:
            price_section = EC.presence_of_element_located((By.CLASS_NAME,'css-r6gfjb-PurchasePrice__priceContainer'))
            WebDriverWait(driver, timeout).until(price_section)
        except TimeoutException:
            print("Timed out waiting for prices to load")

        
        # BeautifulSoup
        soup = BeautifulSoup(driver.page_source.encode('utf-8').strip(),'html.parser')

        # Check if price appears on the top section
        price_top_section = soup.find('div',class_='css-4tpn3e')
        if price_top_section:
            prices = price_top_section.findAll(attrs={'data-component':'Price'})
            if len(prices)<2: # If not discounted
                return prices[0].text[:-2].replace(',','.')
            else: # If discounted
                countdown_section = soup.find('div',attrs={'data-component':'PurchaseCaption'}).find('span',attrs={'data-component':'Message'})
                countdown_value = countdown_section.text.split()[4].split('/')
                countdown_month = MONTHS.get(int(countdown_value[1]), None)
                return (prices[0].text[:-2].replace(',','.'),prices[1].text[:-2].replace(',','.'),countdown_value[0]+'-'+countdown_month)
        # Check if price appears on the bot section
        else:
            products = soup.findAll('div',attrs={'data-component':'ProductCard'})
            price_section = products[0].find('div',attrs={'data-component':'PriceLayout'})
            prices = price_section.findAll(attrs={'data-component':'Price'})
            if len(prices)<2: # If not discounted
                return prices[0].text[:-2].replace(',','.')
            else: # If discounted
                countdown_section = price_section.find('div',attrs={'data-component':'PurchaseCaption'}).find('span',attrs={'data-component':'Message'})
                countdown_value = countdown_section.text.split()[4].split('/')
                countdown_month = MONTHS.get(int(countdown_value[1]), None)
                return (prices[0].text[:-2].replace(',','.'),prices[1].text[:-2].replace(',','.'),countdown_value[0]+'-'+countdown_month)
    except AttributeError:
        print('-> AttributeError')
        return None

        
# ------------- Price in top section ---------------
# Discounted
#print(get_game_price_ep('https://www.epicgames.com/store/es-ES/product/monkey-barrels/home'))
# Not discounted
#print(get_game_price_ep('https://www.epicgames.com/store/es-ES/product/super-meat-boy-forever/home'))

# ------------- Price in bot section ---------------
# TODO FAILS SOMETIMES when the price is in the bot section
# Discounted
#print(get_game_price_ep('https://www.epicgames.com/store/es-ES/product/werewolf-the-apocalypse-earthblood/home'))
# Not discounted
#print(get_game_price_ep('https://www.epicgames.com/store/es-ES/product/assassins-creed-origins/home'))
#print(get_game_price_ep('https://www.epicgames.com/store/es-ES/product/star-wars-jedi-fallen-order/home'))
#print(get_game_price_ep('https://www.epicgames.com/store/es-ES/product/mafia-ii-definitive-edition/home'))