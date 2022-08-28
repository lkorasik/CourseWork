class Result:
    def __init__(self, task, task_result):
        self._task = task
        self._task_result = task_result

    def get_uid(self):
        return self._task.get_uid()

    def get_args(self):
        return self._task.get_args()

    def get_result(self):
        return self._task_result

    def __str__(self):
        return f"Task:\n\tid: {self.get_uid()}\n\targs: {self.get_args()}\n\tresult: {self._task_result}"
