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
quarter = 0
dime = 0
nickle = 0
penny = 0
## Выбор кофе пользователем
user_choise = input('What would you like? (espresso/latte/cappuccino): ')
# Применение ингредиентов и и цены кофе


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

# Оповещение, если денег не хватает и новый заказ
if coin_summ < MENU[user_choise]['cost']:
    coin_summ = 0
    print('Sorry that\'s not enough money. Money refunded.')

# Подсчет сдачи


# Вычитание ингредиентов кофе из общего ресурса
def resourses(resources, menu):
    water = resources['water'] - menu[user_choise][1]['water']
    milk = resources['milk'] - menu[user_choise][1]['milk']
    coffee = resources['coffee'] - menu[user_choise][1]['coffee']
    return {
        "water": water,
        "milk": milk,
        "coffee": coffee,
    }
resourses(resources, MENU[user_choise])
# Выдача кофе, сдачи

# Новый заказ

# Отчет о текущем кол-ве ресурсов и денег
