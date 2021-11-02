from matplotlib import pyplot as plt


def plot(xb, b_range, title, xlabel, ylabel, has_next_graphic):
    draw_x = []
    draw_y = []

    for b in b_range:
        x = xb[b]
        for x_ in x:
            if x_ > 10:
                continue
            draw_x.append(b)
            draw_y.append(x_)

    fig, ax = plt.subplots()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.yscale('log')
    plt.scatter(draw_x, draw_y, marker='.', rasterized=True, linewidths=0.01)

    ax.grid(which='major')
    plt.title(title)
    fig.canvas.manager.set_window_title(title)

    plt.show(block=not has_next_graphic)
