import asyncio
import telebot
from ..project.controller import new_user, process_feed

bot = telebot.TeleBot("1332015866:AAH4KDr10aXlS4qqXrEvo--p4wIC3bQTTuw", threaded=False)


async def start_polling():

	@bot.message_handler(commands=['health'])
	def check_health(message):
		bot.reply_to(message, "healthy")

	@bot.message_handler(commands=['start'])
	def add_new(message):
		if new_user(int(message.chat['chat_id'])):
			print(message.chat['chat_id'])
			bot.reply_to(message, "You was successfully added to database.\n Wait for next new vacancies! ( ^ _ ^) ")
	while True:
		try:
			await asyncio.sleep(5)
			updates = bot.get_updates(offset=(bot.last_update_id + 1), timeout=2)
			bot.process_new_updates(updates)
		except:
			await asyncio.sleep(20)


async def check_for_new_jobs(url):
	while True:
		# TODO: connect to service
		# TODO: run a delivery by chat id
		for resp in process_feed(url):
			for user_id in resp.users_id:
				print('checking______________________________________________')
				img = open(resp.image, 'rb')
				print('loaded______________________________________________', img.readable())
				bot.send_photo(user_id, img, resp.message)
				print('sent______________________________________________')
				img.close()
		await asyncio.sleep(100)


async def main(url):
	await asyncio.gather(check_for_new_jobs(url), start_polling())


def start(url):
	new_user(775621366)
	asyncio.run(main(url))