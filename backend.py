import time
import telepot
import os, sys
from bot_token import bot_token



def handle(msg):
    chat_id = msg['chat']['id']
    if 'text' in msg.keys():
        bot.sendMessage(chat_id, f"Give me the list of the ingredients you have, separated by comma!")
        
    return None

bot = telepot.Bot(bot_token)
bot.message_loop(handle)

while(1):
    time.sleep(1)