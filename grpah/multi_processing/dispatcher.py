from multiprocessing import Queue

from multi_processing.executor import Executor


class Dispatcher:
    def     __init__(self, size: int, tasks: Queue, is_log_enabled):
        self._executors = [Executor(tasks, i, is_log_enabled) for i in range(size)]

    def run(self):
        for executor in self._executors:
            executor.start()

    def wait(self):
        for executor in self._executors:
            executor.join()
