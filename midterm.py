"""
Midterm Practical Exam — Movie Collection Manager
Student: Diomes, Danny D.
"""

movies = [["Inception", "Christopher Nolan", "Watched"]]

x = movies.index("Watched")
print(x)

def display_menu():
    print("=== Movie Collection Manager ===")
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Count watched vs unwatched")
    print("4. Find a movie")
    print("5. Remove a movie")
    print("6. Exit")
    choice = int(input("Choose an option: "))
    return choice

def add_movie(movie_list):
    title = input("Enter movie title: ")
    director = input("Enter director: ")
    status = input("Enter status: ")
    added_movies = [[title, director, status]]
    movies.extend(added_movies)
    print("")
    print("Movie added successfully.")
    return print("")
def view_movies(movie_list):
    print("")
    print("=== All Movies ===")
    for movie in movies:
        print(movie)
        print("")

def count_watched_unwatched(movie_list):
    print("")
    for movie in movies:
        watched = movie.count("watched")
        return print(f"Watched: {watched}")
        unwatched = movie.count("unwatched")
        return print(f"Unwatched: {unwatched}")

def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass

def remove_movie(movie_list):
    remove = int (input ("Number: "))
    movies.pop(remove)
    print(movies)



def main():
    while True:
        choice = display_menu()
        if choice == 1:
            add_movie(movies)
        elif choice == 2:
            view_movies(movies)
        elif choice == 3:
            count_watched_unwatched(movies)
        elif choice == 4:
            find_movie(movies)
        elif choice == 5:
            remove_movie(movies)
        elif choice == 6:
            break
        else:
            print("Invalid Choice")


main()