from multiprocessing import Queue, Process
from time import sleep


def worker(id_, tasks: Queue):
    while tasks.qsize() != 0:
        task = tasks.get()
        task()
        print("Task done " + str(id_))


def f():
    sleep(0.5)


if __name__ == "__main__":
    tasks = Queue()

    for i in range(10):
        tasks.put(f)

    print("Tasks created")

    worker0 = Process(target=worker, args=(0, tasks))
    worker1 = Process(target=worker, args=(1, tasks))

    worker0.start()
    worker1.start()

    print("Thread started")

    worker0.join()
    worker1.join()
