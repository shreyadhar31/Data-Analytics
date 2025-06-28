import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("netflix dataset.csv", engine='python')
df.shape

df.isna().sum()
df = df.dropna()
df.shape

df= df.drop_duplicates()

#1 Which movie has the highest popularity score?
df[df['Popularity'] == df['Popularity'].max()]

#2 Which movie has the highest vote average?
df['Vote_Average'] = pd.to_numeric(df['Vote_Average'], errors='coerce')
df[df['Vote_Average'] == df['Vote_Average'].max()]

#3 Which movie has the vote count greater than 1000?
df['Vote_Count'] = pd.to_numeric(df['Vote_Count'], errors='coerce')
df[df['Vote_Count'] > 1000]

#4 What is the average vote score across all movies?
df['Vote_Average'].mean()

#5 What is the total number of unique genres represented?
df['Genre'].nunique()

import matplotlib.pyplot as plt
genre_split = df['Genre'].str.split(', ')
genre_exploded = genre_split.explode()
genre_counts = genre_exploded.value_counts()
plt.figure(figsize=(12, 8))
genre_counts.plot.pie(autopct='%1.1f%%', colors = ['#1f77b4','#000080','#000080','#5DADE2', '#85C1E9', '#D6DBDF','#696969', '#AAB7B8', '#85929E', '#566573'])
plt.title('Distribution of Genres')
plt.ylabel('')
plt.tight_layout()
plt.show()

#6 How many movies are released in 2022?
df['Release_Date']=pd.to_datetime(df['Release_Date'], errors='coerce')
movies_2022=df[df['Release_Date'].dt.year == 2022].shape[0]
print(movies_2022)

#7 Which is the oldest movie in the dataset?
df[df['Release_Date'] == df['Release_Date'].min()]

#8 What is the average popularity of movies released after 2020?
movies_after_2020 = df[df['Release_Date'].dt.year > 2020]
movies_after_2020['Popularity'].mean()

#9 Group movies by year and what is the average vote per year?
df.groupby(df['Release_Date'].dt.year)['Vote_Average'].mean()

df['Release_Date']=pd.to_datetime(df['Release_Date'], errors='coerce')
df['Vote_Average'] = pd.to_numeric(df['Vote_Average'], errors='coerce')
plt.figure(figsize=(12, 8))
plt.plot(df.groupby(df['Release_Date'].dt.year)['Vote_Average'].mean(), marker= 'o', color= '#D3D3D3')
plt.xlabel('Year')
plt.ylabel('Average Vote')
plt.title('Average Vote per Year')
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()

#10 Which year has the most releases?
df['Release_Year'] = df['Release_Date'].dt.year
df['Release_Year'].value_counts().idxmax()

df['Release_Year'] = df['Release_Date'].dt.year
plt.hist(df['Release_Year'], bins=20, color='#6495ED', edgecolor='black')
plt.xlabel('Release Year')
plt.ylabel('Number of Movies')
plt.title('Distribution of Movies by Release Year')
plt.xticks(rotation=90)
plt.show()

#11 How many movies are in english?
df[df['Original_Language'] == 'en'].shape[0]

colors = ['#1f77b4','#000080','#000080','#5DADE2', '#85C1E9', '#D6DBDF','#696969', '#AAB7B8', '#85929E', '#566573']
df['Original_Language'].value_counts().plot.pie(
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'width': 0.4} , colors= colors
)
plt.title('Distribution of Movies by Language')
plt.ylabel('')
plt.tight_layout()
plt.show()

#12 Which language is the most common in dataset?
df['Original_Language'].value_counts().idxmax()

#13 List all the movies that belong to the 'Action' genre?
df[df['Genre'].str.contains('Action', case=False, na=False)]

#14 Which genre appears most frequently across movies?
genre_split = df['Genre'].str.split(', ')
genre_exploded = genre_split.explode()
genre_exploded.value_counts().idxmax()

#15 What is the average vote for movies in each genre?
df['Genre'] = df['Genre'].str.split(', ')
df = df.explode('Genre')
df.groupby('Genre')['Vote_Average'].mean()

genre_avg_votes = df.groupby('Genre')['Vote_Average'].mean().sort_values()
plt.scatter(genre_avg_votes.index, genre_avg_votes.values, color='dodgerblue')

plt.xticks(rotation=45, ha='right')
plt.xlabel('Genre')
plt.ylabel('Average Vote')
plt.title('Average Vote per Genre')
plt.grid(True)
plt.tight_layout()
plt.show()

#16 What are the top 5 movies by average vote?
top_5 = df.sort_values(by='Vote_Average', ascending=False).head(5).drop_duplicates()
print(top_5[['Title', 'Vote_Average']])

plt.barh(top_5['Title'], top_5['Vote_Average'], color= '#B0E0E6')
plt.ylabel('Movie Title')
plt.xlabel('Vote Average')
plt.title('Top 5 Movies by Vote Average')
plt.xticks(rotation=90)
plt.show()

#17 What are the top 5 movies by popularity?
top_5p = df.sort_values(by='Popularity', ascending=False).head(5).drop_duplicates()
print(top_5p[['Title', 'Popularity']])

plt.barh(top_5p['Title'], top_5p['Popularity'], color= '#C0C0C0')
plt.ylabel('Movie Title')
plt.xlabel('Popularity Score')
plt.title('Top 5 Movies by Popularity')
plt.xticks(rotation=90)
plt.show()

#18 What are the top 5 movies by vote count?
top_5v = df.sort_values(by='Vote_Count', ascending=False).head(5).drop_duplicates()
print(top_5v[['Title', 'Vote_Count']])

plt.barh(top_5v['Title'], top_5v['Vote_Count'], color= '#696969')
plt.ylabel('Movie Title')
plt.xlabel('Vote_Count')
plt.title('Top 5 Movies by Vote count')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#19 Movies with popularity>2000 and average vote.7.5
df['Popularity'] = pd.to_numeric(df['Popularity'], errors='coerce')
df['Vote_Average'] = pd.to_numeric(df['Vote_Average'], errors='coerce')
movies = df[(df['Popularity'] > 2000) & (df['Vote_Average'] > 7.5)]
print(movies[['Title', 'Popularity', 'Vote_Average']])

group1 = movies.iloc[0]   # navy
group2 = movies.iloc[1]   # dimgray
group3 = movies.iloc[2]   # lightgray

plt.scatter(group1['Popularity'], group1['Vote_Average'], color='#000080', label='Spider-Man: No Way Home')
plt.scatter(group2['Popularity'], group2['Vote_Average'], color='#696969', label='The Batman')
plt.scatter(group3['Popularity'], group3['Vote_Average'], color='#D3D3D3', label='Encanto')

plt.xlabel('Popularity')
plt.ylabel('Vote_Average')
plt.title('Movies with Popularity > 2000 and Vote_Average > 7.5')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

#20 Movies which have both 'Action' and 'Thriller' genre.
movies = df[df['Genre'].str.contains('Action') & df['Genre'].str.contains('Thriller')]
print(movies[['Title', 'Genre']])

#21 List movies with a vote average higher than the dataset's average.
avg_vote = df['Vote_Average'].mean()
movies = df[df['Vote_Average'] > avg_vote].drop_duplicates()
print(movies[['Title', 'Vote_Average']])

#22 List movies with vote count above median.
median_vote_count = df['Vote_Count'].median()
movies = df[df['Vote_Count'] > median_vote_count].drop_duplicates()
print(movies[['Title', 'Vote_Count']])

#23 What is the average popularity by original language?
df.groupby('Original_Language')['Popularity'].mean()

#24 scatter chart of popularity by genre.
popularity_by_genre = df.groupby('Genre')['Popularity'].mean().sort_values()
plt.scatter(popularity_by_genre.index, popularity_by_genre.values, color='#808080')

plt.xticks(rotation=45, ha='right')
plt.xlabel('Genre')
plt.ylabel('Popularity')
plt.title('Popularity per Genre')
plt.grid(True)
plt.tight_layout()
plt.show()

#25 donut chart of top 5 genres.
top5_genres = df['Genre'].value_counts().nlargest(5)
colors = ['#1f77b4', '#5DADE2', '#85C1E9', '#D6DBDF', '#AAB7B8']
plt.pie(
    top5_genres,
    labels=top5_genres.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    wedgeprops={'width': 0.4}  # Donut effect
)
plt.title('Top 5 Genres (Donut Chart)')
plt.tight_layout()
plt.show()

#26 heatmap
import seaborn as sns
numerical_df = df.select_dtypes(include=['number'])
sns.heatmap(numerical_df.corr(), annot=True, cmap='Greys')
plt.show()
