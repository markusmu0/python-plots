#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
import locale
import numpy as np
import datetime
import os
import platform
from cycler import cycler

POINT_TO_INCHES = 1.0/72.27
CM_TO_INCHES = 1.0/2.54
GOLDEN_MEAN = (np.sqrt(5)-1.0)/2.0
DEFAULT_COLORS = ['r', 'b', 'g', 'orange', 'k', 'cyan']
DEFAULT_LINESTYLES = ['-', '--', ':', '-.', (0, (1, 4.5)), (0, (3, 1, 1, 1, 1, 1))]

def align_legend_right(fig, legend):
    # Get the renderer instance
    renderer = fig.canvas.get_renderer()
    # Get the width of the widest label
    shift = max([t.get_window_extent(renderer).width for t in legend.get_texts()])

    # Set the horizontal alignment and position of all labels
    for t in legend.get_texts():
        t.set_ha('right') # ha is alias for horizontalalignment
        t.set_position((shift - t.get_window_extent(renderer).width,0))

def calculate_figure_size(width, height, unit):
    """
    Converts the figure dimensions and sets them to the golden mean if one of them is unspecified
    """
    if not width and not height:
        return None, None
    fig_height = width*GOLDEN_MEAN if height is None else height
    fig_width = height/GOLDEN_MEAN if width is None else width

    if unit == "pt":
        fig_width *= POINT_TO_INCHES
        fig_height *= POINT_TO_INCHES
    elif unit == "cm":
        fig_width *= CM_TO_INCHES
        fig_height *= CM_TO_INCHES
    elif unit != "in":
        raise ValueError("ERROR: You must specify a unit for your lengths! (pt, in, cm)")
    return fig_width, fig_height


def setup(width=None, height=None, unit=None, serif=True, font_size=10, debug=False, set_lines = True, metadata=None, colors = None, linestyles = None):
    """
    The function overwrites the default values for font, font size, figure size

    - width: width of the figure
    - height: height of the figure
    - unit: unit of width and height ("in", "pt" or "cm")
    - serif: with or without serifs
    - font_size: size of the font
    - set_lines: sets the style of lines (linestyle and color)
    - metadata: save metadata for the figure. use a dict
      (see metadata at
      https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)
    - colors : set of colors through which the lines rotate (default if None)
    - linestyles : list of linestyles through which the lines rotate (default if None)

    debug=True allows to use the GUI of Python (plt.show()),
    but it does not show the correct fonts

    for exact behavior see example files
    """

    if not debug:
        mpl.use('pgf')      # Does not support plt.show()!!

    fig_width, fig_height = calculate_figure_size(width, height, unit)
    if fig_width:
        # Update default value for figure size
        plt.rcParams.update({'figure.figsize': [fig_width, fig_height]})

    def metadata_to_str(k,v):
        value =str(v).replace("_", "\_")
        key="pdf"+str(k).lower()
        return f'{key}={{{value}}}'

    font = "serif" if serif else "sans-serif"
    preamble = "\n".join([r"\usepackage[utf8x]{inputenc}",
                          r"\usepackage[T1]{fontenc}"])
    if metadata:
        pdfinfo = ','.join(metadata_to_str(k, v) for k, v in metadata.items())
        preamble = preamble+"\n"+r"\usepackage{hyperref}\hypersetup{%s}" % pdfinfo

    if not serif:
        preamble = preamble+"\n"+r"\usepackage{cmbright}"

    tex_fonts = {
        # Use pgf to get latex font
        "pgf.texsystem": "pdflatex",
        "pgf.preamble": preamble,
        "font.family": font,
        # Use 10pt font in plots, to match 10pt font in document
        "axes.labelsize": font_size,
        "font.size": font_size,
        # Make the legend/label fonts a little smaller
        "legend.fontsize": .7 * font_size,
        "xtick.labelsize": .7 * font_size,
        "ytick.labelsize": .7 * font_size
        }

    # Update default values
    plt.rcParams.update(tex_fonts)

    if set_lines or colors or linestyles:
        color = colors or DEFAULT_COLORS
        lines = linestyles or DEFAULT_LINESTYLES
        length = min(len(color), len(lines))
        plt.rcParams.update({'axes.prop_cycle':
                            (cycler(color = color[:length])
                             + cycler(linestyle = lines[:length]))})

def adjust_axes(ax, major_size=5, minor_size=1.5, width=0.5):
    # Edit the major and minor ticks of the x and y axes
    ax.minorticks_on()
    ax.xaxis.set_tick_params(which='major', size=major_size, width=width,
                            direction='in', top=True)
    ax.xaxis.set_tick_params(which='minor', size=minor_size, width=width,
                            direction='in', top=True)
    ax.yaxis.set_tick_params(which='major', size=major_size, width=width,
                            direction='in', right=True)
    ax.yaxis.set_tick_params(which='minor', size=minor_size, width=width,
                            direction='in', right=True)
    # set the number style
    ax.ticklabel_format(style='sci', axis='y', scilimits=(-3, 3),
                        useLocale=True, useMathText=True)
    ax.ticklabel_format(style='sci', axis='x', scilimits=(-4, 4),
                        useLocale=True, useMathText=True)
    # sets the x plot range to the data range
    ax.autoscale(enable=True, axis='x', tight=True)
    # ax.xaxis.labelpad = 5 padding between label and tick label
    ax.yaxis.labelpad = 5 # padding between label and tick label

def make_figure(width=None, height=None, unit=None, serif=True,
                de=False, plots=None, output_file=None,
                default_axes=False, other_axes=None, metadata=None,
                font_size=10, num_subplots_x=1, num_subplots_y=1, 
                width_ratios=None, height_ratios=None, sharex=False, sharey=False,
                tight_layout=False, debug=False, set_lines=True, colors = None, linestyles = None):
    """
    The function overwrites the default values for font, font size, figure size
    and creates a figure with modified axes and ticks.
    If desired, plotting and saving can be done directly.

    - width: width of the figure
    - height: height of the figure
    - unit: unit of width and height ("in", "pt" or "cm")
    - serif: with or without serifs
    - de: german number format activated
    - plots: function that takes fig and ax and performs the plots
    - output_file: Path and Name of the File that saves the figure
    - default_axes: if you whish to use the default axes
      (always True, when using subplots)
    - other_axes: if you whish to use other axes
      For this you specify a 4-tuple. See 'rect' at
      https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.axes.html
      (deactivated when using subplots)
    - metadata: save metadata in the output_file. use a dict
      (see metadata at
      https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)
    - font_size: size of the font
    - num_subplots_x: number of subplots in x direction 
      (deactivates other_axes) (default is 1)
    - num_subplots_y: number of subplots in y direction 
      (deactivates other_axes) (default is 1) 
    - width_ratios/height_ratios: only relevant if num_subplots>1, 
      see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
    - sharex: only relevant if num_subplots_y>1; if True: share x axis (default if False)
      one can remove whitespace with plt.subplots_adjust(hspace=.0)
    - sharey: only relevant if num_subplots_x>1; if True: share y axis (default if False)
    - tight_layout: plt.tight_layout() (only useful with subplots)
    - set_lines: sets the style of lines (linestyle and color)
    - colors : list of colors through which the lines rotate (default if None)
    - linestyles : list of linestyles through which the lines rotate (default if None)

    debug=True allows to use the GUI of Python (plt.show()),
    but it does not show the correct fonts

    for exact behavior see example files
    """

    setup(width, height, unit, serif, font_size, debug, set_lines, metadata, colors, linestyles)


    # creates figure
    fig, ax = plt.subplots(num_subplots_y, num_subplots_x, gridspec_kw={"width_ratios": width_ratios, "height_ratios": height_ratios}, sharex=sharex, sharey=sharey)

    # overwrites axes
    if not default_axes and num_subplots_x==1 and num_subplots_y==1:
        fig.clf()
        # arbitrarily selected ratio between offset and wide
        xoff = 0.207-0.014*fig.get_size_inches()[0]
        yoff = xoff
        default = [xoff, yoff, 1-1.5*xoff, 1-1.5*yoff]  # x, y, width, height
        ax = plt.axes(other_axes if other_axes else default)

    # sets german number format
    if de:
        locale.setlocale(locale.LC_ALL, "de_DE.utf8" if platform.system() == "Linux" else "deu_deu")

    if num_subplots_x==1 and num_subplots_y==1:
        ax=np.array([ax])

    for a in ax:
        adjust_axes(a)

    if num_subplots_x==1 and num_subplots_y==1:
        ax=ax[0]
    elif tight_layout:
        plt.tight_layout()

    # performs and saves the plots
    if plots:
        plots(fig, ax)
        if output_file:
            file_extension = os.path.splitext(output_file)[1]
            fig.savefig(output_file, format=file_extension[1:])
    return fig, ax


def show(fig):
    """
    this function saves a figure temporary and opens it with evince.
    After the file is closed it will be deleted
    """
    file = "/tmp/figure_show"\
        + datetime.datetime.now().strftime("%y%m%d_%H%M%S")+".pdf"
    fig.savefig(file, format="pdf")
    os.system("evince "+file)
    os.remove(file)
