class Line:
    def __init__(self, x=None, y=None):
        if y is None:
            y = []
        if x is None:
            x = []

        self.x = x
        self.y = y

    def add_x(self, x):
        self.x.append(x)

    def add_y(self, y):
        self.y.append(y)
