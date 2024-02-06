import requests

TOKEN = "6378779878:AAFDYJYA0rZq4sLwvQgzSo-FgE7AJwFQDZg"
URL = "https://api.telegram.org/bot%s/"%TOKEN

proxies = {
   'http': 'socks5://127.0.0.1:9050',
   'https': 'socks5://127.0.0.1:9050'
}

def send_url(url):
    #print(url)
    response = requests.get(url) #, proxies=proxies)
    return response.json()

def json_from_url(url):
    getUpdates = send_url(url)
    return getUpdates

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = json_from_url(url)
    return js

def get_last_update_id(update): # vase ofsset
    return update["update_id"]

def send_message(chat_id, text, reply_markup=dict(), parse_mode=False, reply_to=None):
    if parse_mode == True:
        json = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': 'MarkdownV2',
            'reply_markup': reply_markup,
            'reply_to_message_id': reply_to
        }
    else:
        json = {
            'chat_id': chat_id,
            'text': text,
            'reply_markup': reply_markup,
            'reply_to_message_id': reply_to
        }

    response = requests.post(URL + "sendMessage", json=json)#, proxies=proxies)
    #print(response.json())

def send_sticker(chat_id, sticker_file_id):
    data = {
        'chat_id': chat_id,
        'sticker': sticker_file_id,
    }
    re = requests.post(URL + "sendSticker", data=data) #, proxies=proxies)
    #print(re.json())

def send_document(doc, chat_id):
    files = {'document': open("/home/parisa/Documents/bot.py")}
    requests.post(URL + "sendDocument?chat_id={}".format(chat_id), files=files)

def send_image(chat_id):
    files = {'photo': open("/home/parisa/Pictures/Screenshot_2021-09-13_10_33_09.png")}
    requests.post(URL + "sendPhoto?chat_id={}".format(chat_id), files=files)
