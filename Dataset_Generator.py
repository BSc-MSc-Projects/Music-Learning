#Imports

import numpy as np
import scipy
import pandas as pd
import librosa
import librosa.display
import os
import csv
from tinytag import TinyTag
import operator


def get_mfcc(y, sr):
    mfcc = np.array(librosa.feature.mfcc(y=y, sr=sr))
    return mfcc


def get_melspectrogram(y, sr):
    melspectrogram = np.array(librosa.feature.melspectrogram(y=y, sr=sr))
    return melspectrogram


def get_chroma_stft(y, sr):
    chroma_stft = np.array(librosa.feature.chroma_stft(y=y, sr=sr))
    return chroma_stft


def get_tonnetz(y, sr):
    tonnetz = np.array(librosa.feature.tonnetz(y=y, sr=sr))
    return tonnetz


def get_chroma_cqt(y, sr):
    chroma_cqt = np.array(librosa.feature.chroma_cqt(y=y, sr=sr))
    return chroma_cqt


def get_chroma_cens(y, sr):
    chroma_cens = np.array(librosa.feature.chroma_cens(y=y, sr=sr))
    return chroma_cens


def get_spectral_centroid(y, sr):
    spectral_centroid = np.array(librosa.feature.spectral_centroid(y=y, sr=sr))
    return spectral_centroid


def get_spectral_bandwidth(y, sr):
    spectral_bandwidth = np.array(librosa.feature.spectral_bandwidth(y=y, sr=sr))
    return spectral_bandwidth


def get_spectral_contrast(y, sr):
    spectral_contrast = np.array(librosa.feature.spectral_contrast(y=y, sr=sr))
    return spectral_contrast


def get_spectral_flatness(y):
    spectral_flatness = np.array(librosa.feature.spectral_flatness(y=y))
    return spectral_flatness


def get_spectral_rolloff(y, sr):
    spectral_rolloff = np.array(librosa.feature.spectral_rolloff(y=y, sr=sr))
    return spectral_rolloff


def get_poly_features(y, sr):
    poly_features = np.array(librosa.feature.poly_features(y=y, sr=sr))
    return poly_features


def get_rms(y):
    rms = np.array(librosa.feature.rms(y=y))
    return rms


def get_zero_crossing_rate(y):
    zero_crossing_rate = np.array(librosa.feature.zero_crossing_rate(y=y))
    return zero_crossing_rate


def get_tempogram(y, sr):
    tempogram = np.array(librosa.feature.tempogram(y=y, sr=sr))
    return tempogram


def get_fourier_tempogram(y, sr):
    fourier_tempogram = np.array(librosa.feature.fourier_tempogram(y=y, sr=sr))
    return fourier_tempogram


def calculate_metrics(array):
    features = []
    mean = np.mean(array)
    value_min = np.min(array)
    value_max = np.max(array)
    median = np.median(array)
    std = np.std(array)
    skew = scipy.stats.skew(array, axis=None)
    kurtosis = scipy.stats.kurtosis(array, axis=None)
    features.append(mean)
    features.append(value_min)
    features.append(value_max)
    features.append(median)
    features.append(std)
    features.append(skew)
    features.append(kurtosis)
    return features


def get_features(writer):
    
    for dirpath, dirnames, filenames in os.walk("dataset"):
        for filename in filenames:
            if ".mp3" in filename:
                file_path = dirpath+"\\"+filename
                try:
                    tag = TinyTag.get(file_path)
                    row = [filename, tag.title, tag.artist, tag.album]
                    try:
                        y, sr = librosa.load(file_path, offset=0, duration=30)
                        row.extend(calculate_metrics(get_chroma_stft(y, sr)))
                        row.extend(calculate_metrics(get_chroma_cens(y, sr)))
                        row.extend(calculate_metrics(get_chroma_cqt(y, sr)))
                        row.extend(calculate_metrics(get_fourier_tempogram(y, sr)))
                        row.extend(calculate_metrics(get_melspectrogram(y, sr)))
                        row.extend(calculate_metrics(get_mfcc(y, sr)))
                        row.extend(calculate_metrics(get_poly_features(y, sr)))
                        row.extend(calculate_metrics(get_rms(y)))
                        row.extend(calculate_metrics(get_spectral_bandwidth(y, sr)))
                        row.extend(calculate_metrics(get_spectral_centroid(y, sr)))
                        row.extend(calculate_metrics(get_spectral_contrast(y, sr)))
                        row.extend(calculate_metrics(get_spectral_flatness(y)))
                        row.extend(calculate_metrics(get_spectral_rolloff(y, sr)))
                        row.extend(calculate_metrics(get_tempogram(y, sr)))
                        row.extend(calculate_metrics(get_tonnetz(y, sr)))
                        row.extend(calculate_metrics(get_zero_crossing_rate(y)))
                        row.append(tag.genre)
                        writer.writerow(row)
                    except:
                        print("librosa error: " + file_path)
                except:
                    print("tinyTag error: " + file_path)

        
def retrieve_header():
    header = ["filename", "title", "artist", "album"]
    features = ["chroma_stft", "chroma_cens", "chroma_cqt", "fourier_tempogram", "melspectrogram", "mfcc", "poly_features",
                "rms", "spectral_bandwidth", "spectral_centroid", "spectral_contrast", "spectral_flatness",
                "spectral_rolloff", "tempogram", "tonnetz", "zero_crossing_rate"]
    moments = ["mean", "min", "max", "median", "std", "skew", 'kurtosis']
    for feature in features:
        for moment in moments:
            header.append(feature + "_" + moment)
    header.append("genre")
    return header
  

def count_genres(df, threshold):
    # create an empty dictionary
    genres = {}
    for index, row in df.iterrows():
        genre = row["genre"]
        if genre in genres:
            new_value = genres[genre] + 1
            genres.update({genre: new_value})
        else:
            genres.update({genre: 1})

    dataset_elements = 0
    for k in genres.copy():
        if genres[k] <= threshold:
            genres.pop(k, None)
        else:
            dataset_elements = dataset_elements + genres[k]
    print("dataset = ", dataset_elements)
    sorted_genres = sorted(genres.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_genres)
    print(len(sorted_genres))


def delete_unkown(df):
    black_list = ["", "Soundtrack", "Other", "Unknown", "Unclassifiable", "Noise"]
    row_to_del = []
    df = df.dropna(subset = ['genre'])
    for i, row in df.iterrows():
        for name in black_list:
            if df.loc[i, "genre"] == name:
                row_to_del.append(i)
    df = df.drop(row_to_del)
    return df


def delete_outlayers(df, threshold):
    # create an empty dictionary
    genres = {}
    for index, row in df.iterrows():
        genre = row["genre"]
        if genre in genres:
            new_value = genres[genre] + 1
            genres.update({genre: new_value})
        else:
            genres.update({genre: 1})

    for k in genres.copy():
        if genres[k] > threshold:
            genres.pop(k, None)

    black_list = list(genres.keys())
    if "Country" in black_list:
        black_list.remove("Country")
    row_to_del = []
    for i, row in df.iterrows():
        for name in black_list:
            if df.loc[i, "genre"] == name:
                row_to_del.append(i)
    df = df.drop(row_to_del)
    return df


def reduce_subgenres(df):
    for i, row in df.iterrows():
        if not isinstance(row["genre"], float):
            genre = row["genre"].lower()
            if "soul" in genre:
                df.loc[i, "genre"] = "Soul-RnB"
            if "rnb" in genre:
                df.loc[i, "genre"] = "Soul-RnB"
            if "disco" in genre:
                df.loc[i, "genre"] = "Soul-RnB"
            if "funk" in genre:
                df.loc[i, "genre"] = "Soul-RnB"
            if "house" in genre:
                df.loc[i, "genre"] = "Electronic"
            if "pop" in genre:
                df.loc[i, "genre"] = "Pop"
            if "alternative" in genre:
                df.loc[i, "genre"] = "Alternative"
            if "experimental" in genre:
                df.loc[i, "genre"] = "Experimental"
            if "punk" in genre:
                df.loc[i, "genre"] = "Rock"
            if "ambient" in genre:
                df.loc[i, "genre"] = "Ambient"
            if "chip" in genre:
                df.loc[i, "genre"] = "Electronic"
            if "idm" in genre:
                df.loc[i, "genre"] = "Electronic"
            if "glitch" in genre:
                df.loc[i, "genre"] = "Electronic"
            if "instrumental" in genre:
                df.loc[i, "genre"] = "Instrumental"
            if "surrism-phonoethics" in genre:
                df.loc[i, "genre"] = "Electronic"
            if "shoegaze" in genre:
                df.loc[i, "genre"] = "Alternative"
            if "international" in genre:
                df.loc[i, "genre"] = "International"
            if "avant garde" in genre:
                df.loc[i, "genre"] = "Avant-Garde"
            if "avant-garde" in genre:
                df.loc[i, "genre"] = "Avant-Garde"
            if "classical" in genre:
                df.loc[i, "genre"] = "Classical"
            if "trip-hop" in genre:
                df.loc[i, "genre"] = "Electronic"
            if "trip hop" in genre:
                df.loc[i, "genre"] = "Electronic"
            if "downtempo" in genre:
                df.loc[i, "genre"] = "Electronic"
            if "blues" in genre:
                df.loc[i, "genre"] = "Blues"
            if "core" in genre:
                df.loc[i, "genre"] = "Hardcore"
            if "hard" in genre:
                df.loc[i, "genre"] = "Hardcore"
            if "rock" in genre:
                df.loc[i, "genre"] = "Rock"
            if "garage" in genre:
                df.loc[i, "genre"] = "Rock"
            if "techno" in genre:
                df.loc[i, "genre"] = "Electronic"
            if "metal" in genre:
                df.loc[i, "genre"] = "Metal"
            if "hip-hop" in genre:
                df.loc[i, "genre"] = "Hip-Hop"
            if "hip hop" in genre:
                df.loc[i, "genre"] = "Hip-Hop"
            if "electr" in genre:
                df.loc[i, "genre"] = "Electronic"
            if "jazz" in genre:
                df.loc[i, "genre"] = "Jazz"
            if "folk" in genre:
                df.loc[i, "genre"] = "Folk"
            if "country" in genre:
                df.loc[i, "genre"] = "Country"
            if "bluegrass" in genre:
                df.loc[i, "genre"] = "Country"


def post_processing(file_name):

    file_name_out = ".\\out.csv"

    df = pd.read_csv(file_name, encoding='latin-1')

    count_genres(df, 1)
    reduce_subgenres(df)

    count_genres(df, 1)
    df = delete_unkown(df)

    count_genres(df, 1)
    count_genres(df, 100)
    df = delete_outlayers(df, 100)

    df.to_csv(file_name_out, index=False)
    print("csv file is ready")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_name = ".\\raw_csv_file.csv"

    # open the file in the write mode\n
    f = open(file_name, 'w', newline='')
 
    # create the csv writer
    writer = csv.writer(f)

    # write header to the csv file
    header = retrieve_header()
    writer.writerow(header)

    # write data to the csv file
    get_features(writer)

    # close the file
    f.close()
    
    post_processing(file_name)
