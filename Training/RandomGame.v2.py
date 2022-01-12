from random import randint

print("\n" + "Проверь свою удачу!")
print("Мы загадали число от 1 до 100. Твоя задача - угадать его за наименьшее количество попыток!" + "\n")
print("Не волнуйся, компьютер будет тебе подсказывать!")

run = True

while run:
    count = 0

    r = randint(1, 101)

    n = int(input("Введи любое целое число от 1 до 100: \n"))

    while n != r:
        if n > r:
            count += 1
            print("Меньше!\n")
        if n < r:
            count += 1
            print("Больше!\n")
        n = int(input("Попробуй снова: \n"))
    print("Поздравляем! Вы угадали число за " + str(count + 1) + " попыток!\n")

    rerun = True

    reboot = input("Еще раз? Да/Нет: " + "\n")

    if reboot == "Да" or reboot == "да":
        run = True
        continue
    elif reboot == "Нет" or reboot == "нет":
        break
    else:
        print("Выбрана неверная операция!" + "\n")
    if input("Хотите продолжить? Да/Нет ") == "Да" or input("Хотите продолжить? Да/Нет ") == "да":
        run = True
    else:
        break




