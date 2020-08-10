import asyncio
import telebot
# from ..database.services

bot = telebot.TeleBot("1332015866:AAH4KDr10aXlS4qqXrEvo--p4wIC3bQTTuw", threaded=False)


async def start_polling():

	@bot.message_handler(commands=['health'])
	def check_health(message):
		bot.reply_to(message, "healthy")

	@bot.message_handler(commands=['start'])
	def add_new(message):
		bot.reply_to(message, "You was successfully added to database.\n Wait for next new vacancies! ( ^ _ ^) ")

	while True:
		try:
			await asyncio.sleep(2)
			updates = bot.get_updates(offset=(bot.last_update_id + 1), timeout=2)
			bot.process_new_updates(updates)
		except:
			await asyncio.sleep(10)


async def send_message():
	while True:
		bot.send_message(775621366, "sdiufsuodf suidbf uisdb isbdiu")
		await asyncio.sleep(2)


async def main():
	await asyncio.gather(send_message(), start_polling())

asyncio.run(main())
