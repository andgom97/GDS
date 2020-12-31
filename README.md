Videogames discount web scrapper
===============================

Python web scrapper to get the desired game prices from the **Playstation**, **Steam** and **Epic Games** stores, while highlighting the discounted ones.

Place the desired games URLs you want to track at the ``GDS/src/URL.py`` file, and the scrapper will save them with a **cron process**, which must be configured in first place. 

*Note: You can always force the saving prices process by running the ``GDS/sh/save_prices.sh`` script.*

Configuration
----------------
To configure the environment properly, set the ``$GDS`` variable as described in the ``GDS/config/bash_profile_config.txt`` file, along with the alias to display the prices on the terminal. After that set a **cron process** as described in the ``GDS/config/cron.txt`` file. Feel free to tune the cron frequency and the alias to display the prices as you wish.

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
* ``GDS/data/``: **Json** files which contain **the scrapped data**.
* ``GDS/src/``: **Python** source code.
