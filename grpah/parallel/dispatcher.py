from multiprocessing import Queue, cpu_count

from parallel.commands import Commands
from parallel.worker import Worker


# todo: проблема в том, что 4 команды в общей очереди не всегда могут дойти до всех потоков, в итоге кто-то прочитал не
#  свои сообщения и остановился

class Dispatcher:
    def __init__(self, workers_count=cpu_count()):
        self._tasks = Queue()
        self._results = Queue()
        self._worker_count = workers_count
        self._workers = [self._create_worker(i) for i in range(self._worker_count)]

    def _create_worker(self, uid):
        return Worker(uid, self._tasks, self._results)
        # return Process(target=Worker.start_work, args=(uid, self._tasks, self._commands, self._results))

    def add_task(self, task):
        self._tasks.put(task)

    def start(self):
        for item in self._workers:
            item.start()

    def done(self):
        self._tasks.close()

    def stop(self):
        for worker in self._workers:
            worker.get_commands().put(Commands.STOP)

    def tasks_finished(self):
        for worker in self._workers:
            worker.get_commands().put(Commands.TASK_FINISHED)

    def wait(self):
        for worker in self._workers:
            worker.join()

    def get_results(self):
        return self._results
