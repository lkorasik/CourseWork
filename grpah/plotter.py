from matplotlib import pyplot as plt


class Plotter:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self._legend = dict()

    def setup(self, x_label, y_label, y_scale, grid, title):
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.yscale(y_scale)
        self.ax.grid(which=grid)
        plt.title(title)
        self.fig.canvas.manager.set_window_title(title)
        return self

    def plot(self, draw_x, draw_y, marker, color, name=""):
        line = plt.plot(draw_x, draw_y, marker=marker, color=color)
        self._legend[line[0]] = name
        return self

    def scatter(self, draw_x, draw_y, marker, color, name=""):
        scatter = plt.scatter(draw_x, draw_y, marker=marker, rasterized=True, linewidths=0.01, color=color)
        self._legend[scatter] = name
        return self

    def show(self):
        plt.show(block=False)
        return self

    def show_last(self):
        plt.show(block=True)

    def legend(self):
        lines = []
        names = []
        for k in self._legend:
            lines.append(k)
            names.append(self._legend[k])
        self.ax.legend(lines, names)
        return self
