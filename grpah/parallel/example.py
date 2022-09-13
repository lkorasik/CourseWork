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
    dispatcher.start()
    print("Dispatcher started")

    for i in range(10):
        task = Task(i, g, [i], {"y": i})
        dispatcher.add_task(task)

    print("Tasks created")
    # dispatcher.stop()

    # dispatcher.stop()
    # dispatcher.wait()
    time.sleep(3)
    dispatcher.add_task(Task(10, g, [i, i], {}))

    time.sleep(3)
    dispatcher.tasks_finished()
    # dispatcher.wait()

    print("All work done")

    results = dispatcher.get_results()
    while not results.empty():
        print(results.get())
