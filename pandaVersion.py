import pandas as pd
import numpy as np
import csv
#loading tables via pandas so data can be manipulated
movies = pd.read_csv(r'C:\archives\movie.csv',low_memory=False)
ratings = pd.read_csv(r'C:\archives\rating.csv',low_memory=False)
movie_data = pd.read_csv('C:/archives2/movies_metadata.csv',low_memory=False)
#users = pd.read_csv(r'C:\archives\user.csv')
#movie and ratings combined 
moviesAndRatings = pd.merge(movies, ratings)
#print(moviesAndRatings.head(5))
#gets the film the user watched


#get certain userID
userID = input("Whats your user ID")

#creates the matrix to find similarities between the movies
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vector = TfidfVectorizer(stop_words='english')

movie_data['overview'] = movie_data['overview'].fillna('')

tfidf_matrix = tfidf_vector.fit_transform(movie_data['overview'])
from sklearn.metrics.pairwise import linear_kernel

sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(movie_data.index, index=movie_data['title']).drop_duplicates()
indices[:10]


genreOfFilm = ""

#this is to see if the movie entered is in the table
def addFilmToUsers():
    genreOfFilm = ""
    filmNumber = -10
    filmThere = False
    filmWatched = input("Enter film watched")
    filmScore = input("Rate the film on a scale of 1 to 5")
    filmWatched.lower()
    for column in movies[['title','genres']]:
        specificColumn = movies[column]
        #print('Column Name : ', column)
   # print(specificColumn.values[1])
        #print(specificColumn.values)
        counter = 0
        for films in specificColumn:     
            filmsShort = films[:-7]
            if(filmsShort.lower() == filmWatched.lower()):
                filmNumber = counter
                with open(r'C:\archives\user.csv', 'a', newline='') as file:
                    write = csv.writer(file)
#for userId we need to set users first               
                    write.writerow([userID,films, filmScore]) 
                    filmThere = True
            if(filmNumber == counter):
                print(films)
                genreOfFilm = films
                
            counter += 1

    if(filmThere == False):
        print("film not in database")
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




firstTime = True
anotherFilm = 'y'
genreOfFilm, filmWatched = addFilmToUsers()
anotherFilm = input("Would you like to enter another film? 'y' or 'n'")
while(anotherFilm.lower() == 'y'):
    if(firstTime == True):
        firstTime=False
        genreOfFilm, filmWatched = addFilmToUsers()
    else:
        genreOfFilm, filmWatched = addFilmToUsers()
        anotherFilm = input("Would you like to enter another film? 'y' or 'n'")   

    
    #if(firstTime == False):
    #    anotherFilm = input("Would you like to enter another film? 'y' or 'n'")
    #firstTime = False
    #if(anotherFilm == 'y'):
    #    addFilmToUsers()


#finds all the purely one set of genres
groupedFilms = moviesAndRatings.loc[moviesAndRatings['genres']==genreOfFilm]
#creates new table which is the movie with their mean rating next to it
filmRating = groupedFilms.groupby('title').agg({'rating': [np.mean]})
#sorts the table so highest rating is at the top
sortedFilms = filmRating.sort_values([('rating', 'mean')],ascending = False)
#prints first 5 values
print(sortedFilms.head(5))
ratingList= []
for index, row in sortedFilms.head(5).iterrows():
    ratingList.append(index)

print(ratingList)

contentBasedReccomendation = content_based_recommender(filmWatched.title())
mlList = []
for i in range(5):
    mlList.append(contentBasedReccomendation.iat[i])
print(content_based_recommender(filmWatched.title()))
finished = input("Press Any key to finish")
