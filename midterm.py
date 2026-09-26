"""
Midterm Practical Exam — Movie Collection Manager
Student: Diomes, Danny D.
"""

global movies = [["Inception", "Christopher Nolan", "Watched"]]
for movie in movies:
        print(movie[0])

def display_menu():
    print("=== Movie Collection Manager ===")
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Count watched vs unwatched")
    print("4. Find a movie")
    print("5. Remove a movie")
    print("6. Exit")
    choice = int(input ("Choose an option: "))
        

def add_movie(movie_list):
    print("Hi")
    name = input("Movie name: ")
    added_movies = [name]
    movies.extend(added_movies)
    print(movies)

def view_movies(movie_list):
    # for movie in movies:
    #     print(movie)
    pass


def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass

def remove_movie(movie_list):
    choice = int (input ("Number: "))
    movies.pop(choice)
    print(movies)
    pass



def main():
    # create the main menu loop
    # call the appropriate function based on the user's choice
    pass


main()
# while True:
#     display_menu()
#     if display_menu(choice) == 1:
#         add_movie(movie_list)
#     elif display_menu(choice) == 2:
#         pass
#     elif display_menu(choice) == 3:
#         pass
#     elif display_menu(choice) == 4:
#         pass
#     elif display_menu(choice) == 5:
#         pass
#     elif display_menu(choice) == 6:
#         pass
#     else:
#         print("Invalid Choice")

