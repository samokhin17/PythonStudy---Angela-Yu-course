from colorama import init
init()
from colorama import Fore, Back, Style

# Калькулятор v.2


what = input("Что делаем? (+, -): ")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if what == "+":
    c = a + b
    print("Результат " + str(c))
elif what == "-":
    c = a - b
    print("Результат " + str(c))
else:
    print("Выбрана неверная операция")
input()
