# Netflix Recommendation Engine

A Netflix-style movie recommendation system built using Python, Pandas, and the MovieLens dataset. This project demonstrates how collaborative filtering techniques can be used to recommend movies based on user behavior and rating patterns.

---

## Project Overview

Streaming platforms such as Netflix, Hulu, Disney+, and Amazon Prime rely heavily on recommendation systems to improve user engagement and content discovery.

This project simulates a recommendation engine by:

* Processing over 100,000 movie ratings
* Analyzing user behavior and movie popularity
* Building a user-movie interaction matrix
* Identifying similar movies using collaborative filtering
* Generating personalized movie recommendations

---

## Dataset

MovieLens Latest Small Dataset

* 100,836 Ratings
* 9,742 Movies
* 610 Users

Source: https://grouplens.org/datasets/movielens/

---

## Technologies Used

* Python
* Pandas
* NumPy
* Jupyter Notebook
* Git
* GitHub

---

## Project Workflow

### 1. Data Collection

Loaded movie metadata and user ratings from the MovieLens dataset.

### 2. Data Preparation

Merged movie and rating datasets to create a unified analysis table.

### 3. Exploratory Data Analysis

Analyzed movie popularity, rating distributions, and user engagement patterns.

### 4. User-Movie Matrix Construction

Built a matrix containing:

* 610 users
* 9,719 movies

This matrix serves as the foundation for recommendation generation.

### 5. Collaborative Filtering

Calculated movie similarity using user rating correlations.

Example:

Movies similar to **Toy Story (1995)** include:

* The Incredibles
* Finding Nemo
* Aladdin
* Monsters, Inc.
* Mrs. Doubtfire

---

## Key Results

| Metric            | Value       |
| ----------------- | ----------- |
| Movies            | 9,742       |
| Ratings           | 100,836     |
| Users             | 610         |
| User-Movie Matrix | 610 x 9,719 |

---

## Business Value

Recommendation engines help organizations:

* Increase user engagement
* Improve customer retention
* Personalize user experiences
* Drive content discovery
* Increase platform watch time

Companies such as Netflix, Amazon, Spotify, YouTube, and Disney+ rely heavily on recommendation systems to enhance customer experiences.

---

## Future Enhancements

Planned improvements include:

* User-based Collaborative Filtering
* Item-based Collaborative Filtering
* Matrix Factorization
* Content-Based Recommendations
* Hybrid Recommendation Systems
* Deployment as a Web Application

---

## Author

Jeremie Merchant

MS Data Science

LinkedIn:
[www.linkedin.com/in/jeremie-merchant](http://www.linkedin.com/in/jeremie-merchant)

GitHub:
github.com/jmerch81
