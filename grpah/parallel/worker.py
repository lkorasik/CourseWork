from multiprocessing import Process, Manager
from queue import Empty


class Worker(Process):
    """Исполнитель"""

    def __init__(self, uid, tasks, results, task_finished_event, stop_event):
        print("Worker " + str(uid) + " created")
        self._id = uid
        self._tasks = tasks
        self._results = results

        self._should_stop = Manager().Value('bool', False)

        task_finished_event.add_handler(self.handle_task_finished_event)
        stop_event.add_handler(self.handle_stop_event)

        super(Worker, self).__init__()

    def handle_stop_event(self, event):
        """Обработчик события прерывания работы"""
        self.kill()

    def handle_task_finished_event(self, event):
        """Обработчик события завершения добавления задач"""
        self._should_stop.value = True

    def run(self):
        """Запустить исполнителя"""
        while True:
            try:
                task = self._tasks.get_nowait()
                result = task.perform()
                self._results.put(result)
                print("Task " + str(task.get_uid()) + " done by worker " + str(self._id))
            except Empty:
                if self._should_stop.value:
                    print("Worker " + str(self._id) + " stop running")
                    break
