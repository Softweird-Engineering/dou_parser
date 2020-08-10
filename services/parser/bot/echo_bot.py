import telebot

bot = telebot.TeleBot("1332015866:AAH4KDr10aXlS4qqXrEvo--p4wIC3bQTTuw")


@bot.message_handler(commands=['health'])
def check_health(message):
	bot.reply_to(message, "Healthy")
	bot.stop_polling()

bot.polling()
