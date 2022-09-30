'''
Utility functions for plotting
'''
import matplotlib.pyplot as plt
import numpy as np


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


# Basic barplot utility
#
# @param fig_size:  tuple, for changing the figure figure figure size
# @param x_array:   x axis data
# @param labels:    label array data 
# @param title:     plot title 
#
def bar_plot(fig_size, x_array, labels, title):
    plt.figure(figsize=fig_size)
    plt.bar(labels, x_array)
    plt.title(title)
    plt.show()


# Bar plot used to compare classifier with plain config, SMOTE and oversampling
#
# @param metrics_array_1: array for the first column
# @param metrics_array_2: array for the second column
# @param metrics_array_3: array for the third column
# @param labels: labels array
# @param title: chart title
# @param xlabel: x-axis label
# @param ylabel: y-axis label
#
def three_group_bar_plot(metrics_array_1, metrics_array_2, metrics_array_3, labels, title, xlabel, ylabel):
    plt.figure(figsize=(30,15))
    X_axis = np.arange(len(labels))
    width = 0.25  # the width of the bars


    plt.bar(X_axis-0.25, metrics_array_1, width, label="plain")
    plt.bar(X_axis, metrics_array_2, width, label="oversampling")
    plt.bar(X_axis + 0.25, metrics_array_3, width, label="SMOTE")

    plt.xticks(X_axis, labels)

    plt.legend(["Plain", "Oversampling", "SMOTE"])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
