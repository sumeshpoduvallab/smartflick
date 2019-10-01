from recommender import Recommender


def movieLikedInput():
        while True:
            try:
                print("")
                print("")
                print("---------------------------------------------------------------------------")
                movieLiked = input("Enter a movie you liked (Avatar): ")
                print("---------------------------------------------------------------------------")
                movieLiked = str(movieLiked).capitalize()

                return movieLiked
            except Exception:
                print("Exception occurred: Please try again and enter a valid movie")
                print("")
                continue

        return movieLiked


def main():
    try:
        print("---------------------------------------------------------------------------")
        print("                  SMARTFLICK                                               ")
        print("---------------------------------------------------------------------------")
        print("")
        movieLiked = movieLikedInput()

        print("SmartFlick is tuning. Wait for few moment.")
        engine = Recommender(10, movieLiked)
        engine.process()

    except Exception as e:
        print("Error: " + e.__str__())
        print("SmartFlick shutting down...")
        print("---------------------------------------------------------------------------")
        print("                  Good Bye!                ")
        print("---------------------------------------------------------------------------")


main()
