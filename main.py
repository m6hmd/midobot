import requests, user_agent, json, flask, telebot, random, os, sys, time
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

BOT_TOKEN = "1111603340:AAHuKvMBE6z5Sk1rQ_jl-yWi12UVcjBU91U"
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

@bot.message_handler(content_types=["text"])
def S(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Send List ......")
    elif "/" in message.text:
        bot.send_message(message.chat.id, "Send List ......")
    else:
        mes = message.text.splitlines()
        for username in mes:
            username1 = username.replace("@", "")
            url = "https://t.me/" + str(username1)
            headers = {
                    "User-Agent": generate_user_agent(),
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
            response = requests.get(url, headers=headers).text
            if "Send Message" in response:
                if "bot" not in username1:
                    if "@" in username:
                        bot.send_message(message.chat.id, f"{username} is account")
                    else:
                        bot.send_message(message.chat.id, f"@{username} is account")
        bot.send_message(message.chat.id, f"Done list begin with {mes[0}]}")

            elif "subscribers" in response or "Preview channel" in response or "subscriber":
                print("hello")
            time.sleep(5)


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
