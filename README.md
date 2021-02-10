Games Discount Scraper (GDS)
============================

A Python web scraper to get the desired game prices from the **Playstation**, **Steam** and **Epic Games** stores, while highlighting the discounted ones.

Place the desired games URLs you want to track at the ``GDS/src/URL.py`` file, and the scraper will save them with a **cron process**, which must be configured in first place. 

*Note: You can always force the saving prices process by running the ``GDS/sh/save_prices.sh`` script.*

The following image shows what the ``gds``should display on your terminal:

![alt text](https://github.com/andgom97/GDS/tree/master/res/gds_example.png "GDS command result example")


Configuration
----------------
To configure the environment properly, set the ``$GDS`` variable as described in the ``GDS/config/bash_profile_config.txt`` file, along with the alias to display the prices on the terminal. After that set a **cron process** as described in the ``GDS/config/cron.txt`` file. Feel free to tune the cron frequency and the alias to display the prices as you wish.

Before you start, you will also need to set the ``$CHROMEDRIVER`` varibale equals to the path where the chromedriver file is allocated in your system, e.g. in OSX systems you will be able to find it at ``$HOME/.wdm/drivers/chromedriver/mac64/{version}/chromedriver``. If you don't have the chromedriver installed already. you can always download the latest version [here](https://chromedriver.chromium.org/downloads).

HTTP API 
-----------
The ``GDS/src/api/`` directory contains the source code to make http requests and get the game prices you want to track remotely.
To start the HTTP API listener process run the main.py file like this:
```
$ python main.py
```

File organization
--------------------
* ``GDS/sh/``: **Shell** scripts to **turn on the web scrapper** and **display** the data on your terminal.
* ``GDS/config/``: **Text files** with **configuration hints**.
* ``GDS/data/``: **Json** files which contain **the scraped data**.
* ``GDS/src/``: **Python** source code.
