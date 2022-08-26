from multiprocessing import Queue, Process
from queue import Empty

from parallel.commands import Commands


def executor(id_, tasks: Queue, commands: Queue, results: Queue):
    finish = False
    while True:
        if commands.qsize() != 0:
            command = commands.get()
            if command == Commands.STOP:
                break
            if command == Commands.TASK_FINISHED:
                finish = True

        try:
            task = tasks.get_nowait()
            result = task.perform()
            results.put(result)
            print("Task " + str(task._uid) + " done by worker " + str(id_))
        except Empty:
            if finish:
                break


class Dispatcher:
    def __init__(self):
        self._tasks = Queue()
        self._commands = Queue()
        self._results = Queue()
        self._worker_count = 2
        self._workers = [Process(target=executor, args=(i, self._tasks, self._commands, self._results)) for i in
                         range(self._worker_count)]

    def add_task(self, task):
        self._tasks.put(task)

    def start(self):
        for item in self._workers:
            item.start()

    def done(self):
        self._tasks.close()

    def stop(self):
        for _ in range(len(self._workers)):
            self._commands.put(Commands.STOP)

    def tasks_finished(self):
        for _ in range(len(self._workers)):
            self._commands.put(Commands.TASK_FINISHED)

    def wait(self):
        for worker in self._workers:
            worker.join()

    def get_results(self):
        return self._results
