import time
import telepot
import os, sys
from bot_token import bot_token
from app_ricette.source.constants import APP_PATH

sys.path.append(APP_PATH)

from app_ricette.source.recommender import recommend_recipes
from app_ricette.recommender_app import preprocess_query

bot = telepot.Bot(bot_token)

def handle(msg):
    chat_id = msg['chat']['id']
    print(msg)
    if msg['text'] == '/start':
        bot.sendMessage(chat_id, f"Give me the list of the ingredients you have, separated by comma!")
    elif 'text' in msg.keys():
        ingredients = msg['text']
        ingredient_list = list(map(preprocess_query, 
                                   ingredients.split(",")))
        suggestions = recommend_recipes(ingredient_list, max_results=1)
        name = suggestions['name'][0]
        url = suggestions['url'][0]
        bot.sendMessage(chat_id, f"What about {name}? Take a look at the recipe:")
        bot.sendMessage(chat_id, url)
        return 
    return None

bot.message_loop(handle)

while(1):
    time.sleep(1)