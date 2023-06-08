import json
import consts
from RepositoryBase import RepositoryBase


class Repository(RepositoryBase):
    __fileName = "data/notes.json"
    __notes = []

    @classmethod
    def loadData(cls):
        with open(cls.__fileName, 'r', encoding='utf-8') as f:
            cls.__notes = json.load(f)

    @classmethod
    def saveData(cls):
        with open(Repository.__fileName, 'w', encoding="utf-8") as f:
            f.write(json.dumps(cls.__notes, ensure_ascii=False))

    @classmethod
    def getAll(cls):
        return cls.__notes

    @classmethod
    def getNote(cls, id):
        """Получить заметку по идентификатору.

        id -- Идентификатор заметки.
        """
        for note in cls.__notes:
            if note[consts.KEY_ID] == id:
                return note

        return None

    @classmethod
    def addNote(cls, title, text, update):
        # формируем объект заметки
        note = {
            consts.KEY_ID: cls.__getNewID(),
            consts.KEY_TITLE: title,
            consts.KEY_TEXT: text,
            consts.KEY_UPDATE: update.strftime(consts.DATE_FORMAT)
        }
        cls.__notes.append(note)

    @classmethod
    def updateNote(cls, note):
        position = -1
        for ind in range(len(cls.__notes)):
            curNote = cls.__notes[ind]
            if curNote[consts.KEY_ID] == note[consts.KEY_ID]:
                position = ind
                break
        if position >= 0:
            cls.__notes[position] = note

    @classmethod
    def __getNewID(cls):
        """ Получить идентификатор заметки """
        result = 0
        for note in cls.__notes:
            result = max(result, note[consts.KEY_ID])
        return result + 1
