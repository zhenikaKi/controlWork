import datetime
import sys
import consts
from JsonRepository import Repository


class Funcs:

    __repository = Repository()

    @classmethod
    def loadData(cls):
        """ Загрузить список заметок """
        cls.__repository.loadData()

    @classmethod
    def printHelp(cls):
        """ Напечатать справку по командам """
        strHelp = f'''-----------------------------------------
{consts.CMD_ADD} - Добавить заметку
{consts.CMD_EDIT} - Редактировать заметку (по id)
{consts.CMD_DELETE} - Удалить заметку (по id)
{consts.CMD_PRINT_MINI} - Вывести все заметки (кратко)
{consts.CMD_PRINT_FULL} - Вывести все заметки (подробно)'''
        print(strHelp)
        cls.__blueText(f'{consts.CMD_EXIT} - Выход из приложения')
        print('-----------------------------------------')

    @classmethod
    def procCommand(cls, cmd):
        """
        Обработать команду.

        cmd - Введенная команда
        """
        if cmd == consts.CMD_EXIT:
            cls.__repository.saveData()
            return False
        elif cmd == consts.CMD_ADD:
            cls.__addNoteDialog()
        elif cmd == consts.CMD_EDIT:
            cls.__editNoteDialog()
        elif cmd == consts.CMD_PRINT_MINI or cmd == consts.CMD_PRINT_FULL:
            cls.__printAllNotes(cmd == consts.CMD_PRINT_MINI)
        else:
            cls.__redText(f'{cmd} - Неизвестная команда')
        return True

    @classmethod
    def __addNoteDialog(cls):
        """ Запросить данные для новой заметки """
        cls.__blueText(f'{consts.CMD_EXIT} - для выхода из режима добавления')
        title = input('Заголовок: ')
        if title == '0':
            return
        text = input('Текст: ')
        if text == '0':
            return
        cls.__addNote(title, text)

    @classmethod
    def __addNote(cls, title, text):
        """
        Добавить новую заметку.

        title - Заголовок заметки.
        text - Текст заметки
        """
        update = datetime.datetime.now()
        cls.__repository.addNote(title, text, update)
        cls.__greenText("Заметка добавлена")

    @classmethod
    def __editNoteDialog(cls):
        """ Запросить идентификатор заметки для редактирования """
        note = cls.__selectIdDialog("редактирования")
        if note[consts.KEY_ID] == 0:
            return
        cls.__editNote(note)

    @classmethod
    def __editNote(cls, note):
        """
        Редактировать заметку.

        note - Заметка для редактирования.
        """
        cls.__blueText(f'{consts.CMD_EXIT} - для выхода из режима редактирования')
        cls.__blueText('** - чтобы не менять значение')
        # печатаем текущие данные по заметке
        print('Текущая заметка')
        print(f'Заголовок: {note[consts.KEY_TITLE]}')
        print(f'Дата обновления: {note[consts.KEY_UPDATE]}')
        print(f'Текст: {note[consts.KEY_TEXT]}')
        print('')
        newNote = {
            consts.KEY_ID: note[consts.KEY_ID]
        }
        title = input('Новый заголовок: ')
        if title == '0':
            return
        newNote[consts.KEY_TITLE] = title if title != '**' else note[consts.KEY_TITLE]

        text = input('Новый текст: ')
        if text == '0':
            return
        newNote[consts.KEY_TEXT] = text if text != '**' else note[consts.KEY_TEXT]

        while True:
            try:
                date = input('Новая дата в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС ')
                if date == '0':
                    return
                if date == '**':
                    newNote[consts.KEY_UPDATE] = note[consts.KEY_UPDATE]
                    break

                # проверяем корректность даты
                datetime.datetime.strptime(date, consts.DATE_FORMAT).date()
                newNote[consts.KEY_UPDATE] = date
                break
            except ValueError:
                cls.__redText('Некорректная дата')

        cls.__repository.updateNote(newNote)
        cls.__greenText("Заметка обновлена")

    @classmethod
    def __selectIdDialog(cls, oper):
        """
        Запросить идентификатор заметки.

        oper - наименование операции, для которой нужен идентификатор.
        """
        print("Существующие заметки")
        cls.__printAllNotes(withLine=False)
        cls.__blueText(f'{consts.CMD_EXIT} - для выхода из режима {oper}')
        while True:
            try:
                id = int(input(f'Введите id заметки для {oper}: '))
                if id == 0:
                    return id

                note = cls.__repository.getNote(id)
                if note is not None:
                    return note
                else:
                    raise ValueError()
            except ValueError:
                cls.__redText('Некорректный id')

    @classmethod
    def __printAllNotes(cls, asMini=True, withLine=True):
        """
        Показать все заметки.

        asMini - True - показывать заметки в кратком виде, false - показывать в подробном виде.
        withLine - True - показывать горизонтальные линии, false - не показывать.
        """
        ID_SIZE = 5
        DATE_SIZE = 19
        # печатаем шапку
        line = f'|{"-" * (ID_SIZE + 2)}|{"-" * (DATE_SIZE + 2)}|{"-" * 5}'
        lineFull = f'|{" " * (ID_SIZE + 2)}|{" " * (DATE_SIZE + 2)}|   '
        print(f'| {"id".ljust(ID_SIZE)} | {"Дата обновления".ljust(DATE_SIZE)} | Заголовок{"" if asMini else " / Текст"}')
        if withLine:
            print(line)
        # печатаем все заметки
        for note in cls.__repository.getAll():
            text = f'| {str(note[consts.KEY_ID]).rjust(ID_SIZE)} | {note[consts.KEY_UPDATE].rjust(DATE_SIZE)} | {note[consts.KEY_TITLE] }'
            print(text)
            if not asMini:
                print(f'{lineFull}{note[consts.KEY_TEXT]}')
            if withLine:
                print(line)

    @classmethod
    def __redText(cls, text):
        """
        Напечатать текст красным цветом.

        text - Текст.
        """
        cls.__printColorText(consts.RED, text)

    @classmethod
    def __greenText(cls, text):
        """
        Напечатать текст зеленым цветом.

        text - Текст.
        """
        cls.__printColorText(consts.GREEN, text)

    @classmethod
    def __blueText(cls, text):
        """
        Напечатать текст голубым цветом.

        text - Текст.
        """
        cls.__printColorText(consts.BLUE, text)

    @classmethod
    def __printColorText(cls, color, text):
        """
        Напечатать цветной текст.

        color - Цвет текст.
        text - Текст.
        """
        sys.stdout.write(color)
        print(text)
        sys.stdout.write(consts.RESET)
