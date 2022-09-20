import pandas as pd

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
