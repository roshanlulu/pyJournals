# List of movies dictionaries:
import numpy as np
from operator import itemgetter
movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


# 2.1 Function definition to filter data by IMDB score
def check_score(movie):
    return (True if movie["imdb"] > 5.5 else False)


print(check_score(movies[0]))


# 2.2 Function definition to check average score of a given category
def check_avgscore(movies, category):
    imdb_scores = [movie["imdb"] for movie in movies]
    imdb_avg = np.mean(imdb_scores)
    imdb_categoryscores = [movie['imdb']
                           for movie in movies if movie['category'] == category]
    imdb_categoryavg = np.mean(imdb_categoryscores)
    return (True if imdb_avg > imdb_categoryavg else False)


print(check_avgscore(movies, 'Suspense'))


# 3.1 Function to create subsets based on the movie score
def better_score(movies, score):
    better_movies = []
    better_movies.append([m for m in movies if m['imdb'] > score])
    return(better_movies)


print(better_score(movies, 9))

# 3.2 Function to sort the movies list based on different parameters


def sort_movies(movies):
    sortbycategory = sorted(movies, key=itemgetter('category', 'imdb'))
    print(sortbycategory)

sort_movies(movies)