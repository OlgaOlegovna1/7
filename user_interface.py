import model as cr
import logger as lg


print('\nВас приветствует телефонная книга')


def ls_menu():
    while True:
        print('\nМЕНЮ')
        print('1. Показать все записи.')
        print('2. Найти номер по фамилии.')
        print('3. Найти номер по имени.')
        print('4. Поиск по номеру телефона.')
        print('5. Добавить новую запись.')
  
        n = сhecking_the_number(input('Выберите пункт меню: '))

        if n == 1:
            lg.logging.info('The user has selected item number 1')
            print(cr.retrive())

        elif n == 2:
            lg.logging.info('The user has selected item number 2')
            search = input('Введите фамилию: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(surname=search))

        elif n == 3:
            lg.logging.info('The user has selected item number 3')
            search = input('Введите имя: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(name=search))

        elif n == 4:
            lg.logging.info('The user has selected item number 4')
            search = input('Введите номер  телефона: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(number=search))

        elif n == 5:
            lg.logging.info('The user has selected item number 5')
            name = input('Введите имя: ')
            lg.logging.info('User entered: {name}')
            surname = input('Введите фамилию: ')
            lg.logging.info('User entered: {surname}')
            number = input('Введите номер телефона: ')
            lg.logging.info('User entered: {number}')
            cr.create(name, surname, number)


def сhecking_the_number(arg):
    while arg.isdigit() != True:
        lg.logging.info('User entered an invalid menu value: {arg}')
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)
