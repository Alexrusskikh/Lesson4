'''в моей  версии Paython словарь упорядочен, - проводил  испытания, и  в словарь можно  добавть еще вопросы...'''
literature_dict = {'год рождения А.С.Пушкина': '1799', 'дату рождения А.С Пушкина': '6 июня'}
mathematics_dict = {'2x2': '4', '5x5': '25'}
#функция принимает словари вопросов по предметам, перебирает пары и  задает  вопросы
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
