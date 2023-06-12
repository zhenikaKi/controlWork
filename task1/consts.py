# Цвета и стили для текста для текста
RED = "\033[1;31m"
GREEN = "\033[0;32m"
BLUE  = "\033[1;34m"
RESET = "\033[0;0m"

# Команды
CMD_EXIT = 0
CMD_ADD = 1
CMD_EDIT = 2
CMD_DELETE = 3
CMD_PRINT_MINI = 4
CMD_PRINT_FULL = 5
CMD_PRINT_SORT = 6
CMD_PRINT_SORT_DESC = 7
CMD_PRINT_NOTE = 8

# Имена полей
KEY_ID = 'id'
KEY_TITLE = 'title'
KEY_TEXT = 'text'
KEY_UPDATE = 'update'

# Формат даты
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Сортировка по дате
# не сортировать заметки
SORT_DISABLE = 0
# сортировать заметки по убыванию
SORT_DESC = 1
# сортировать по возрастанию
SORT_ASC = 2
