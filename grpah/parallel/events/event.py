class Event:
    """Событие"""

    def __init__(self):
        self._handlers = []

    def add_handler(self, handler):
        """Добавить обарботчик события"""
        self._handlers.append(handler)

    def fire(self):
        """Активировать событие и вызвать все обработчики этого события"""
        for handler in self._handlers:
            handler(self)
