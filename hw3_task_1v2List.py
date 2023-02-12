''' Пользователь вводит месяц в виде целого числа от 1 до 12.Сообщить, к какому времени года относится
месяц (зима, весна, лето, осень).Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень '''

my_list = [['Зима', 12, 1, 2],
    ['Весна', 3, 4, 5],
    ['Лето', 6, 7, 8],
    ['Осень', 9, 10, 11]]

month = int(input('Введите номер месяца: '))
if month in range(1, 13):
    for i, el in enumerate(my_list):
        if month in el[1:4]:
            print(el[0])
            break
else:
    print('Месяца с таким номером не существует! Попробуйте ещё!')