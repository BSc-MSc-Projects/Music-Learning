'''
Utility functions for plotting
'''
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


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
# @param legend: list with bar legend
#
def three_group_bar_plot(metrics_array_1, metrics_array_2, metrics_array_3, labels, 
        title, xlabel, ylabel, legend):
    plt.figure(figsize=(30,15))
    X_axis = np.arange(len(labels))
    width = 0.25  # the width of the bars


    plt.bar(X_axis-0.25, metrics_array_1, width, label="plain")
    plt.bar(X_axis, metrics_array_2, width, label="oversampling")
    plt.bar(X_axis + 0.25, metrics_array_3, width, label="SMOTE")

    plt.xticks(X_axis, labels)

    plt.legend(legend)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


# Print confusion matrix using seaborn
#
# @param svm_cm:    confusion matrix
# @param labels:    labels for matrix axis
# @param title:     matrix title
#
def print_cm(svm_cm, labels, title):
    dims = (13.7, 10.27)
    fig, ax = plt.subplots(figsize=dims)
    plt.title(title)
    sns.heatmap(svm_cm, annot=True, linewidths=.5, ax=ax, 
            xticklabels=labels, yticklabels=labels, fmt='g', vmin=0, vmax=500)


# Bar plot used to compare the best cases of the five classifier
#
# @param metrics_array_1: array for the first column
# @param metrics_array_2: array for the second column
# @param metrics_array_3: array for the third column
# @param metrics_array_4: array for the fourth column
# @param metrics_array_5: array for the fifth column
# @param labels: labels array
# @param title: chart title
# @param xlabel: x-axis label
# @param ylabel: y-axis label
# @param legend: list with bar legend
#
def five_group_bar_plot(metrics_array_1, metrics_array_2, metrics_array_3, metrics_array_4, 
        metrics_array_5, labels, 
        title, xlabel, ylabel, legend):
    plt.figure(figsize=(30,15))
    X_axis = np.arange(len(labels))
    width = 0.11  # the width of the bars


    plt.bar(X_axis - 0.26, metrics_array_1, width, label="Support Vector Machine")
    plt.bar(X_axis - 0.13, metrics_array_2, width, label="Logistic Regression")
    plt.bar(X_axis, metrics_array_3, width, label="KNeighbors")
    plt.bar(X_axis + 0.13, metrics_array_4, width, label="Multilayer Perceptron")
    plt.bar(X_axis + 0.26, metrics_array_5, width, label="Decision Tree")


    plt.xticks(X_axis, labels)

    plt.legend(legend)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)