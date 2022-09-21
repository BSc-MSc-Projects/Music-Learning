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
        if genres[k] <= threshold:  # to update
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
        if genres[k] > threshold:  # to update
            genres.pop(k, None)

    black_list = list(genres.keys())
    black_list.remove("Country")
    black_list.remove("Spoken")
    black_list.remove("Soul-RnB")
    black_list.remove("Disco")      # forse da togliere
    black_list.remove("Balkan")
    black_list.remove("Industrial")
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
            #if "dance" in genre:
            #    df.loc[i, "genre"] = "Dance"
            #if "collage" in genre:
            #    df.loc[i, "genre"] = "Audio Collage"
            #if "field" in genre:
            #    df.loc[i, "genre"] = "Field Recordings"
            if "surrism-phonoethics" in genre:
                df.loc[i, "genre"] = "Experimental"  # or Electronic
            if "alternative" in genre:
                df.loc[i, "genre"] = "Alternative"
            if "shoegaze" in genre:
                df.loc[i, "genre"] = "Alternative"
            if "pop" in genre:
                df.loc[i, "genre"] = "Pop"
            if "hip-hop" in genre:
                df.loc[i, "genre"] = "Hip-Hop"
            if "hip hop" in genre:
                df.loc[i, "genre"] = "Hip-Hop"
            if "international" in genre:
                df.loc[i, "genre"] = "International"
            if "avant" in genre:
                df.loc[i, "genre"] = "Avant-Garde"
            if "classical" in genre:
                df.loc[i, "genre"] = "Classical"
            if "trip-hop" in genre:
                df.loc[i, "genre"] = "Hip-Hop"  # or Electronic
            if "trip hop" in genre:
                df.loc[i, "genre"] = "Hip-Hop"  # or Electronic
            #if "minimal" in genre:
            #    df.loc[i, "genre"] = "Minimal"
            if "downtempo" in genre:
                df.loc[i, "genre"] = "Electronic"  # or Hip-Hop
            if "blues" in genre:
                df.loc[i, "genre"] = "Blues"
            if "hard" in genre:
                df.loc[i, "genre"] = "Hardcore"
            if "core" in genre:
                df.loc[i, "genre"] = "Hardcore"
            #if "latin" in genre:
            #    df.loc[i, "genre"] = "Latin America"
            #if "indie" in genre:
            #    df.loc[i, "genre"] = "Indie"
            if "experimental" in genre:
                df.loc[i, "genre"] = "Experimental"
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
            #if "no wave" in genre:
            #    df.loc[i, "genre"] = "No Wave"
            if "electr" in genre:
                df.loc[i, "genre"] = "Electronic"
            if "jazz" in genre:
                df.loc[i, "genre"] = "Jazz"
            #if "rap" in genre:
            #    df.loc[i, "genre"] = "Rap"
            if "folk" in genre:
                df.loc[i, "genre"] = "Folk"
            #if "disco" in genre:
            #    df.loc[i, "genre"] = "Disco"
            if "spoken" in genre:
                df.loc[i, "genre"] = "Spoken"
            if "country" in genre:
                df.loc[i, "genre"] = "Country"
            if "bluegrass" in genre:
                df.loc[i, "genre"] = "Country"      #prova a commentare
            if "soul" in genre:
                df.loc[i, "genre"] = "Soul-RnB"
            if "rnb" in genre:
                df.loc[i, "genre"] = "Soul-RnB"

    count_genres(df, 1)

    df = delete_unkown(df)

    count_genres(df, 1)
    #count_genres(df, 5)
    count_genres(df, 100)
    df = delete_outlayers(df, 100)

    df.to_csv(file_name_out, index=False)
    print("csv file is ready")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    manage_genres()
