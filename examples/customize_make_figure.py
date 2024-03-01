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


def my_make_figure():
    """
    Define your own function that sets the appropriate parameters for you.
    That way you don't have to write them for every figure.
    """
    return make_figure(width=8.5, height=5.85, unit="cm")
    # return make_figure(width=8.5, height=5.85, unit="cm", debug=True)


x = np.linspace(0, 20, 300)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = my_make_figure()
ax.plot(x, 1e4*y1, label="sin")
ax.plot(x, 1e4*y2, label="cos")
ax.legend()
ax.set_xlabel("x values")
ax.set_ylabel("y values")
fig.savefig(os.path.join(os.path.dirname(__file__), "example2.pdf"), format="pdf")
"""
Attention: some commands are called differently for the axes:
plt.xlabel -> ax.set_xlabel
"""
# show(fig)
# plt.show()
"""
The only disadvantage of using the setup function is that by using pgf,
the python internal GUI for plots (plt.show()) is no longer supported.
If you still want to view the file directly you can use the show() function.
This generates a temporary pdf file and opens it.

Alternatively, debug=True can be selected for setup.
In this case, the correct fonts are not displayed.
"""
