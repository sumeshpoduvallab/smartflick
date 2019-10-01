import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, maxResults=10, movieUserLikes="Avatar"):
        self.__index = None
        self.__features = ['keywords','cast','genres','director']
        self.__movieUserLikes = movieUserLikes
        self.__maxResults = maxResults

    def process(self):
        # Read CSV File
        df = pd.read_csv("resources/data/movie_dataset.csv")

        # Create a column in DF which combines all selected features
        for feature in self.__features:
            df[feature] = df[feature].fillna('')

        def combine_features(row):
            try:
                return row['keywords'] + " " + row['cast'] + " " + row["genres"] + " " + row["director"]
            except:
                print("Error:", row)

        df["combined_features"] = df.apply(combine_features,axis=1)

        # Create count matrix from this new combined column
        cv = CountVectorizer()

        count_matrix = cv.fit_transform(df["combined_features"])

        cosine_sim = cosine_similarity(count_matrix)

        # Get index of this movie from its title
        def get_index_from_title(title):
            return df[df.title == title]["index"].values[0]

        movie_index = get_index_from_title(self.__movieUserLikes)

        similar_movies =  list(enumerate(cosine_sim[movie_index]))

        # Get a list of similar movies in descending order of similarity score
        sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)
        # Print titles of top movies
        def get_title_from_index(index):
            return df[df.index == index]["title"].values[0]

        i=0
        for element in sorted_similar_movies:
            print(get_title_from_index(element[0]))
            i=i+1
            if i > self.__maxResults:
                break


