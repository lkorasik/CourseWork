import queue
from multiprocessing import Queue, Process


class Executor:
    def __init__(self, tasks: Queue, id: int):
        self._process = Process(target=self.run, args=(tasks,))
        self._id = id

    def start(self):
        print("Start ", self._id)
        self._process.start()

    def join(self):
        self._process.join()

    def run(self, tasks: Queue):
        while True:
            try:
                task = tasks.get(block=False)
                task.run()
            except queue.Empty:
                print("stop ", self._id)
                break
        print("Finish ", self._id)
