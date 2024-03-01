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


def plots(fig, ax):
    ax.plot(x, 1e4*y1, label="sin")
    ax.plot(x, 1e4*y2, label="cos")
    ax.legend()
    ax.set_xlabel("x values")
    ax.set_ylabel("y values")
    """
    Attention: some commands are called differently for the axes:
    plt.xlabel -> ax.set_xlabel
    """


make_figure(width=10, height=7, unit="cm", other_axes=[0.17, 0.15, 0.95-0.15, 0.9-0.15], output_file=os.path.join(os.path.dirname(__file__), "example.svg"), plots=plots)
# make_figure(width=10, height=7, unit="cm", other_axes=[0.17, 0.15, 0.95-0.15, 0.9-0.15], output_file=os.path.join(os.path.dirname(__file__), "example.svg"), plots=plots, debug=True)
"""
basic explanation see make_figure_parameters.py
new features:
* with other_axes you can configure your own axes.
  For this you specify a 4-tuple. See 'rect' at
  https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.axes.html
* By passing a function which uses fig and ax as parameters,
  it is possible to plot directly with make_figure.
  If an output_file is additionally specified, the figure is saved.

debug=True allows to use the GUI of Python (plt.show()),
but it does not show the correct fonts
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
