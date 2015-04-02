__author__ = 'fiodar'

import numpy as np
from scipy.special import l_roots


def integrate_double_mc(f, (a, b), y1, y2=lambda x: 0, args=(), n=1e4):
    x = np.random.uniform(a, b, n)
    y = map(np.random.uniform, y1(x), y2(x))
    h = np.abs(y2(x) - y1(x))

    sum = np.mean((b - a) * h * f(x, y, *args))

    return sum


def integrate_laguerre(f, args=(), n=6):
    x, c = l_roots(n)
    I = sum(np.exp(x) * f(x, *args) * c)

    return I
