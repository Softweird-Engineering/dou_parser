import telebot

bot = telebotimport telebot

bot = telebot.TeleBot("1332015866:AAH4KDr10aXlS4qqXrEvo--p4wIC3bQTTuw")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Parsing-Bot started")
