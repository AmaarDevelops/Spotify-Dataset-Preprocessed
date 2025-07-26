import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('SpotifyFeatures.csv',encoding='latin1')

df.rename(columns={
    "ï»¿genre" : "genre",
},inplace=True)

df.fillna('UNDEFINED',inplace=True)
print(df.head())


total_missing_values = df.isnull().sum()
duplicates = df.duplicated().sum()

descripton_of_dataset = df.describe()

numerical_cols_df = df.select_dtypes(include=np.number)

numercials_cols_list = numerical_cols_df.columns.to_list()

numerical_columns = df[numercials_cols_list]

correlation = numerical_columns.corr()

population_correlation = correlation['popularity'].sort_values(ascending=False)

top_10_most_common_genres = df['genre'].value_counts(ascending=False).head(10)

avg_popularity_per_genre = df.groupby('genre')['popularity'].mean()
avg_danceability_per_genre = df.groupby('genre')['danceability'].mean()
avg_energy_per_genre = df.groupby('genre')['energy'].mean()

df = df[(df['duration_ms'] < 600000) & (df['loudness'] > - 60)]

df['song_length'] = df['duration_ms'] / 6000

df['popularity_category'] = pd.qcut(df['popularity'],
                                    q=3,
                                    labels = ['Low','Medium','High'],
                                    duplicates='drop')

condition = (df['danceability'] > 0.7) & (df['energy'] > 0.6)
df['Dance Hit'] = np.where(condition,'Yes','No')




print('Total missing values:-',total_missing_values)
print('Duplicates:-',duplicates)
print('Description of dataset:-',descripton_of_dataset)
print('Numerical columns df:-',numerical_cols_df)
print("Top 10 most common genres",top_10_most_common_genres)
print('Average popularity per genre:-',avg_popularity_per_genre)
print('Average danceability per genre:-',avg_danceability_per_genre)
print('Average energy per genre:-',avg_energy_per_genre)
print("\nOriginal Popularity vs. Category:")
print(df[['popularity', 'popularity_category']].head(10))

print("\n\nFINAL",df.head())

df.to_csv('Cleaned Spotify Dataset.csv',index=False)

#Visualizaton
plt.figure()
sns.histplot(data=df,x='energy',palette='muted')
plt.title('Enegry column histogram')
plt.savefig('Energy histogram.png')


plt.figure()
sns.histplot(data=df,x='duration_ms',palette='deep')
plt.title('duraction_ms histplot')

plt.figure()
sns.histplot(data=df,x='loudness')
plt.title('Loudness histogram')

plt.figure()
sns.heatmap(correlation,annot=True)
plt.title('Numerical columns correlation')
plt.savefig('screenshots/Numerical columns correlation.png')

plt.figure()
sns.heatmap(population_correlation.to_frame(),annot=True)
plt.title('Correlation with population')


plt.figure()
sns.barplot(x=avg_popularity_per_genre.values,y=avg_popularity_per_genre.index,palette='deep')
plt.title('Average popularity per genre')
plt.savefig('screenshots/average popularity with genre.png')

plt.figure()
sns.barplot(x=avg_danceability_per_genre.values,y=avg_danceability_per_genre.index,palette='muted')
plt.title('Average danceability per genre')


plt.figure()
sns.barplot(x=avg_energy_per_genre.values,y=avg_energy_per_genre.index,palette='rainbow')
plt.title('Average energy per genre')
plt.savefig('screenshots/average energy per genre.png')

plt.figure()
sns.scatterplot(x='energy',y='danceability',hue='Dance Hit',data=df,palette='Set2')
plt.title('Energy vs danceability')

plt.figure()
sns.countplot(data=df,x='popularity_category',palette='cool')
plt.title('Distribution of popularity categories')
plt.savefig('screenshots/distribution of popularity')

plt.show()