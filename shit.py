import ttbotapi , requests, json, threading
tok = str(input("Token :: "))
abu_jasim = {}
def check(update):
    user = []
    count = 0
    if ":" in update.message.body.text and update.message.body.text.split(":")[0] != '' and update.message.body.text.split(":")[1] != '':
        username = update.message.body.text.split(":")[1]
        user.append(username)
        abu_jasim.setdefault(user[0], 0)
        token = update.message.body.text.split(":")[0]
        url = "https://botapi.tamtam.chat/"
        params = {"access_token": token}
        method = 'me'
        data = {
            "username": username
        }

        bot.send_message(text="[+]Username :: {}\nStarted ....".format(user[0]), user_id=update.message.sender.user_id , chat_id=None)
        while True:
            response = requests.patch(url + method, params=params, data=json.dumps(data)).text
            # if '"This name is already in use"' in response :
            print(response)
            if '"username":"{}"'.format(username) in response:
                bot.send_message(text="[+]Done Hunted\n— — — —\n[+]Username :: {}\n[+]Requests Number :: {}".format(
                                     username, abu_jasim[username]), user_id=update.message.sender.user_id , chat_id=None)
                a = requests.patch(url + method, params=params, data=json.dumps(data)).text
                abu_jasim.pop(username)
                print(str(a))
                break
            elif 'Invalid' in response:
                bot.send_message(text='Send Right Token', user_id=update.message.sender.user_id , chat_id=None)
                abu_jasim.pop(username)
                break
            else:
                abu_jasim[user[0]] += 1
                print("[+]Username :: {}\n[+]Requests Number :: {}".format(user[0], abu_jasim[user[0]]))

    elif "/check" in update.message.body.text:
        if len(abu_jasim) > 0:
            for item in abu_jasim:
                bot.send_message(text=
                                 "[+]Username :: {}\n[+]Requests Number :: {}".format(item, abu_jasim[item]), user_id=update.message.sender.user_id , chat_id=None)
        else:
            bot.send_message(text="[+]Not Found Username ...", user_id=update.message.sender.user_id , chat_id=None)
    else:
        bot.send_message(text="[+]Send Information Like :\nToken:username", user_id=update.message.sender.user_id , chat_id=None)

bot = ttbotapi.Bot(access_token=tok)

@bot.update_handler(chat_type='dialog')
def send_hi(update):
    threading.Thread(target=check, args=[update]).start()


bot.polling()

