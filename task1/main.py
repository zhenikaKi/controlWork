import datetime
from Funcs import Funcs

funcs = Funcs()


def runner():
    # Постоянный цикл для работы справочника
    while True:
        try:
            funcs.printHelp()
            inputComand = int(input('Введите номер команды: '))

            if not funcs.procCommand(inputComand):
                break
        except ValueError:
            print("Неизвестная команда")


# Загружаем в память список заметок
Funcs.loadData()

# Запускаем консольное приложение "Заметки"
runner()
