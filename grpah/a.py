import time
from multiprocessing import Manager

from multi_processing.Dispatcher import Dispatcher
from multi_processing.task import Task


def f(x):
    return x ** 2


if __name__ == "__main__":
    manager = Manager()

    output = manager.Queue()
    tasks = manager.Queue()
    for i in range(100000):
        task = Task(i, output, f, [i])
        tasks.put(task)

    dispatcher = Dispatcher(6, tasks)
    start = time.time()
    dispatcher.run()
    dispatcher.wait()
    end = time.time()
    print(end - start)
