import telebot
import requests
bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'Ты можешь отправить мне мне ссылку на какой-нибудь сайт или написать /help.')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/help':
        bot.send_message(message.from_user.id, 'Привет! \nТы можешь отправить мне ссылку на сайт, и я проверю доступен ли он')

    elif message.text:
        user_msg = message.text
        try:
            status_code = requests.get(user_msg).status_code
        except:
            bot.send_message(message.from_user.id, 'Этот сайт недоступен или это не сайт')
        else:
            if status_code == 200:
                bot.send_message(message.from_user.id, 'Этот сайт доступен!')
            elif status_code == 400:
                bot.send_message(message.from_user.id, f'Код ошибки {status_code} - Bad Request ')
            elif status_code == 403:
                bot.send_message(message.from_user.id, f'Код ошибки {status_code} - Forbidden ')
            elif status_code == 404:
                bot.send_message(message.from_user.id, f'Код ошибки {status_code} - Not Found')
            else:
                bot.send_message(message.from_user.id, f'Сайт недоступен или к нему нельзя получить доступ. Код ошибки {status_code}')

bot.polling(none_stop=True, interval=0)
