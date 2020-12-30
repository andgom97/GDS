## PlayStation 4 videogames discounts web scrapper

Python web scrapper to get the desired playstation 4 games prices and highlight those ones with a discount.

Place the desired games URLs from the PlayStation Store you want to track at the src/URL.py file, and the scrapper will save them with a cron, which must be configured in first place.

# Configuration
To configure the environment properly, go to config/ directory and set the $PS4_DISC variable as described at the bash_profile_config.txt file in your .bash_profile, along with the alias to display the prices on terminal. After that set a cron as described at the cron.txt file in your system. Feel free to tune the cron frequency and the alias to display the prices as you wish.

# HTTP API 
The /api directory contains the source code that allows you to make http requests and get the game prices you want to track.
Do 'python main.py' to start the listener process.