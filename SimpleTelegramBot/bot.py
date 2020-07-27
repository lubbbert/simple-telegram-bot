import requests

class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = f'https://api.telegram.org/bot{TOKEN}/'

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
            last_update = get_result[len(get_result)]
        return last_update

token = '1072488292:AAHCA2i4oh46j_rDbxTPyQSnUpdfWchd65w'
messeges_list = ['1', '2', '3']
bot = BotHandler(token)

def main():
    new_offset = None

    while True:
        bot.get_updates(new_offset)

        last_update = bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text in messeges_list:
            if (last_chat_text == '1'):
                bot.send_message(last_chat_id, 'Ну что там с деньгами?')
            if (last_chat_text == '2'):
                bot.send_message(last_chat_id, 'Как с деньгами-то там?')
            if (last_chat_text == '3'):
                bot.send_message(last_chat_id, 'Чё с деньгами?')
        else:
            bot.send_message(last_chat_id, 'Ты куда звонишь?! По какому номеру звонишь?')

        new_offset = last_update_id + 1

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()