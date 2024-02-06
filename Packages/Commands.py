from Packages.Connection import send_message

def start_new_user(chat_id):
    text = f"Hi my new friend✋\!\!\nYour ChatId is `{chat_id}`~`"
    send_message(chat_id, text, parse_mode=True)

def start(chat_id):
    text = f"🤓 I told you\n🆔 Your __*chat id*__ is `{chat_id}`\! "
    send_message(chat_id, text , parse_mode=True)

def help(chat_id):
    text = "You have sended /help command.\nThere is no help.🤷‍♂️💁‍♂️\nYou can ask @mehrsahdina."
    send_message(chat_id, text)

def unknow(chat_id):
    text = "I don't undresstand what you said!🥸\nClick on /start. "
    send_message(chat_id, text)
