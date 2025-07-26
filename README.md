# 🎧 Spotify Music Dataset Analysis

A data exploration and visualization project using the Spotify Tracks dataset. This project aims to understand musical trends, artist patterns, and track popularity using data-driven techniques in Python.

## 📌 Overview

This project includes:
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Visualizations of track features (danceability, energy, tempo, etc.)
- Correlation analysis and insights
- (Optional) Predictive modeling on track popularity

## 📂 Dataset

- **Records**: ~160,000 tracks
- **Columns**:
  - `track_name`, `artist_name`, `release_date`
  - `popularity`, `danceability`, `energy`, `tempo`, `acousticness`, `valence`, `instrumentalness`, `liveness`, `speechiness`, `duration_ms`

## ⚙️ Tech Stack

- Python 3.x
- VSCODE
- `pandas`, `numpy`, `matplotlib`, `seaborn`


## 🧹 Data Cleaning

- Removed duplicates
- Filtered out nulls and outliers
- Converted `release_date` to datetime format
- Handled popularity scale normalization (0–100)

## 📊 Exploratory Data Analysis

- 🎼 Top artists by track count
- 🔥 Tracks with highest popularity
- 🎚️ Distribution of features like tempo, energy, and valence
- 📈 Correlation heatmap between all features

## 📈 Predictive Modeling *(Optional)*

- Built a Linear Regression model to predict track popularity based on audio features
- Evaluated with RMSE and R² score

## 📌 Key Insights

- Higher danceability and energy correlate with more popular tracks
- Instrumental and acoustic tracks tend to be less popular
- Track durations have decreased over the years
