from multiprocessing import cpu_count, Manager

from parallel.events.stop_event import StopEvent
from parallel.events.task_finished_event import TaskFinishedEvent
from parallel.worker import Worker


class Dispatcher:
    """Диспетчер задач. Управляет исполнителями и распределяет задачи между ними"""

    def __init__(self, workers_count=cpu_count()):
        self._task_finished_event = TaskFinishedEvent()
        self._stop_event = StopEvent()

        self._manager = Manager()

        self._tasks = self._manager.Queue()
        self._results = self._manager.Queue()
        self._worker_count = workers_count
        self._workers = [self._create_worker(i) for i in range(self._worker_count)]

    def _create_worker(self, uid):
        return Worker(uid, self._tasks, self._results, self._task_finished_event, self._stop_event, self._manager)

    def add_task(self, task):
        """Добавить задачу в очередь"""
        print("Task " + str(task.get_uid()) + " added to queue")
        self._tasks.put(task)

    def start(self):
        """Запустить исполнение задач"""
        for item in self._workers:
            item.start()

    def stop(self):
        """Прервать исполнение всех задач"""
        self._stop_event.fire()

    def tasks_finished(self):
        """Событие заврешения создания задач. Работа исполнителей закончится, когда очередь задач станет пустой"""
        self._task_finished_event.fire()

    def wait(self):
        """Дождаться завершения работы всех исполнителей"""
        for worker in self._workers:
            worker.join()
        print("Dispatcher stopped")

    def get_results(self):
        """Получить результаты задач"""
        return self._results
