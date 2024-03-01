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

setup(width=5, height=5, unit="cm", font_size=8, serif=False)
# setup(width=5, height=5, unit="cm", serif=False, font_size=8, debug=True)
"""
a call to setup with parameters does all the stuff that setup
wthout parameters does (see simple_setup.py).
In addition, the size of the plot can be defined via width and height.
A unit ("in", "pt" or "cm") must be specified. If only a height or a width plus
unit is specified, the corresponding other size is calculated via
the golden ratio.
Tip: With \showthe\columnwidth you can display the column width of the text
in pt in Latex

With serif=False serifs can be removed.

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
# plt.show()
"""
The only disadvantage of using the setup function is that by using pgf,
the python internal GUI for plots (plt.show()) is no longer supported.
If you still want to view the file directly you can use the show() function.
This generates a temporary pdf file and opens it.

Alternatively, debug=True can be selected for setup.
In this case, the correct fonts are not displayed.
"""
