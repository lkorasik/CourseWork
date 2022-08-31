from multiprocessing import Process

import dill


class DillPickle:
    def __init__(self, e):
        self.e = e

    def __getstate__(self):
        return dill.dumps(self.e)

    def __setstate__(self, state):
        self.e = dill.loads(state)


class DillPickleCallable(DillPickle):
    def __call__(self, *args, **kwargs):
        return self.e(*args, **kwargs)


def wrap(func):
    return DillPickle(func)


if __name__ == "__main__":
    a = DillPickleCallable(lambda x: print("Hi"))
    Process(target=a, args=(1,)).start()
