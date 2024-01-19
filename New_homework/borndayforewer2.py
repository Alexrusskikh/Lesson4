'''в моей  версии Paython словарь упорядочен, - проводил  испытания, и  в словарь можно  добавть еще вопросы...'''
literature_dict = {'год рождения А.С.Пушкина': '1799', 'дату рождения А.С Пушкина': '6 июня'}
mathematics_dict = {'2x2': '4', '5x5': '25'}
#функция перебирает пары и  задает  вопросы  и проверяет  ответы
print("Внимаение - тестирование началось!")
def long_separator(count):
    return'*' * count

def  test (subject):
    for key in subject: #итератор по ключам словаря
        answer = input("Укажите ответ - " + key + " \n")
        if answer == subject[key]:
            print("Верно!!!")
        else:
            print("Не верно...")

print(long_separator(30))
test(literature_dict)
print(long_separator(30))
test(mathematics_dict)
print(long_separator(30))
print("Тест  закончен")


# изменил  предложенный модуль
def year_birth(yyyy):
    while yyyy != '1799':
        print("Не верно")
        yyyy = input('Ввведите год рождения А.С.Пушкина:')

def day_birth(dd):
    while dd != '6':
        print("Не верно")
        dd = input('В какой день июня родился Пушкин?')

def test(func_year,func_day):
    year = input('Ввведите год рождения А.С.Пушкина:')
    func_year(year)
    day = input('Ввведите день рождения Пушкин?')
    func_day(day)
    print('Верно')

test(year_birth, day_birth)
