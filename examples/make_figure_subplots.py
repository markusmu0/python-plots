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

x1 = np.linspace(0, 20, 300)
y1 = np.sin(x1)
x2 = 2*x1
y2 = np.cos(x2)

fig, ax = make_figure(num_subplots_x=1, num_subplots_y=2, tight_layout=False)
#fig, ax = make_figure(debug=True)
"""
These parameters of make_figure allow multiple axes in one figure.
* tight_layout reduces the white space around the axes

debug=True allows to use the GUI of Python (plt.show()),
but it does not show the correct fonts
"""

ax[0].plot(x1, y1, label="sin")
ax[1].plot(x2, y2, label="cos")
ax[0].legend()
ax[1].legend()
ax[1].set_xlabel("x values")
ax[0].set_ylabel("y values")
ax[1].set_ylabel("y values")
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
