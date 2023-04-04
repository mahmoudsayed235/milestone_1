menuPrompt="\n Enter 'a' to add movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies=[]

def addMovie():
    title=input("Enter the movie title : ")
    director=input("Enter the movie director : ")
    year=input("Enter the movie release year : ")
    movies.append(
        {
            'title':title,
            'director':director,
            'year':year
        }
    )
def showMovies():
    for movie in movies:
        printMovie(movie)
def printMovie(movie):
    print(f"Title: {movie['title']}, Director: {movie['director']}, and Year: {movie['year']}, ")

def findMovie():
    searchTitle=input("Enter movie title you;re looking for: ")
    for  movie in movies:
        if movie['title']==searchTitle:
            printMovie(movie)
            break
    else:
        print(f"there is no movie with title {searchTitle}")

userOptions={
    "a":addMovie,
    "f":findMovie,
    "l":showMovies
}
def menu():
    selection=input(menuPrompt)
    while selection!="q":
        if selection in userOptions:
            selectionFun = userOptions[selection]
            selectionFun()

        else:
            print("you entered an invalid selection, please try again! ")
        selection=input(menuPrompt)

    """
        if selection=="a":
            addMovie()
        elif selection=="l":
            showMovies()
        elif selection=="f":
            findMovie()
        """



menu()