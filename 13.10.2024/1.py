import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Чтение данных
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Объединить таблицы по movie_id
ratings_movies = pd.merge(ratings, movies, on='movie_id')

# Сгруппировать по полю user_id , чтобы найти любимый жанр
favorite_genres = ratings_movies.groupby('user_id')['genres'].apply(lambda x: x.value_counts().index[0])

# Создать датафрейм с полем user_id и любимым жанром
fav_genres_df = pd.DataFrame({'user_id': favorite_genres.index, 'favorite_genre': favorite_genres.values})
genre_ratings = ratings_movies.pivot_table(index='user_id', columns='genres', values='rating', fill_value=0)
result_df = pd.concat([fav_genres_df, genre_ratings], axis=1)
# Печатать результат
threshold = 3
na_count = result_df.isna().sum(axis=1)
filtered_df = result_df[na_count <= threshold]
print(fav_genres_df)
