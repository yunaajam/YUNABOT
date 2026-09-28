import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.tgju.org/profile/geram18')
datahtml = BeautifulSoup(data.text, 'html.parser')
prices = datahtml.find_all('span', value={'class' : 'info.last_trade.PDrCotVal'})

for price in prices:
    price.get_text()
    print(price.get_text())

for price in prices:
    price.get_text()
    print(price.get_text())

token = '8879197490:AAGZ9CwTUq9CqtGnJxQNt0n75nBdaR8bMiU'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(" طلا 18 عیار", callback_data="18"))
    kb.add(InlineKeyboardButton(" طلا 24 عیار", callback_data="24"))
    bot.send_message(message.chat.id, "یک گزینه را انتخاب کن:", reply_markup=kb)

@bot.message_handler(commands=['Start'])
def start(message):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(" طلا 18 عیار", callback_data="18"))
    kb.add(InlineKeyboardButton(" طلا 24 عیار", callback_data="24"))
    bot.send_message(message.chat.id, "یک گزینه را انتخاب کن:", reply_markup=kb)

@bot.message_handler(commands=['START'])
def start(message):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(" طلا 18 عیار", callback_data="18"))
    kb.add(InlineKeyboardButton(" طلا 24 عیار", callback_data="24"))
    bot.send_message(message.chat.id, "یک گزینه را انتخاب کن:", reply_markup=kb)



@bot.message_handler(commands=['yuna'])
def start(message):
    bot.send_message(message.chat.id , 'بله با من هستید ؟')

@bot.message_handler(commands=['YUNA'])
def start(message):
    bot.send_message(message.chat.id , 'بله با من هستید ؟')

@bot.message_handler(commands=['Yuna'])
def start(message):
    bot.send_message(message.chat.id , 'بله با من هستید ؟')


@bot.message_handler(commands=['hi'])
def start(message):
    bot.send_message(message.chat.id , 'سلام خوش امدید ')

@bot.message_handler(commands=['HI'])
def start(message):
    bot.send_message(message.chat.id , 'سلام خوش امدید ')

@bot.message_handler(commands=['Hi'])
def start(message):
    bot.send_message(message.chat.id , 'سلام خوش امدید ')


@bot.message_handler(commands=['yes'])
def start(message):
    bot.send_message(message.chat.id , '  سوال تون چیست ؟')

@bot.message_handler(commands=['YES'])
def start(message):
    bot.send_message(message.chat.id , '  سوال تون چیست ؟')

@bot.message_handler(commands=['Yes'])
def start(message):
    bot.send_message(message.chat.id , '  سوال تون چیست ؟')

@bot.message_handler(commands=['gold24'])
def start(message):
    bot.send_message ( message.chat.id , price.get_text())

@bot.message_handler(commands=['Gold24'])
def start(message):
    bot.send_message ( message.chat.id , price.get_text())

@bot.message_handler(commands=['GOLD24'])
def start(message):
    bot.send_message ( message.chat.id , price.get_text())

@bot.callback_query_handler(func=lambda call: call.data == "18")
def button(call):
    data = requests.get('https://www.tgju.org/gold-chart')
    datahtml = BeautifulSoup(data.text, 'html.parser')
    prices = datahtml.find_all('td', attrs={'class' : 'nf'})
    bot.send_message ( call.message.chat.id , prices[0].get_text())

@bot.callback_query_handler(func=lambda call: call.data == "24")
def button(call):
    data = requests.get('https://www.tgju.org/gold-chart')
    datahtml = BeautifulSoup(data.text, 'html.parser')
    prices = datahtml.find_all('td', attrs={'class' : 'nf'})
    bot.send_message ( call.message.chat.id , prices[4].get_text())


bot.infinity_polling()