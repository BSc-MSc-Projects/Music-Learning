'''

    Different utility functions for the main notebook

'''

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


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
