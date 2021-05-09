import pandas as pd
import numpy as np

#change path as appropriate
movie_data = pd.read_csv('C:/Users/Dominic/Downloads/archive/movies_metadata.csv',low_memory=False)
movie_data['overview'] = movie_data['overview'].fillna('')
file = open("lk","rb")
#opens the file the sorted database is saved as
#Can save the array with file = open("fileName","wb") then np.save(file)
#loads the sorted database so it doesn't have to be recalculated every time
sim_matrix = np.load(file)
file.close
indices = pd.Series(movie_data.index, index=movie_data['title']).drop_duplicates()
indices[:10]

def content_based_recommender(title, sim_scores = sim_matrix):

    idx = indices[title]

    sim_scores = list(enumerate(sim_matrix[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:11]

    movie_indices = [i[0] for i in sim_scores]
    results = movie_data['title'].iloc[movie_indices]
    #sortedOrder = results.sort_values(['sim_scores'], ascending = False)
    # sortedOrder
    return results

x = content_based_recommender("Toy Story")
print(x.iat[0])
print(x.iat[1])
