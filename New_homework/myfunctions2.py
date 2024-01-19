# МОДУЛЬ 1
#первый пример
def simple_separator(sign):
    return sign * 10

print(simple_separator("*") == "**********")

#второй пример
def long_separator(count):
    return'*' * count

print(long_separator(3) == "***")
print(long_separator(4) == "****")

#третий пример
def separator(symbol, count):
    return f'{symbol * count}'

print(separator("|", 10) == "||||||||||")
print(separator("#", 10) == "##########")

#четвертый пример
def hello_world():
    print('*' * 12)
    print('Hello World!')
    print('#' * 12)

hello_world()

#пятый пример
def hello_who(who='World'):
    print('*' * 17)
    print(f'Hello  {who}!')
    print('#' * 17)

hello_who('Александра')
hello_who()
hello_who('Max')

#шестой пример
def pow_many(power, *num):
    return sum(num) ** power

print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


#седьмой пример
def print_key_val(**kwargs):
    for key,val in kwargs.items():
        print (f'{key} ==>{val}')

print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)

#восьмой пример
def my_filter(iterable, function):
    elements = []
    for el in iterable:
        if function (el):
           elements.append(el)
    return elements

print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True

