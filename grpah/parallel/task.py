from parallel.result import Result


class Task:
    def __init__(self, uid, func, args, kwargs):
        self._uid = uid
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def perform(self):
        result = self._func(*self._args, **self._kwargs)
        return Result(self, result)

    def get_uid(self):
        return self._uid

    def get_args(self):
        return self._args + list(self._kwargs.values())
