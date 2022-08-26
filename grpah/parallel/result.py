class Result:
    def __init__(self, task_uid, task_args, task_result):
        self._task_uid = task_uid
        self._task_result = task_result
        self._args = task_args

    def get_uid(self):
        return self._task_uid

    def get_result(self):
        return self._task_result

    def __str__(self):
        return f"Task:\n\tid: {self._task_uid}\n\targs: {self._args}\n\tresult: {self._task_result}"
