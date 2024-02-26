import pandas as pd

import requests
import subprocess



def ml_pipeline(movie: str, rating: int):

    # loading the data
    movies = pd.read_csv('./data/movies.csv')
    ratings = pd.read_csv('./data/ratings.csv')

    # data manipulation & data cleaning
    ratings = pd.merge(movies, ratings).drop(['genres','timestamp'], axis=1)
    user_ratings = ratings.pivot_table(index=['userId'], columns=['title'], values='rating')
    user_ratings = user_ratings.dropna(thresh=10, axis=1).fillna(0)
    item_similarity_df = user_ratings.corr(method='pearson')


    # function to get similar movies
    def get_similar_movies(movie_name,user_rating):
        similar_score = item_similarity_df[movie_name]*(user_rating-2.5)
        similar_score = similar_score.sort_values(ascending=False)
        return similar_score


    # function to check if the recommended movies is already seen or not ? 
    def check_seen(movie, seen_movies):
        for item in seen_movies:
            if item == movie:
                return True
        return False


    # Empty Dataframe
    similar_movies = pd.DataFrame()    

    # Getting similar movies
    similar_movies = similar_movies._append(get_similar_movies(movie,rating), ignore_index=True)

    all_recommend = similar_movies.sum().sort_values(ascending=False)

    # return the recommended movies
    return all_recommend
