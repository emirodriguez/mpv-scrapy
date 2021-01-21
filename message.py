import requests

def send_message(chat_id, text):
    bot = 'https://api.telegram.org/bot1409231480:AAFleUQe3p4R2gw5dN3OyKcSpqdthswVTDg/'
    
    parameters = {'chat_id': chat_id, 'text': text}
    message = requests.post(bot + 'sendMessage', data=parameters)