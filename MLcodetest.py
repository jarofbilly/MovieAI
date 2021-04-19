import pandas as pd
#load the data
movie_data = pd.read_csv('C:/Users/edwar/OneDrive/Desktop/movies_metadata.csv',low_memory=False)
movie_data.head()
print('Hello')
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vector = TfidfVectorizer(stop_words='english')
movie_data['overview'] = movie_data['overview'].fillna('')
tfidf_matrix = tfidf_vector.fit_transform(movie_data['overview'])
from sklearn.metrics.pairwise import linear_kernel
sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movie_data.index, index=movie_data['title']).drop_duplicates()
indices[:10]
def content_based_recommender(title, sim_scores = sim_matrix):
    idx = indices[title]
    sim_scores = list(enumerate(sim_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return movie_data['title'].iloc[movie_indices]
    print(movie_data['title'].iloc[movie_indices])
    content_based_recommender('Toy Story')
