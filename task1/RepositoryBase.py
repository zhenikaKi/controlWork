class RepositoryBase:
    """ Базовый класс по работе с хранилищем заметок """

    @classmethod
    def loadData(cls):
        """ Загрузка всех заметок """
        pass

    @classmethod
    def saveData(cls):
        """ Сохранение всех заметок """
        pass

    @classmethod
    def getAll(cls):
        """ Получить все заметки """
        pass

    @classmethod
    def getNote(cls, id):
        """Получить заметку по идентификатору.

        id -- Идентификатор заметки.
        """
        pass

    @classmethod
    def addNote(cls, title, text, update):
        """
        Добавить новую заметку.

        title - Заголовок заметки.
        text - Текст заметки.
        update - Дата обновления заметки.
        """
        pass

    @classmethod
    def updateNote(cls, note):
        """
        Обновить заметку.

        note - Обновленная заметка.
        """
        pass
        pass

    @classmethod
    def deleteNote(cls, note):
        """
        Удалить заметку.

        note - Заметка для удаления.
        """
        pass
