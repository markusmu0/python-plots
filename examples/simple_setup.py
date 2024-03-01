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

x = np.linspace(0, 20, 300)
y1 = np.sin(x)
y2 = np.cos(x)

setup()
#setup(debug=True)
"""
a call to setup() without parameters sets the font to
the latex font with serifs and sets font sizes

debug=True allows to use the GUI of Python (plt.show()),
but it does not show the correct fonts
"""

fig = plt.figure()
plt.plot(x, y1, label="sin")
plt.plot(x, y2, label="cos")
plt.legend()
plt.xlabel("x values")
plt.ylabel("y values")
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
fig = plt.figure()
ax = fig.gca()
contourplot(fig, ax, x, y, z)
ax.set_xlabel("x")
ax.set_ylabel("y")

show(fig)
#plt.show()