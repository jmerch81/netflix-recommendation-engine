import pandas as pd


def get_recommendations(
    movie_title,
    user_movie_matrix,
    movie_stats,
    min_rating_count=100,
    num_recommendations=10
):
    """
    Generate movie recommendations based on user rating correlations.

    Parameters:
        movie_title (str): Movie title to base recommendations on.
        user_movie_matrix (DataFrame): Matrix of users and movie ratings.
        movie_stats (DataFrame): Movie statistics including rating_count.
        min_rating_count (int): Minimum number of ratings required.
        num_recommendations (int): Number of recommendations to return.

    Returns:
        DataFrame: Top recommended movies sorted by correlation.
    """

    movie_user_ratings = user_movie_matrix[movie_title]

    similar_movies = user_movie_matrix.corrwith(movie_user_ratings)

    recommendations = pd.DataFrame(
        similar_movies,
        columns=["Correlation"]
    )

    recommendations.dropna(inplace=True)

    recommendations = recommendations.join(
        movie_stats["rating_count"]
    )

    recommendations = recommendations[
        recommendations["rating_count"] >= min_rating_count
    ].sort_values(
        by="Correlation",
        ascending=False
    )

    return recommendations.head(num_recommendations)