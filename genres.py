import pandas as pd
import operator


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
    black_list = ["", "Soundtrack", "Other", "Unknown", "Unclassifiable"]
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
    if "Spoken" in black_list:
        black_list.remove("Spoken")
    if "Soul-RnB" in black_list:
        black_list.remove("Soul-RnB")
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
            if "noise" in genre:
                df.loc[i, "genre"] = "Noise"
            if "house" in genre:
                df.loc[i, "genre"] = "Electronic"
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
            if "reggae" in genre:
                df.loc[i, "genre"] = "Reggae"
            if "dub" in genre:
                df.loc[i, "genre"] = "Reggae"
            if "instrumental" in genre:
                df.loc[i, "genre"] = "Instrumental"
            if "surrism-phonoethics" in genre:
                df.loc[i, "genre"] = "Electronic"
            if "alternative" in genre:
                df.loc[i, "genre"] = "Alternative"
            if "shoegaze" in genre:
                df.loc[i, "genre"] = "Alternative"
            if "experimental" in genre:
                df.loc[i, "genre"] = "Experimental"
            if "international" in genre:
                df.loc[i, "genre"] = "International"
            if "avant" in genre:
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
            if "hard" in genre:
                df.loc[i, "genre"] = "Hardcore"
            if "core" in genre:
                df.loc[i, "genre"] = "Hardcore"
            if "rock" in genre:
                df.loc[i, "genre"] = "Rock"
            if "garage" in genre:
                df.loc[i, "genre"] = "Rock"
            if "techno" in genre:
                df.loc[i, "genre"] = "Electronic"
            if "metal" in genre:
                df.loc[i, "genre"] = "Metal"
            if "lo-fi" in genre:
                df.loc[i, "genre"] = "Lo-Fi"
            if "pop" in genre:
                df.loc[i, "genre"] = "Pop"
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
            if "spoken" in genre:
                df.loc[i, "genre"] = "Spoken"
            if "country" in genre:
                df.loc[i, "genre"] = "Country"
            if "bluegrass" in genre:
                df.loc[i, "genre"] = "Country"
            if "soul" in genre:
                df.loc[i, "genre"] = "Soul-RnB"
            if "rnb" in genre:
                df.loc[i, "genre"] = "Soul-RnB"


def post_processing(file_name):

    file_name_out = ".\\out.csv"

    df = pd.read_csv(file_name, encoding='latin-1')

    #count_genres(df, 1)
    reduce_subgenres(df)

    #count_genres(df, 1)
    df = delete_unkown(df)

    #count_genres(df, 1)
    #count_genres(df, 100)
    df = delete_outlayers(df, 100)

    df.to_csv(file_name_out, index=False)
    print("csv file is ready")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_name = ".\\raw_csv_file.csv"
    post_processing(file_name)
