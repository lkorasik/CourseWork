import time
from multiprocessing import Queue, Process
from queue import Empty
from time import sleep


class Task:
    def __init__(self, uid, func, args, kwargs):
        self._uid = uid
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def perform(self):
        self._func(*self._args, **self._kwargs)


class Dispatcher:
    def __init__(self):
        self._tasks = Queue()
        self._commands = Queue()
        self._worker_count = 2
        self._workers = [Process(target=executor2, args=(i, self._tasks, self._commands)) for i in range(self._worker_count)]

    def add_task(self, task):
        self._tasks.put(task)

    def start(self):
        for worker in self._workers:
            worker.start()

    def done(self):
        self._tasks.close()

    def stop(self):
        for _ in range(len(self._workers)):
            self._commands.put("stop")

    def tasks_finished(self):
        for _ in range(len(self._workers)):
            self._commands.put("tasks_finished")

    def wait(self):
        for worker in self._workers:
            worker.join()


def executor2(id_, tasks: Queue, commands: Queue):
    finish = False
    while True:
        command = None
        if commands.qsize() != 0:
            command = commands.get()
            if command == "stop":
                break
            if command == "tasks_finished":
                finish = True

        try:
            task = tasks.get_nowait()
            task.perform()
            print("Task " + str(task._uid) + " done by worker " + str(id_))
        except Empty:
            if finish:
                break


def f():
    sleep(0.5)


if __name__ == "__main__":
    dispatcher = Dispatcher()

    for i in range(10):
        task = Task(i, f, [], {})
        dispatcher.add_task(task)

    print("Tasks created")

    dispatcher.start()

    print("Thread started")

    # dispatcher.stop()
    # dispatcher.wait()
    time.sleep(3)
    dispatcher.add_task(Task(10, f, [], {}))

    time.sleep(3)
    dispatcher.tasks_finished()

    print("All work done")
