from pyspark import *
from pyspark.sql import SparkSession
import numpy as np
from pyspark.sql.functions import desc
import csv
import pandas as pd

#creates the spark session
spark = SparkSession \
    .builder \
    .master("local[*]")\
    .appName("MovieAI") \
    .getOrCreate()


#reads the files and prints the first 5 values of each
movies = spark.read.option("header", "true").csv(r'C:\archives\movie.csv')
ratings = spark.read.option("header", "true").csv(r'C:\archives\rating.csv')
#merges the two
moviesAndRatings = movies.join(other = ratings, on=(movies['movieId']==ratings['movieId']))
#for machine learning
movie_data = pd.read_csv('C:/archives2/movies_metadata.csv',low_memory=False)

#get certain userID
userID = input("Whats your user ID")

#creates the matrix to find similarities between the movies
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vector = TfidfVectorizer(stop_words='english')
#i dont have overview
movie_data['overview'] = movie_data['overview'].fillna('')

tfidf_matrix = tfidf_vector.fit_transform(movie_data['overview'])
from sklearn.metrics.pairwise import linear_kernel

sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(movie_data.index, index=movie_data['title']).drop_duplicates()
indices[:10]



def addFilmToUsers():
    filmThere = False
    filmWatched = input("Enter film watched")
    filmScore = input("Rate the film on a scale of 1 to 5")
#checks if film is in database and adds it to a table on its own
    filmFound = movies.filter(movies.title == filmWatched)
    filmFound.show()
#checks if the database is empty so to tell if the film was in the database
    if(len(filmFound.head(1))==0):
        print("film not found in database")
    else:
    #gets information of film
        genreOfFilm = filmFound.collect()[0]["genres"]
        nameOfFilm = filmFound.collect()[0]["title"]
        #writes the data to the users csv
        with open(r'C:\archives\user.csv', 'a', newline='') as file:
            write = csv.writer(file)            
            write.writerow([userID,nameOfFilm, filmScore]) 

        return genreOfFilm, filmWatched
    

def content_based_recommender(title, sim_scores = sim_matrix):

    idx = indices[title]

    sim_scores = list(enumerate(sim_matrix[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:11]

    movie_indices = [i[0] for i in sim_scores]
    results = movie_data['title'].iloc[movie_indices]
    #sortedOrder = results.sort_values(['sim_scores'], ascending = False)
    # sortedOrder
    return movie_data['title'].iloc[movie_indices]


#gets the genre of a film entered
genre, filmWatched = addFilmToUsers()
anotherFilm="y"
while(anotherFilm.lower() != "n"):
    anotherFilm = input("Would you like to add another film? Y/N")
    if(anotherFilm.lower() == "y"):
        genre = addFilmToUsers()
    else:
    #filters so only comedy films
        Films = moviesAndRatings.filter(moviesAndRatings["genres"] == genre)
#comedyFilms.show(5)
#gets the mean value
        Rating = Films.groupby('title').agg({"rating": "mean"})
#comedyRating.show(5)
#orders the data by ratings
        sortedRating = Rating.sort(desc("avg(rating)"))
        print("Here are some other reccomendations based off of last film watched")
        sortedRating.show(5)
        print(content_based_recommender(filmWatched[:-7]))
        finished = input("Press Any key to finish")





    
 
