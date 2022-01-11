import pyowm
owm = pyowm.OWM('b08e922f86cb7fa591888ea372e4845a')

place = input("Введите город/страну: ")

observation = owm.weather_at_place("Москва")
w = observation.get_weather()
print(w)