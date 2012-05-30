import numpy as np
from numpy import pi, sin, cos, tan

import artist


def main():
    np.random.seed(1)

    graph = artist.MultiPlot(2, 3, width=r'.5\linewidth')
    x = np.linspace(-pi, pi)
    graph.plot(0, 1, x, sin(x), mark=None)
    graph.add_pin(0, 1, '$\sin(x)$', relative_position=.5)
    graph.plot(1, 0, x, cos(x), mark=None)
    graph.add_pin_at_xy(1, 0, 1, .5, '$\cos(x)$')
    graph.plot(1, 2, x, tan(x), mark=None)

    x = np.random.normal(size=1000)
    n, bins = np.histogram(x, bins=20)
    graph.histogram(0, 0, n, bins)

    x = range(5)
    lower = np.random.uniform(-2, -1, size=5)
    median = np.random.uniform(-.5, .5, size=5)
    upper = np.random.uniform(1, 2, size=5)
    graph.plot(0, 2, x, median, mark='*')
    graph.shade_region(0, 2, x, lower, upper)

    graph.plot(1, 1, range(5), np.random.normal(size=5))

    graph.save('preview.tex')
    graph.save_as_pdf('preview.pdf')


if __name__ == '__main__':
    main()
