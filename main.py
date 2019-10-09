import pandas as pd
from tabulate import tabulate
from recommender import Recommender


def movieLikedInput():
        while True:
            try:
                print("")
                print("")
                print("---------------------------------------------------------------------------")
                movieLiked = input("Enter a movie you liked (Avatar): ")
                print("---------------------------------------------------------------------------")
                movieLiked = str(movieLiked).title()

                return movieLiked
            except Exception as e:
                print("Exception occurred: Please try again and enter a valid movie")
                print("Error: " + e.__str__())
                print("")
                continue

        return movieLiked


def printResult(movies):
    print(tabulate(movies, headers='keys', tablefmt='psql'))


def main():
    try:
        print("---------------------------------------------------------------------------")
        print("                  SMARTFLICK                                               ")
        print("---------------------------------------------------------------------------")
        print("")

        print("SmartFlick is tuning. Wait for few moment.")
        engine = Recommender(10)
        engine.prepareData()
        engine.mergeFeatures()
        engine.measureSimilarity()

        movieLiked = movieLikedInput()

        searchResult = engine.search(movieLiked)
        printResult(searchResult)

    except Exception as e:
        print("Error: " + e.__str__())
        print("SmartFlick shutting down...")
        print("---------------------------------------------------------------------------")
        print("                  Good Bye!                ")
        print("---------------------------------------------------------------------------")


main()
