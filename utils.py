'''

    Different utility functions for the main notebook

'''

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
