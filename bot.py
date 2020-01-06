import telebot
import pyowm

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc',language='ru')
bot = telebot.TeleBot("841873862:AAFebl2ZjNDAAG_Eg35eXG-SDrXSARk1DJk")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')['temp']

	answer = "В вашей бомжатне "  + "сейчас: " + w.get_detailed_status() +'\n'
	answer += "Температура в районе: " + str(temp) + '\n\n'
	if temp < 10:
		answer += "бля холодновато, одевайся теплее"
	if temp > 10 and temp <20:
		answer += "бля 10-20 градусов я хуй знает смотри сам"
	if temp >20 and temp<30:
		answer += "бля заебись погодка, рассекай в шортиках"
	if temp>30:
		answer += "ебать жара нахуй, сиди дома"
	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )
