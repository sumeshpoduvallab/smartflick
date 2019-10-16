import pandas as pd
from tabulate import tabulate
from recommender import Recommender


def movieLikedInput():
        while True:
            try:
                print("")
                print("")
                print("---------------------------------------------------------------------------")
                movieLiked = input("Enter a movie you liked recently (El Mariachi): ")
                print("---------------------------------------------------------------------------")
                movieLiked = str(movieLiked).title()

                break
            except Exception as e:
                print("Exception occurred: Please try again and enter a valid movie")
                print("Error: " + e.__str__())
                print("")
                continue

        return movieLiked

def operationInput():
        while True:
            try:
                print("")
                print("")
                print("---------------------------------------------------------------------------")
                print("Options")
                print("---------------------------------------------------------------------------")
                print("0 : Exit")
                print("1 : Recommend Movie")
                print("2 : Browse All Movies")
                print("---------------------------------------------------------------------------")
                operation = input("Enter operation (1): ")
                print("---------------------------------------------------------------------------")

                operation = int(operation)

                if operation < 0 or operation > 2:
                    print("Invalid Operation: Please try again and enter a valid operation")
                    print("")
                    continue
                break
            except Exception as e:
                print("Exception occurred: Please try again and enter a valid movie")
                print("Error: " + e.__str__())
                print("")
                continue

        return operation

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
    except Exception as e:
        print("Error: " + e.__str__())
        print("SmartFlick shutting down...")
        print("---------------------------------------------------------------------------")
        print("                  Good Bye!                ")
        print("---------------------------------------------------------------------------")

    while True:
        try:
            operation = operationInput()
            if operation == 0:
                break
            if operation == 1:
                movieLiked = movieLikedInput()
                searchResult = engine.search(movieLiked)
                printResult(searchResult)
                continue
            if operation == 2:
                engine.printDataSet()
                continue

        except Exception as e:
            print("Error: " + e.__str__())
            print("SmartFlick shutting down...")
            print("---------------------------------------------------------------------------")
            print("                  Good Bye!                ")
            print("---------------------------------------------------------------------------")

    print("SmartFlick shutting down...")
    print("---------------------------------------------------------------------------")
    print("                  Good Bye!                ")
    print("---------------------------------------------------------------------------")


main()
