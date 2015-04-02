__author__ = 'fiodar'

import numpy as np
from scipy.special import l_roots
from scipy.misc import factorial, derivative


def integrate_double_mc(f, (a, b), y1, y2=lambda x: 0, args=(), n=1e4):

    x = np.random.uniform(a, b, n)
    y = map(np.random.uniform, y1(x), y2(x)) #[np.random.uniform(y1(i), y2(i)) for i in x]
    h = np.abs(y2(x) - y1(x))

    I = np.mean((b - a) * h * f(x, y, *args))

    return I


def integrate_laguerre(f, args=(), n=6):

    x, c = l_roots(n)
    I = sum(np.exp(x) * f(x, *args) * c)

    # R = factorial(n)**2/factorial(2*n) * abs(derivative(f, 0, dx=0.01, order=2*n+1, n=2*n))

    # print 'Laguerre quadrature: R <=', R
    return I
