'''
    Utility function to manage datasets
'''

import pandas as pd
import ast
import os

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
