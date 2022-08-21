
def  test ( year='1799', day='6 июня'):
    BornYearPushkin = input("Укажите год рождения А.С Пушкина: ")
    while BornYearPushkin != "1799":
        BornYearPushkin = input("Уточните год в справочнике и введите вновь...")
    print("Верно!!!!")

    BornDaуPushkin = input("Укажите дату рождения А.С Пушкина, например - '6 июня': ")
    while BornDaуPushkin != '6 июня':
        BornDaуPushkin = input("Уточните год в справочнике и введите вновь...")
    print("Верно!!!!")

    print("Тест  закончен")


test()