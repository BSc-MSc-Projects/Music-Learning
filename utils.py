'''

    Different utility functions for the main notebook

'''

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import classification_report
import pandas as pd


# Write the Confusion Matrix on an output file,
# in the format of a csv
#
# @param cm:        confusion matrix
# @param labels:    genres labels list
# @param path:      csv file path
#
def write_cm_on_file(cm, labels, path):
    cm_file = open(path, "w")

    # write header, label names
    row = ""
    for label in labels:
        row += "," + label
        
    cm_file.write(row+"\n")


    row = ""
    index = 0
    for item in cm:
        row += labels[index]
        for value in item:
            row += ","+str(value)
        cm_file.write(row+"\n")
        row = ""
        index+=1
    cm_file.close()


# File loader
#
# @returns: filepath of the chosen file 
#
def open_file_dialog():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return filename


# Compute classification report, precision, recall, f1-score starting from a vector of predictions
#
# @param predictions: vector of predictions
# @param y_set: label to predict
# @param labels: classes labels
#
# @return a vector with the computed values
#
def compute_class_metrics(predictions, y_set, labels):

    metrics = []

    report = classification_report(y_set, predictions, output_dict=True, labels=labels)

    # format the report table
    accuracy = report["accuracy"]
    
    # delete accuracy from each row
    report.pop("accuracy")

    df = pd.DataFrame(report).transpose()
    df = df.astype({"precision": float, "recall": float, "f1-score": float, "support":int})
    df.style.set_caption("Metrics for SVM")

    # compute precision, recall, f1-score
    precision = precision_score(y_set, predictions, average=None, labels=labels)
    recall = recall_score(y_set, predictions, average=None, labels=labels)
    f1 = f1_score(y_set, predictions, average=None, labels=labels)

    metrics.append(df)
    metrics.append(precision)
    metrics.append(recall)
    metrics.append(f1)
    metrics.append(accuracy)
    return metrics


# Print accuracy table
#
# @param accuracy_dict: dictonary to format as pandas table
#
def print_acc_table(accuracy):
    accuracy_dict = {'Metric':["Accuracy"], 'Score':[accuracy]}
    accuracy_dict = pd.from_dict(accuracy_dict)
    accuracy_dict = accuracy_dict.astype({"Score": float})
    accuracy_dict
