import telebot
from telebot import types
from math import pi
bot = telebot.TeleBot('')

expr = ''
keyboard = types.InlineKeyboardMarkup()

key_AC = types.InlineKeyboardButton(text='AC', callback_data='AC')
key_bracket_l = types.InlineKeyboardButton(text='(', callback_data='(')
key_bracket_r = types.InlineKeyboardButton(text=')', callback_data=')')
key_div = types.InlineKeyboardButton(text='/', callback_data='/')
key_7 = types.InlineKeyboardButton(text='7', callback_data='7')
key_8 = types.InlineKeyboardButton(text='8', callback_data='8')
key_9 = types.InlineKeyboardButton(text='9', callback_data='9')
key_mul = types.InlineKeyboardButton(text='*', callback_data='*')
key_4 = types.InlineKeyboardButton(text='4', callback_data='4')
key_5 = types.InlineKeyboardButton(text='5', callback_data='5')
key_6 = types.InlineKeyboardButton(text='6', callback_data='6')
key_sub = types.InlineKeyboardButton(text='-', callback_data='-')
key_1 = types.InlineKeyboardButton(text='1', callback_data='1')
key_2 = types.InlineKeyboardButton(text='2', callback_data='2')
key_3 = types.InlineKeyboardButton(text='3', callback_data='3')
key_add = types.InlineKeyboardButton(text='+', callback_data='+')
key_pi = types.InlineKeyboardButton(text='π', callback_data='pi')
key_zero = types.InlineKeyboardButton(text='0', callback_data='0')
key_dot = types.InlineKeyboardButton(text='.', callback_data='.')
key_equel = types.InlineKeyboardButton(text='=', callback_data='=')

keyboard.row(key_AC, key_bracket_l, key_bracket_r, key_div)
keyboard.row(key_7, key_8, key_9, key_mul)
keyboard.row(key_4, key_5, key_6, key_sub)
keyboard.row(key_1, key_2, key_3, key_add)
keyboard.row(key_pi, key_zero, key_dot, key_equel)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'Напиши здесь математическое выражение через /calc или напиши /help')

@bot.message_handler(content_types=['text'])
def handle_text(message):

    if message.text == '/help':
        bot.send_message(message.from_user.id, f'Привет! \nНапиши мне какое-нибудь математическое выражение через /calc, '
                                               f'и я дам тебе ответ')

    elif message.text == '/calc':
        global expr
        try:
            bot.send_message(message.from_user.id, text=expr, reply_markup=keyboard)
        except:
            bot.send_message(message.from_user.id, text='0', reply_markup=keyboard)

    else:
        bot.send_message(message.chat.id, f'Попробуй еще раз через /calc')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global expr
    if call.data == 'AC':
        expr = ''
    elif call.data == '=':
        try:
            expr = str(eval(expr))
        except:
            expr = 'Такая операция невозможна('
    else:
        expr += str(call.data)

    if expr == '':
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='0',
                                  reply_markup=keyboard)
        except:
            pass
    else:
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=expr,
                                  reply_markup=keyboard)
        except:
            pass


bot.polling(none_stop=True, interval=0)

