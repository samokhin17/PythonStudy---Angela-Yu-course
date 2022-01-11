import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('b08e922f86cb7fa591888ea372e4845a')
token = "5023209716:AAFNxlBN705X4pHpIJpiiA2KTS8OQWB4CG0"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def send_echo(message):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = w.temperature('celsius')["temp"]

	answer = "В городе " + message.text + " погода сейчас: " + str(w.detailed_status + "\n")
	answer += "Температура в городе " + message.text + ": " + str(temp) + "°" + " по Цельсию" + "\n\n"

	if temp < 10:
		answer += "На улице холодно! Одевайтесь теплее, не забудьте шарф и шапку!" + "\n"
	elif temp < 20:
		answer += "Прохладно! Одевайтесь теплее!" + "\n"
	else:
		answer += "На улице тепло, одевайтесь как удобно!" + "\n"

	bot.send_message(message.chat.id, answer)



bot.infinity_polling()
