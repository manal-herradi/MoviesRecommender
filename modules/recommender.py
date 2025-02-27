import pandas as pd
import numpy as np
from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate, train_test_split

# Load dataset
ratings = pd.read_csv("data/ratings.csv")
movies = pd.read_csv("data/movies.csv")

# Prepare data for Surprise library
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
trainset, testset = train_test_split(data, test_size=0.2)

# Train model
model = SVD()
model.fit(trainset)

# Function to get recommendations
def get_recommendations(user_id, num_recommendations=5):
    movie_ids = ratings['movieId'].unique()
    user_ratings = {iid: model.predict(user_id, iid).est for iid in movie_ids}
    recommended_movies = sorted(user_ratings.items(), key=lambda x: x[1], reverse=True)[:num_recommendations]
    
    return movies[movies["movieId"].isin([x[0] for x in recommended_movies])][['title']]