from pyowm import OWM
from pyowm.utils.config import get_default_config
import colorama

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('b08e922f86cb7fa591888ea372e4845a')

while True:

    print("Узнай погоду в твоем городе!")
    place = input("Введите город: ")

    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    # w.detailed_status - точное описание погоды
    print("\n" + "В городе " + place + " погода сейчас: " + str(w.detailed_status) + "\n")
    print("Температура в городе " + place + ": " + str(temp) + " по Цельсию" + "\n")

    if temp < 10:
        print("На улице холодно! Одевайтесь теплее, не забудьте шарф и шапку!" + "\n")
    elif temp < 20:
        print("Прохладно! Одевайтесь теплее!" + "\n")
    else:
        print("На улице тепло, одевайтесь как удобно!" + "\n")




