#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import cm  # Colormaps
import matplotlib.ticker as ticker

def generate_formatter(arr, decimals = 2):
    """
        Generate a formatter which returns strings of values from a given array with the given decimal precision
    """
    def formatter(value, pos=None):
        new_v = arr[int(value) if value < len(arr) else 0]
        if new_v == 0:
            return 0
        if abs(new_v) < 1e-3 or abs(new_v) >= 1e3:
            return f"%.{decimals}e" % new_v
        else:
            return f"%.{decimals}f" % new_v
    return formatter

def contourplot(fig, ax, x, y, z, x_label = None, y_label = None, z_label = None, zmin = None, zmax = None,
                x_decimals = 2, y_decimals = 2, cmap = cm.seismic, center_around_zero = False):
    """
    The function generates a contourplot

    - fig: figure object (can be generated e.g. with fig=plt.figure())
    - ax: axes object (can be generated e.g. with ax=fig.gca())
    - x: x values
    - y: y values
    - z: z values, should be a 2D array with shape [x.size,y.size]
    - cmap: matplotlib colormap (see https://matplotlib.org/stable/gallery/color/colormap_reference.html)
    - z_label: label along the colormap
    - center_around_zero: if True, it centers the colormap around zero (dafault is False)
    """
    zmax = zmax or np.max(z)
    zmin = zmin or np.min(z)
    if center_around_zero:
        zmax = np.max(np.abs(z))
        zmin = -zmax
    con = ax.imshow(z.transpose(), cmap = cmap, vmin = zmin, vmax = zmax, aspect = "auto", origin = "lower")

    my_x_formatter = generate_formatter(x, decimals = x_decimals)
    my_y_formatter = generate_formatter(y, decimals = y_decimals)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(my_x_formatter))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(my_y_formatter))

    ax.set_xlim((0, len(x)-1))
    ax.set_ylim((0, len(y)-1))
    if x_label:
        ax.set_xlabel(x_label)
    if y_label:
        ax.set_ylabel(y_label)
    cb = fig.colorbar(con, shrink=0.7, aspect=10)
    if z_label:
        cb.set_label(z_label)
    return fig, ax
