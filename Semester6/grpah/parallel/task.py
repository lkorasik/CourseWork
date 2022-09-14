from parallel.result import Result


class Task:
    """Задача. Вызов функции с заданными аргументами в каком-то из исполнителей"""

    def __init__(self, uid, func, args, kwargs):
        self._uid = uid
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def perform(self):
        """Выполнить задачу"""
        result = self._func(*self._args, **self._kwargs)
        return Result(self, result)

    def get_uid(self):
        """Получить идентификатор задачи"""
        return self._uid

    def get_args(self):
        """Получить список аргументов"""
        return self._args + list(self._kwargs.values())
