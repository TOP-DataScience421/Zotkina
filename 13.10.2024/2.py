from pandas import read_csv
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix

from pathlib import Path
from sys import path


movies_raw = read_csv(Path(path[0]) / 'movies.csv')
ratings_raw = read_csv(Path(path[0]) / 'ratings.csv')

ratings = ratings_raw.pivot(
    index='user_id',
    columns='movie_id',
    values='rating'
)

votes_user_for_movie = ratings_raw.groupby('movie_id').count()['user_id']
print(votes_user_for_movie.describe().round().loc['min':], end='\n\n')

votes_movie_for_user = ratings_raw.groupby('user_id').count()['movie_id']
print(votes_movie_for_user.describe().round().loc['min':], end='\n\n')

mask = votes_user_for_movie >= 10
ratings = ratings.loc[:, mask]

mask = votes_movie_for_user >= 50
ratings = ratings.loc[mask, :]

ratings.fillna(0, inplace=True)

ratings_csr = csr_matrix(ratings)

model = NearestNeighbors(
    n_neighbors=15,
    algorithm='brute',
    metric='cosine',
    n_jobs=-1
)
model.fit(ratings_csr)


user_id = 2
dist, idx = model.kneighbors(ratings_csr[user_id], 5)

mask = ratings.index.isin(idx.flat)
close_users = ratings.loc[mask, :]

mask = close_users.where(close_users > 0).count() > 1
print(close_users.loc[:, mask].T, end='\n\n')

