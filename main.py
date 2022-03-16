import requests, user_agent, json, flask, telebot, random, os, sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

BOT_TOKEN = "1196044747:AAFzqG3jFuaeyeG6BddflCWxgZ-RqoOHm1c"
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(content_types=['text'])
def getID(message):
    check = 0
    more = 0
    less = 0
    pastebin = message.text

    idS = requests.get(str(pastebin)).text.splitlines()

    sendM = bot.send_message(message.chat.id, f'-ID : 000000000\nCHECK : {str(check)}\nPastebin : {pastebin}')
    for fil in idS:
        bot.edit_message_text(chat_id=message.chat.id, message_id=sendM.message_id,
                              text=f'- ID : {fil}\nCHECK : {str(check)}\nMore 800 : {str(more)}\nLess 800 : {str(less)}\nPastebin : {pastebin}')
        url = f"https://fluidhighserver.mohammedhaiderz.repl.co/?id={fil}"
        chk = requests.get(url).text
        if '"successful+800"' in chk:
            more += 1
        elif '"successful-800"' in chk:
            less += 1
        elif '"not coin"' in chk:
            pass
        else:
            pass
        check += 1

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
