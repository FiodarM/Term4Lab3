__author__ = 'fiodar'

from integration import *
import matplotlib.pyplot as plt


f = lambda x, y: np.cos(x*y)
a, b = 0., 2.
X = np.linspace(a, b)
y1, y2 = lambda x: x - 2, lambda x: 4 - x**2
g = lambda x: x/(x**4 + 1)
integral_f = integrate_double_mc(f, (a, b), y1, y2, n=50e3)
integral_g = integrate_laguerre(g, n=5)


fig = plt.figure('Lab 3', tight_layout=True)
ax = fig.gca()
ax.set_title('Integration region', fontsize=16)
boundary = ax.plot(X, y1(X), 'r', X, y2(X), 'b')
region = ax.fill_between(X, y1(X), y2(X), color=(0., 0.5, 0., 0.5), label='$\Omega$')
lgnd = ax.legend(('$x-2$', '$4-x^2$'), loc='best')
Omega = ax.text(0.3, 0.5, r"$\Omega$", fontsize=200, color='w', alpha='0.5')
Res_f = ax.text(1.4, 2.6, r"$\iint_\Omega f(x,y)dxdy=%.2f$" % integral_f, fontsize=16)
Res_g = ax.text(1.5, 2.0, r"$\int_{0}^{\infty} g(x)dx=%.2f$" % integral_g, fontsize=16)
plt.show(fig)
