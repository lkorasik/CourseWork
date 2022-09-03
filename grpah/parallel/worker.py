from multiprocessing import Queue, Process
from queue import Empty

from parallel.commands import Commands


class Worker(Process):
    def __init__(self, uid, tasks, results):
        print("Worker " + str(uid) + " created")
        self._id = uid
        self._tasks = tasks
        self._commands = Queue()
        self._results = results
        super(Worker, self).__init__()

    def get_commands(self):
        return self._commands

    def run(self):
        should_stop = False
        while True:
            if self._commands.qsize() != 0:
                command = self._commands.get()
                if command == Commands.STOP:
                    break
                if command == Commands.TASK_FINISHED:
                    print("Worker " + str(self._id) + " got stop command")
                    should_stop = True

            try:
                task = self._tasks.get_nowait()
                result = task.perform()
                self._results.put(result)
                print("Task " + str(task.get_uid()) + " done by worker " + str(self._id))
            except Empty:
                if should_stop:
                    print("Worker " + str(self._id) + " stop running")
                    break
