from multiprocessing import Queue
from queue import Empty

from parallel.commands import Commands


class Worker:
    @staticmethod
    def start_work(executor_id, tasks: Queue, commands: Queue, results: Queue):
        should_stop = False
        while True:
            if commands.qsize() != 0:
                command = commands.get()
                if command == Commands.STOP:
                    break
                if command == Commands.TASK_FINISHED:
                    print("Worker " + str(executor_id) + " got stop command")
                    should_stop = True

            try:
                task = tasks.get_nowait()
                result = task.perform()
                results.put(result)
                print("Task " + str(task.get_uid()) + " done by worker " + str(executor_id))
            except Empty:
                if should_stop:
                    print("Worker " + str(executor_id) + " stop running")
                    break
