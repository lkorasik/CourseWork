import queue
from multiprocessing import Queue, Process


class Executor:
    def __init__(self, tasks: Queue, id: int, is_log_enabled: bool):
        self._process = Process(target=self.run, args=(tasks,))
        self._id = id
        self._is_log_enabled = is_log_enabled

    def start(self):
        if self._is_log_enabled:
            print("Start executor ", self._id)
        self._process.start()

    def join(self):
        self._process.join()

    def run(self, tasks: Queue):
        while True:
            try:
                task = tasks.get(block=False)
                task.run()
            except queue.Empty:
                if self._is_log_enabled:
                    print("Stop ", self._id)
                break

        if self._is_log_enabled:
            print("Finish ", self._id)
