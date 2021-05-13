import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import csv

# Loading tables via pandas so records can be manipulated
movies = pd.read_csv(r'data/movies.csv',low_memory=False)
ratings = pd.read_csv(r'data/ratings.csv',low_memory=False)
movie_data = pd.read_csv('data/movies_metadata.csv',low_memory=False)
# Movies and ratings combined 
moviesAndRatings = pd.merge(movies, ratings)

# Creates the matrix to find similarities between the movies
tfidf_vector = TfidfVectorizer(stop_words='english')
movie_data['overview'] = movie_data['overview'].fillna('')
tfidf_matrix = tfidf_vector.fit_transform(movie_data['overview'])
sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movie_data.index, index=movie_data['title']).drop_duplicates()

# Function to check if movie in dataset
def findMovie(film):
    counter = 0
    for movie in movies['title']:
        dateTrimmed = movie[:-7]
        if (dateTrimmed.lower() == film.lower()):
            genres = movies['genres'][counter]
            return(dateTrimmed, genres)
        counter += 1
    # Movie does not exist
    return(False, False)

# Function to find similar movies (Machine Learning)
def similarMovies(title, sim_scores = sim_matrix):
    try:
        idx = indices[title]
        sim_scores = list(enumerate(sim_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]
        results = movie_data['title'].iloc[movie_indices]
        mlList = []
        for i in range(5):
            mlList.append(results.iat[i])
        return mlList
    except:
        return []

def topMoviesForGenre(genres):
    # Finds all records matching one set of genres
    groupedFilms = moviesAndRatings.loc[moviesAndRatings['genres']==genres]
    # Creates new table containing the movie with their mean rating
    filmRating = groupedFilms.groupby('title').agg({'rating': [np.mean]})
    # Sorts the table
    sortedFilms = filmRating.sort_values([('rating', 'mean')],ascending = False)
    ratingList= []
    # Converts table to list of top movies
    for index, row in sortedFilms.head(5).iterrows():
        ratingList.append(index)
    return(ratingList)

# Master function
def recommendations(userMovie):
    title, genres = findMovie(userMovie)

    if (title and genres):
        topRated = topMoviesForGenre(genres)
        similar = similarMovies(title)
        return [topRated,similar]
    else:
        return False
