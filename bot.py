# coding=utf-8
import requests

token = '1072488292:AAHCA2i4oh46j_rDbxTPyQSnUpdfWchd65w'
messeges_dict = {
     '1': 'Ну что там с деньгами?',
     '2': 'Как с деньгами-то там?',
     '3': 'Чё с деньгами?',
    }
default_message = 'Ты куда звонишь?! По какому номеру звонишь?'


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = f'https://api.telegram.org/bot{token}/'

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = None
        return last_update


def main():
    new_offset = None

    bot = BotHandler(token)

    while True:
        bot.get_updates(new_offset)

        last_update = bot.get_last_update()

        if last_update is None:
            continue

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']

        if last_chat_text in messeges_dict.keys():
            bot.send_message(last_chat_id, messeges_dict[last_chat_text])
        else:
            bot.send_message(last_chat_id, default_message)
        new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
