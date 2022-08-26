from multiprocessing import Queue, Process
from time import sleep


class Task:
    def __init__(self, uid, func):
        self._uid = uid
        self._func = func

    def perform(self):
        self._func()


def worker(id_, tasks: Queue):
    while tasks.qsize() != 0:
        task = tasks.get()
        task.perform()
        print("Task " + str(task._uid) + " done by worker " + str(id_))


def f():
    sleep(0.5)


if __name__ == "__main__":
    tasks = Queue()

    for i in range(10):
        task = Task(i, f)
        tasks.put(task)

    print("Tasks created")

    worker0 = Process(target=worker, args=(0, tasks))
    worker1 = Process(target=worker, args=(1, tasks))

    worker0.start()
    worker1.start()

    print("Thread started")

    worker0.join()
    worker1.join()

    print("All work done")
