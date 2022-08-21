import datetime
#создаем список, элементами которого будет кортеж
traffic_money = []

#разделитель для  удобства восприятия
def simple_separator():
    return '************************'

#функция пополнения  счета
def put_cash(traffic_money): #функция пополнения  счета
    amount = int(input('Введите сумму для пополнения: '))
    traffic_money.append(('Поступление средств '+data, int(amount)))#добавляет в traffic_money кортеж из 2 элементов

# функция покупки и ее суммы
def buy(traffic_money):
    product_name = input('Введите название продукта: ')
    amount = input('Введите сумму покупки: ')
    traffic_money.append(('Покупка '+data+' '+ product_name, -int(amount)))# добавляет в traffic_money покупки и ее суммы

def history(traffic_money):#функция истории транзакций
    print("Баланс счета: ", sum([trans[1] for trans in traffic_money]))
    print('История транзакций:')
    for name, amount in traffic_money:
        print(f'      {name}: {amount} УЕ')#перебор кортежей и вывод их элементов через ":"

    input('\nНажмите Enter чтобы продолжить ')

data =(datetime.date.today().strftime("%d/%m/%Y"))
print(data)
while True:
    print(simple_separator())
    print("Баланс счета: ", sum([trans[1] for trans in traffic_money]))
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(simple_separator())

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        put_cash(traffic_money)
    elif choice == '2':
        buy(traffic_money)
    elif choice == '3':
        history(traffic_money)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
