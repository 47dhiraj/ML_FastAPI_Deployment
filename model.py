import pandas as pd

# import requests



def ml_recommendation_model(movie: str, rating: int):

    # # loading the data to use correlation algorithm
    # movies = pd.read_csv('./data/movies.csv')
    # ratings = pd.read_csv('./data/ratings.csv')


    # # data manipulation & data cleaning
    # ratings = pd.merge(movies, ratings).drop(['genres','timestamp'], axis=1)
    # user_ratings = ratings.pivot_table(index=['userId'], columns=['title'], values='rating')
    # user_ratings = user_ratings.dropna(thresh=10, axis=1).fillna(0)
    # item_similarity_df = user_ratings.corr(method='pearson')


    ## To create .pkl file from Pandas Dataframe
    # item_similarity_df.to_pickle('item_similarity_df.pkl')



    # Directly Loading pre-created .pkl file/model for more efficient web-page loading
    item_similarity_df = pd.read_pickle('./data/item_similarity_df.pkl')


    # function to get similar movies
    def get_similar_movies(movie_name, user_rating):
        similar_score = item_similarity_df[movie_name] * (user_rating - 2.5)
        similar_score = similar_score.sort_values(ascending= False)
        return similar_score


    # function to check if the recommended movies is already seen or not ? 
    def check_seen(movie, seen_movie):
        if movie == seen_movie:
            return True
        else:
            return False


    # Empty Dataframe
    similar_movies = pd.DataFrame()    

    similar_movie_list = []


    try:
        
        # Getting similar movies
        similar_movies = similar_movies._append(get_similar_movies(movie, rating), ignore_index= True)

        all_recommend = similar_movies.sum().sort_values(ascending= False)



        # Logic to check & remove, if the recommended movies is already seen
        check_title = movie
        i = 0

        for recommended_movie, score in all_recommend.items():
            if not check_seen(recommended_movie, check_title):
                similar_movie_list.append(recommended_movie)
            else:
                pass

            i = i + 1
            if i >= 30:
                break


        # return the recommended/similar movies
        return similar_movie_list

    except:
        # return empty list
        return similar_movie_list
