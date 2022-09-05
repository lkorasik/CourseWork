class Line:
    """Набор точек, который можно нарисовать в виде набора точек или в виде ломаной линии"""

    def __init__(self, x=None, y=None):
        if y is None:
            y = []
        if x is None:
            x = []

        self.x = x
        self.y = y

    def add(self, x, y):
        """
        Добавить точку в линию

        Вход:
            x - координата по оси абсцисс
            y - координаат по оси ординат
        """
        self.x.append(x)
        self.y.append(y)
        return self

    def add_x(self, x):
        """Добавить координату по оси абсцисс"""
        self.x.append(x)
        return self

    def add_y(self, y):
        """Добавить координату по оси ординат"""
        self.y.append(y)
        return self
