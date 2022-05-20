import requests
from django.conf import settings


def telegram_bot_send_text(username, mail, text):
    bot_token = settings.TELEGRAM.get('bot_token')
    bot_chatID = settings.TELEGRAM.get('channel_id')
    message = f'Username: {username} \nMail: {mail} \nText: {text}'

    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=Markdown&text=' + message

    return requests.get(send_text).json()
