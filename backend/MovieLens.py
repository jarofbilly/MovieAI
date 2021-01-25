import pandas as pd
import numpy as np
import os
from time import sleep

#movie and ratings combined
print("Dataset loading...")
#total = pd.read_pickle(os.path.abspath('data/combined.pkl'))
movies = pd.read_csv(os.path.abspath('data/movies.csv'))
print("Dataset loaded!")

def search(name):
    result = movies[movies['title'].str.contains(name)]
    output = result['title'].values.tolist()
    print(output)
    

def topAction():
    films = total.loc[total['action']==1]
    filmsRating = films.groupby('title', as_index=False)['rating'].mean()
    sortedFilms = filmsRating.sort_values('rating',ascending = False)
    output = sortedFilms.head(10)[['title']]
