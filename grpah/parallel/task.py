from parallel.result import Result


class Task:
    def __init__(self, uid, func, args, kwargs):
        self._uid = uid
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def perform(self):
        result = self._func(*self._args, **self._kwargs)
        return Result(self._uid, self._args, result)

    def get_uid(self):
        return self._uid
