from random import randint

running = True

while running:
    print("\n" + "Проверь свою удачу!")
    print("Мы загадали число от 1 до 5. Твоя задача - угадать его!" + "\n")

    r = randint(1, 5)

    n = int(input("Введи любое целое число от 1 до 5: " + "\n"))

    if n != r:
        print("К сожалению, ты не угадал. Загаданное число = " + str(r) + "\n")
    else:
        print("Поздравляем! Вы угадали! Загаданное число = " + str(r) + "\n")

    reboot = input("Еще раз? Да/Нет: " + "\n")

    if reboot == "Да" or reboot == "да":
        running = True
    elif reboot == "Нет" or reboot == "нет":
        break
    else:
        print("Выбрана неверная операция!" + "\n")





