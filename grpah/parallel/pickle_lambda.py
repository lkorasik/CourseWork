import dill


class PickleLambda:
    """
    Обернуть лямбду в этот класс

    Пример:
        PickleLambda(lambda x: print("Hi"))
        Process(target=a, args=(1,)).start()
    """

    def __init__(self, func):
        self.func = func

    def __getstate__(self):
        return dill.dumps(self.func)

    def __setstate__(self, state):
        self.func = dill.loads(state)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
