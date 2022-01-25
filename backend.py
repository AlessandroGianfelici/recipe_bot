import time
import telepot
import os, sys, re
from bot_token import bot_token
from app_ricette.source.constants import APP_PATH

sys.path.append(APP_PATH)

from app_ricette.source.recommender import recommend_recipes
from app_ricette.recommender_app import preprocess_query

bot = telepot.Bot(bot_token)

def handle(msg):
    chat_id = msg['chat']['id']
    if msg['text'] == '/start':
        bot.sendMessage(chat_id, f"Scrimi la lista degli ingredienti che vuoi usare, separati da virgola!")
    if 'text' in msg.keys():
        try:
            ingredients = msg['text']
            if re.sub(r'[^a-zA-Z]', ' ', ingredients.lower().strip()) == 'ciao':
                bot.sendMessage(chat_id, f"Ciao a te! Scrimi la lista degli ingredienti che vuoi usare, separati da virgola!")
                return
            suggestions = recommend_recipes(list(map(preprocess_query, ingredients.lower()\
                                  .replace("peperone", 'peperoni')\
                                  .replace("peperoni", 'peperone, peperoni').split(","))), max_results=1)
            url = suggestions['url'][0]
            bot.sendMessage(chat_id, f"Cosa ne pensi di questa?")
            bot.sendMessage(chat_id, url)
            return 
        except Exception as e:
            print(f"{e}: {e.__doc__}")
            bot.sendMessage(chat_id, f"Non ho capito! Scrimi la lista degli ingredienti che vuoi usare, separati da virgola!")
    return None

bot.message_loop(handle)

while(1):
    time.sleep(1)