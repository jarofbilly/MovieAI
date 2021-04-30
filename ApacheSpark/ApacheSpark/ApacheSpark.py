from pyspark import *
from pyspark.sql import SparkSession
import numpy as np
from pyspark.sql.functions import desc
import csv

#creates the spark session
spark = SparkSession \
    .builder \
    .master("local[*]")\
    .appName("MovieAI") \
    .getOrCreate()


#reads the files and prints the first 5 values of each
movies = spark.read.option("header", "true").csv(r'C:\archives\movie.csv')
ratings = spark.read.option("header", "true").csv(r'C:\archives\rating.csv')
moviesAndRatings = movies.join(other = ratings, on=(movies['movieId']==ratings['movieId']))

#get certain userID
userID = input("Whats your user ID")


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
        with open(r'C:\archives\user.csv', 'a', newline='') as file:
            write = csv.writer(file)            
            write.writerow([userID,nameOfFilm, filmScore]) 

        return genreOfFilm
    
#gets the genre of a film entered
genre = addFilmToUsers()
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
        
    


