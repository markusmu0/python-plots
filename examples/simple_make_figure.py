#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))      # add path to figure.py
"""
you need to specify the relative path to figure.py
this can be done through an absolute path in sys.path.append(...)
or a relative path (in this case '..') as you can see above
"""

from figure import setup, make_figure, show   # import functions
from contourplots import contourplot   # import functions

x = np.linspace(0, 2000, 300)
y1 = np.sin(x/100)
y2 = np.cos(x/100)

fig, ax = make_figure()
#fig, ax = make_figure(debug=True)
"""
make_figure without parameters calls setup() (see simple_setup.py) and
creates a figure which it returns. In addition, it generates axes that leave
room for the axis labels even with small figure sizes and returns the axes.
It also modifies the ticks.

debug=True allows to use the GUI of Python (plt.show()),
but it does not show the correct fonts
"""

ax.plot(x, 1e5*y1, label="sin")
ax.plot(x, 0.5e5*y2, label="cos")
ax.legend()
ax.set_xlabel("x values")
ax.set_ylabel("y values")
"""
Attention: some commands are called differently for the axes:
plt.xlabel -> ax.set_xlabel
"""
show(fig)
#plt.show()
"""
The only disadvantage of using the setup function is that by using pgf,
the python internal GUI for plots (plt.show()) is no longer supported.
If you still want to view the file directly you can use the show() function.
This generates a temporary pdf file and opens it.

Alternatively, debug=True can be selected for setup.
In this case, the correct fonts are not displayed.
"""

"""
In the following a contourplot example is given
"""
x = np.linspace(0, 20, 300)
y = np.empty(100)
z = np.empty([len(x), len(y)])
for i in range(len(y)):
    y[i] = i**2
    for j in range(len(x)):
        z[j, i] = x[j] * y[i]
fig, ax = make_figure(default_axes=True)
#fig, ax = make_figure(default_axes=True, debug=True)
contourplot(fig, ax, x, y, z, z_label="z")
ax.set_xlabel("x")
ax.set_ylabel("y")

show(fig)
#plt.show()