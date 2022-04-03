MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Вычитание ингредиентов кофе из общего ресурса
def resourses(resources, menu):
    water = resources['water'] - menu['ingredients']['water']
    if 'milk' in menu['ingredients']:
        milk = resources['milk'] - menu['ingredients']['milk']
    else:
        milk = resources['milk']
    coffee = resources['coffee'] - menu['ingredients']['coffee']
    return {
        "water": water,
        "milk": milk,
        "coffee": coffee,
    }


quarter = 0
dime = 0
nickle = 0
penny = 0
## Выбор кофе пользователем
user_choise = input('What would you like? (espresso/latte/cappuccino): ')
# Применение ингредиентов и и цены кофе
money = 0

should_restart = True
while should_restart:
    # Отчет о текущем кол-ве ресурсов и денег
    if user_choise == 'report' and resources['water'] == 300:
        print('Water: ', resources['water'], 'ml')
        print('Milk: ', resources['milk'], 'ml')
        print('Coffee: ', resources['coffee'], 'g')
        print(f'Money: $0')
        user_choise = input('What would you like? (espresso/latte/cappuccino): ')
    elif user_choise not in MENU:
        print('Wrong!')
        user_choise = input('What would you like? (espresso/latte/cappuccino): ')
    ## Вставка монет
    print('Please insert coins.')

    # Подсчет каждого типа монет
    quarters = int(input('How many quarters?: '))
    quarter += quarters

    dimes = int(input('How many dimes?: '))
    dime += dimes

    nickles = int(input('How many nickles?: '))
    nickle += nickles

    pennies = int(input('How many pennies?: '))
    penny += pennies

    coin_summ = (quarter * 0.25) + (dime * 0.1) + (nickle * 0.05) + (penny * 0.01)
    change = round(coin_summ - MENU[user_choise]['cost'], 2)

    money += round(coin_summ - change, 2)

    # Оповещение, если денег не хватает и новый заказ
    if coin_summ < MENU[user_choise]['cost']:
        coin_summ = 0
        print('Sorry that\'s not enough money. Money refunded.')
        should_restart = False
        break

    # Подсчет сдачи


    report = resourses(resources, MENU[user_choise])
    resources['water'] = resources['water'] - report['water']
    resources['milk'] = resources['milk'] - report['milk']
    resources['coffee'] = resources['coffee'] - report['coffee']
    # Выдача кофе, сдачи
    print(f'Here is ${change} in change.')
    print(f'Here is your {user_choise} ☕️. Enjoy!')

    # Новый заказ
    user_choise = input('What would you like? (espresso/latte/cappuccino): ')

    # Отчет о текущем кол-ве ресурсов и денег
    if user_choise == 'report':
        print('Water: ', report["water"], 'ml')
        print('Milk: ', report["milk"], 'ml')
        print('Coffee: ', report["coffee"], 'g')
        print(f'Money: ${money}')
        should_restart = False




