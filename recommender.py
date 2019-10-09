import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Recommender:

    COMBINE_FEATURE_COLUMN_NAME="combined_feature"

    def __init__(self, maxResults=10):
        self.__features = ['keywords','cast','genres','director']
        self.__maxResults = maxResults

        self.__dataFrame = None
        self.__countMatrix = None
        self.__similarity = None

    def prepareData(self):
        # Read CSV File
        self.__dataFrame = pd.read_csv("resources/data/movie_dataset.csv")

        for feature in self.__features:
            self.__dataFrame[feature] = self.__dataFrame[feature].fillna('')

    def mergeFeatures(self):
        # Create a column in DF which combines all selected features
        def combine_features(row):
            try:
                return row['keywords'] + " " + row['cast'] + " " + row["genres"] + " " + row["director"]
            except:
                print("Error:", row)

        self.__dataFrame[self.COMBINE_FEATURE_COLUMN_NAME] = self.__dataFrame.apply(combine_features,axis=1)

        # Create count matrix from this newly combined column
        cv = CountVectorizer()
        self.__countMatrix = cv.fit_transform(self.__dataFrame[self.COMBINE_FEATURE_COLUMN_NAME])

    def measureSimilarity(self):
        self.__similarity = cosine_similarity(self.__countMatrix)

    def getTitleIndex(self, title):
        # Get index of this movie from its title
        return self.__dataFrame[self.__dataFrame.title == title]["index"].values[0]

    def getData(self, columnName, index):
        return self.__dataFrame[self.__dataFrame.index == index][columnName].values[0]

    def search(self, movieUserLikes="Avatar"):
        movieIndex = self.getTitleIndex(movieUserLikes)
        similarMovies = list(enumerate(self.__similarity[movieIndex]))

        # Get a list of similar movies in descending order of similarity score
        sortedSimilarMoviesIndex = sorted(similarMovies,key=lambda x:x[1],reverse=True)

        movie_list = []
        i=0
        for movieIndex in sortedSimilarMoviesIndex:
            movie_dict = {}
            movie_dict['Movie'] = self.getData('title', movieIndex[0])
            movie_dict['Genres'] = self.getData('genres', movieIndex[0])
            movie_dict['Director'] = self.getData('director', movieIndex[0])
            movie_dict['Popularity'] = self.getData('popularity', movieIndex[0])

            movie_list.append(movie_dict)
            i=i+1
            if i > self.__maxResults:
                break

        result_dataframe = pd.DataFrame(movie_list, columns=['Movie','Genres','Director','Popularity'])
        return result_dataframe
