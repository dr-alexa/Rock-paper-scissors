import telebot
from telebot import types
from dotenv import load_dotenv
import os


load_dotenv()
token_tg = os.getenv('TOKEN_TG')
bot = telebot.TeleBot(token_tg)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Ножницы', callback_data='scissors')
    markup.row(button1)
    button2 = types.InlineKeyboardButton('Камень', callback_data='rock')
    button3 = types.InlineKeyboardButton('Бумага', callback_data='paper')
    markup.row(button2, button3)
    bot.reply_to(message,'Хэй, пользователь! Выбирай способ победы:', reply_markup=markup)
    bot.register_next_step_handler(message, callback_mess)

@bot.callback_query_handler(func=lambda call: True)
def callback_mess(call):
    bot.answer_callback_query(call.id)
    if call.data == 'scissors':
        bot.send_message(call.message.chat.id, 'Камень. Упс! Реванш?')
    elif call.data == 'rock':
        bot.send_message(call.message.chat.id, 'Бумага. Упс! Реванш?')
    elif call.data == 'paper':
        bot.send_message(call.message.chat.id, 'Ножницы. Упс! Реванш?')


bot.polling(none_stop=True)