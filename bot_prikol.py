import telebot
import webbrowser
import random
from telebot import types
bot = telebot.TeleBot(token='6687248700:AAHLzbXXXlQlJMF6dn-eVtb8iNlP6thR2Mc')

@bot.message_handler(commands = ['start'] )
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    prikol_button=types.KeyboardButton('z0rg prikol')
    markup.add(prikol_button)
    bot.send_message( message.chat.id, f'Zdarova Bratik', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def buttons(message):
    if (message.text == 'z0rg prikol'):
        prikol_id = random.randint(0, 8025)
        webbrowser.open(f'https://z0r.de/{prikol_id}?ruffle')











bot.polling(none_stop=True,interval=0)