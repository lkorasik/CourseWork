from matplotlib import pyplot as plt


class Plotter:
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def setup(self, x_label, y_label, y_scale, grid, title):
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.yscale(y_scale)
        self.ax.grid(which=grid)
        plt.title(title)
        self.fig.canvas.manager.set_window_title(title)
        return self

    def plot(self, draw_x, draw_y, marker, color):
        plt.plot(draw_x, draw_y, marker=marker, color=color)
        return self

    def scatter(self, draw_x, draw_y, marker, color):
        plt.scatter(draw_x, draw_y, marker=marker, rasterized=True, linewidths=0.01, color=color)
        return self

    def show(self, has_next_graphic):
        plt.show(block=not has_next_graphic)

        return self
