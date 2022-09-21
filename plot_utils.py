'''
Utility functions for plotting
'''
import matplotlib.pyplot as plt


# As simple as plotting with plt.plot()
#
# @param fig_size:  tuple, for changing the figure figure figure size
# @param x_array:   x axis data
# @param y_array:   y axis data
# @param x_label:   x axis label
# @param y_label:   y axis label
# @param title:     plot title 
#
def basic_plot(fig_size, x_array, y_array, x_label, y_label, title):
    plt.figure(figsize=fig_size)
    plt.plot(x_array, y_array)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
