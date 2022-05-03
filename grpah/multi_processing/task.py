from multiprocessing import Queue


class Task:
    def __init__(self, id: int, output: Queue, function, args: list):
        self.id = id
        self._function = function
        self._args = args
        self._output = output

    def run(self):
        result = self._function(*self._args)
        self._output.put(result)
