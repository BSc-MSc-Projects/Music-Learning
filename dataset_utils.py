'''
    Utility function to manage datasets
'''

import pandas as pd
import ast
import os
from os.path import exists

from collections import Counter

rm_file = "run_metrics.csv"

# There are some columns that have complex numbers as values. These columns are recognized and
# deleted from the feature dataset
# @param feature_df: feature dataset
#
# @returns: a list with the names of the columns to discard
def drop_complex_cols(feature_df):
    fourier_cols = []
    for index in range(len(feature_df)):
        for col in feature_df.columns:
            # we got the complex number, in the form (Re, Im)
            if isinstance(feature_df[col][index], str) and col != "genre":
                if col not in fourier_cols: # check if the col is already in the set
                    fourier_cols.append(col)
    return fourier_cols


# Extract the top 16 genres from the FMA 'genres.csv' file and return them into a list
# @param file_pah: path to csv file
# 
# @returns a list with the top genres
def get_top_genres(file_path):
    ds_genres = pd.read_csv(file_path)
    top_genres = []
    
    parents = ds_genres['parent']
    name = ds_genres['title']
    for index in range (len(parents)):
        if parents[index] == 0:
            top_genres.append(name[index])
    return top_genres


# Credits: TODO: metti il link github al repository FMA 
def load(filepath):
    filename = os.path.basename(filepath)

    if 'features' in filename:
        return pd.read_csv(filepath, index_col=0, header=[0, 1, 2])

    if 'echonest' in filename:
        return pd.read_csv(filepath, index_col=0, header=[0, 1, 2])

    if 'genres' in filename:
        return pd.read_csv(filepath, index_col=0)

    if 'tracks' in filename:
        tracks = pd.read_csv(filepath, index_col=0, header=[0, 1])

        COLUMNS = [('track', 'tags'), ('album', 'tags'), ('artist', 'tags'),
                   ('track', 'genres'), ('track', 'genres_all')]
        for column in COLUMNS:
            tracks[column] = tracks[column].map(ast.literal_eval)

        COLUMNS = [('track', 'date_created'), ('track', 'date_recorded'),
                   ('album', 'date_created'), ('album', 'date_released'),
                   ('artist', 'date_created'), ('artist', 'active_year_begin'),
                   ('artist', 'active_year_end')]
        for column in COLUMNS:
            tracks[column] = pd.to_datetime(tracks[column])

        SUBSETS = ('small', 'medium', 'large')
        try:
            tracks['set', 'subset'] = tracks['set', 'subset'].astype(
                    'category', categories=SUBSETS, ordered=True)
        except (ValueError, TypeError):
            # the categories and ordered arguments were removed in pandas 0.25
            tracks['set', 'subset'] = tracks['set', 'subset'].astype(
                     pd.CategoricalDtype(categories=SUBSETS, ordered=True))

        COLUMNS = [('track', 'genre_top'), ('track', 'license'),
                   ('album', 'type'), ('album', 'information'),
                   ('artist', 'bio')]
        for column in COLUMNS:
            tracks[column] = tracks[column].astype('category')

        return tracks



# Functions for metrics comparison based on different execution profiles


# @brief check if the metrics file exists, if not write the header line
#
def write_metrics_header():
    header_line = "Classifier,SMOTE,FS,PCA,OVERS,Precision,Recall,F1\n"
    if not exists(rm_file):
        f = open(rm_file, "a")
        f.write(header_line)
        f.close()


# @brief Write a metrics line in the overall file
#
# @param clf: string, classifier name
# @param profile: the EXECUTION_PROFILE from .ipynb file
# @param precisions: computed precision for each class
# @param recalls: computed recall for each class
# @param f1s: computed f1 for each class
# @param y_test: test labels
#
def write_metrics(clf, profile, precisions, recalls, f1s, y_test):

    f = open(rm_file, "a")  # open file in append mode
    line = clf + "," + str(profile["SMOTE"])+","+str(profile["FS"])+","+str(profile["PCA"])+","+str(profile["OVERS"])+","

    tot_precision = 0.0
    tot_recall = 0.0
    tot_f1 = 0.0
    
    test_counter = Counter(y_test)
    for k,v in test_counter.items():
        print("key {}")
        tot_precision += precisions[k]*v
        tot_recall += recalls[k]*v
        tot_f1 += f1s[k]*v
    
    # Add to the line the computed metrics
    line += str(tot_precision/len(y_test))+","+str(tot_recall/len(y_test))+","+str(tot_f1/len(y_test))+"\n"
    print(line)
    f.write(line)
    f.close()


# @brief write the header of a tuning csv file
# @param filename: path of the file
# @param header_line: the header to write
#
def write_tuning_header(filename, header_line):
    if not exists(filename):
        f = open(filename, "a")
        f.write(header_line)
        f.close()


# @brief write a line on a tuning csv file 
# @param filename: path of the file
# @param header_line: the line to write
#
def write_on_tuning_file(filename, line):
    f = open(filename, "a")
    f.write(line)
    f.close()
