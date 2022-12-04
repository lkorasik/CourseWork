import matplotlib.pyplot as plt
import pylab
import numpy as np


def f(S, Gmax, Km):
    s1 = Gmax*S   # G_max
    e1 = S + Km  # K_m
    return np.divide(s1, e1)


def update(val):
    l.set_ydata(f(S, sGmax.val, sKm.val))


if __name__ == "__main__":
    S = np.arange(0, 100, 0.1)

    ax = plt.subplot(111)
    plt.subplots_adjust(left=0.15, bottom=0.25)
    l, = plt.plot(f(S, 1.0, 1.0))
    plt.grid(False)
    plt.title('Playing with sliders')
    plt.xlabel('time')
    plt.ylabel('concentration')

    axcolor = 'lightgoldenrodyellow'
    axGmax = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor=axcolor)
    axKm = plt.axes([0.15, 0.15, 0.65, 0.03], facecolor=axcolor)

    sGmax = pylab.Slider(axGmax, 'Gmax', 0.1, 3.0, valinit=1)
    sKm = pylab.Slider(axKm, 'Km', 0.01, 1.0, valinit=1)

    sGmax.on_changed(update)
    sKm.on_changed(update)

    plt.show()
