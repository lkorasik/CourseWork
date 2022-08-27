import time
from time import sleep

from parallel.dispatcher import Dispatcher
from parallel.task import Task


def f():
    sleep(0.5)


def g(x, y):
    sleep(0.5)
    return 2 * x + y


if __name__ == "__main__":
    dispatcher = Dispatcher(2)

    for i in range(10):
        task = Task(i, g, [i, i], {})
        dispatcher.add_task(task)

    print("Tasks created")

    dispatcher.start()

    print("Thread started")

    # dispatcher.stop()
    # dispatcher.wait()
    time.sleep(3)
    dispatcher.add_task(Task(10, g, [i, i], {}))

    time.sleep(3)
    dispatcher.tasks_finished()

    print("All work done")

    list = dispatcher.get_results()
    while not list.empty():
        print(list.get())
