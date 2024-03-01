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

x = np.linspace(0, 20, 300)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = make_figure(width=10, height=7, unit="cm", serif=False, de=True, default_axes=True)
# fig, ax = make_figure(width=10, height=7, unit="cm", serif=False, de=True, default_axes=True, debug=True)
"""
make_figure with parameters does the following in addition to what happens
without parameters (see simple_make_figure.py):
* setup with parameters is executed as described in setup_parameters.py;
* German number format is activated with de=True
* Default axes are used with default_axes=True

debug=True allows to use the GUI of Python (plt.show()),
but it does not show the correct fonts
"""

ax.plot(x, 1e4*y1, label="sin")
ax.plot(x, 1e4*y2, label="cos")
ax.legend()
ax.set_xlabel("x values")
ax.set_ylabel("y values")
"""
Attention: some commands are called differently for the axes:
plt.xlabel -> ax.set_xlabel
"""
show(fig)
# plt.show()
"""
The only disadvantage of using the setup function is that by using pgf,
the python internal GUI for plots (plt.show()) is no longer supported.
If you still want to view the file directly you can use the show() function.
This generates a temporary pdf file and opens it.

Alternatively, debug=True can be selected for setup.
In this case, the correct fonts are not displayed.
"""
