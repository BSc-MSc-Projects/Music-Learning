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
        if genres[k] < threshold:  # to update
            genres.pop(k, None)
        else:
            dataset_elements = dataset_elements + genres[k]
    print("dataset = ", dataset_elements)
    sorted_genres = sorted(genres.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_genres)
    print(len(sorted_genres))


def delete_unkown(df):
    black_list = ["", "Soundtrack", "Other", "Unknown"]
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
        if genres[k] >= threshold:  # to update
            genres.pop(k, None)

    black_list = genres.keys()
    #print(black_list)
    row_to_del = []
    for i, row in df.iterrows():
        for name in black_list:
            if df.loc[i, "genre"] == name:
                row_to_del.append(i)
    df = df.drop(row_to_del)
    return df


def manage_genres():
    file_name = "C:\\Users\\Gian Marco\\Desktop\\csv_file.csv"
    file_name_out = ".\\out.csv"

    df = pd.read_csv(file_name, encoding='latin-1')

    count_genres(df, 1)

    for i, row in df.iterrows():
        if not isinstance(row["genre"], float):
            genre = row["genre"].lower()
            if "noise" in genre:
                df.loc[i, "genre"] = "Noise"
            if "glitch" in genre:
                df.loc[i, "genre"] = "Electronic"
            if "electr" in genre:
                df.loc[i, "genre"] = "Electronic"
            if "afr" in genre:
                df.loc[i, "genre"] = "African"
            if "idm" in genre:
                df.loc[i, "genre"] = "IDM"
            if "reggae" in genre:
                df.loc[i, "genre"] = "Reggae"
            if "dub" in genre:
                df.loc[i, "genre"] = "Reggae"
            if "instrumental" in genre:
                df.loc[i, "genre"] = "Instrumental"
            if "dance" in genre:
                df.loc[i, "genre"] = "Dance"
            if "collage" in genre:
                df.loc[i, "genre"] = "Audio Collage"
            if "field" in genre:
                df.loc[i, "genre"] = "Field Recordings"
            if "surrism-phonoethics" in genre:
                df.loc[i, "genre"] = "suRRism-Phonoethics"
            if "spoken" in genre:
                df.loc[i, "genre"] = "Spoken"
            if "bluegrass" in genre:
                df.loc[i, "genre"] = "Country"
            if "hip-hop" in genre:
                df.loc[i, "genre"] = "Hip-Hop"
            if "hip hop" in genre:
                df.loc[i, "genre"] = "Hip-Hop"
            if "international" in genre:
                df.loc[i, "genre"] = "International"
            if "chip" in genre:
                df.loc[i, "genre"] = "Chip Music"
            if "avant" in genre:
                df.loc[i, "genre"] = "Avant-Garde"
            if "classical" in genre:
                df.loc[i, "genre"] = "Classical"
            if "trip-hop" in genre:
                df.loc[i, "genre"] = "Trip-Hop"
            if "trip hop" in genre:
                df.loc[i, "genre"] = "Trip-Hop"
            if "downtempo" in genre:
                df.loc[i, "genre"] = "Trip-Hop"
            if "blues" in genre:
                df.loc[i, "genre"] = "Blues"
            if "ambient" in genre:
                df.loc[i, "genre"] = "Ambient"
            if "hard" in genre:
                df.loc[i, "genre"] = "Hardcore"
            if "latin" in genre:
                df.loc[i, "genre"] = "Latin America"
            if "minimal" in genre:
                df.loc[i, "genre"] = "Minimal"
            if "rock" in genre:
                df.loc[i, "genre"] = "Rock"
            if "psych" in genre:
                df.loc[i, "genre"] = "Psychedelic"
            if "indie" in genre:
                df.loc[i, "genre"] = "Indie"
            if "psych-rock" in genre:
                df.loc[i, "genre"] = "Psych-Rock"
            if "indie-rock" in genre:
                df.loc[i, "genre"] = "Indie-Rock"
            if "indie rock" in genre:
                df.loc[i, "genre"] = "Indie-Rock"
            if "indy rock" in genre:
                df.loc[i, "genre"] = "Indie-Rock"
            if "experimental" in genre:
                df.loc[i, "genre"] = "Experimental"
            if "alternative" in genre:
                df.loc[i, "genre"] = "Alternative"
            if "shoegaze" in genre:
                df.loc[i, "genre"] = "Alternative"
            if "ambient electronic" in genre:
                df.loc[i, "genre"] = "Ambient Electronic"
            if "pop" in genre:
                df.loc[i, "genre"] = "Pop"
            if "experimental pop" in genre:
                df.loc[i, "genre"] = "Experimental Pop"
            if "garage" in genre:
                df.loc[i, "genre"] = "Garage"
            if "techno" in genre:
                df.loc[i, "genre"] = "Techno"
            if "jazz" in genre:
                df.loc[i, "genre"] = "Jazz"
            if "metal" in genre:
                df.loc[i, "genre"] = "Metal"
            if "lo-fi" in genre:
                df.loc[i, "genre"] = "Lo-Fi"
            if "no wave" in genre:
                df.loc[i, "genre"] = "No Wave"
            if "rap" in genre:
                df.loc[i, "genre"] = "Rap"
            if "folk" in genre:
                df.loc[i, "genre"] = "Folk"
            if "disco" in genre:
                df.loc[i, "genre"] = "Disco"
            if "punk" in genre:
                df.loc[i, "genre"] = "Punk"
            if "soul" in genre:
                df.loc[i, "genre"] = "Soul-RnB"
            if "r&b" in genre:
                df.loc[i, "genre"] = "Soul-RnB"

            # valuta ordine elementi, ultimo è più presente

    count_genres(df, 1)

    df = delete_unkown(df)

    count_genres(df, 1)
    #count_genres(df, 5)
    count_genres(df, 15)
    df = delete_outlayers(df, 15)

    df.to_csv(file_name_out, index=False)
    print("csv file is ready")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    manage_genres()
