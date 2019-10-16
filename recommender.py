import pandas as pd
from tabulate import tabulate

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

    def printDataSet(self):
        dataFrame = pd.DataFrame(self.__dataFrame, columns=['title','genres','director','vote_average'])
        totalRows = dataFrame.shape[0]
        startPos = 1
        endPos = startPos + 100

        while True:
            # Print movie list along with features
            paginatedDataFrame = dataFrame[startPos:endPos]
            print(tabulate(paginatedDataFrame, headers='keys', tablefmt='psql'))

            if endPos == totalRows:
                break
            print("")
            print("")
            print("---------------------------------------------------------------------------")
            next = input("Next (y|n): ")
            print("---------------------------------------------------------------------------")
            next = str(next).lower()
            if next == "y":
                startPos = startPos + 100
                endPos = startPos + 100

                if totalRows < endPos:
                    endPos = totalRows
                continue
            elif next == "n":
                break
            else:
                print("Invalid option: Please try again and enter a valid option")
                continue

    def search(self, movieUserLikes="Avatar"):
        movieIndex = self.getTitleIndex(movieUserLikes)
        similarMovies = list(enumerate(self.__similarity[movieIndex]))

        # Get a list of similar movies in descending order of similarity score
        sortedSimilarMoviesIndex = sorted(similarMovies,key=lambda x:x[1],reverse=True)

        # Add recommended movies to a data frame
        movie_list = []
        i=0
        for movieIndex in sortedSimilarMoviesIndex:
            # Skip the first movie, since it will be the movie user liked recently
            if i==0:
                i=i+1
                continue
            movie_dict = {}
            movie_dict['Movie'] = self.getData('title', movieIndex[0])
            movie_dict['Genres'] = self.getData('genres', movieIndex[0])
            movie_dict['Director'] = self.getData('director', movieIndex[0])
            movie_dict['Vote'] = self.getData('vote_average', movieIndex[0])

            movie_list.append(movie_dict)
            i=i+1
            if i > (self.__maxResults + 1):
                break

        result_dataframe = pd.DataFrame(movie_list, columns=['Movie','Genres','Director','Vote'])
        return result_dataframe
