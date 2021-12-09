from matplotlib import pyplot as plt


class Plotter:
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def setup(self, xlabel, ylabel, yscale, grid, title):
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.yscale(yscale)
        self.ax.grid(which=grid)
        plt.title(title)
        self.fig.canvas.manager.set_window_title(title)

    def plot(self, draw_x, draw_y, marker, color):
        plt.plot(draw_x, draw_y, marker=marker, color=color)

    def scatter(self, draw_x, draw_y, marker, color):
        plt.scatter(draw_x, draw_y, marker=marker, rasterized=True, linewidths=0.01, color=color)

    def show(self, has_next_graphic):
        plt.show(block=not has_next_graphic)
