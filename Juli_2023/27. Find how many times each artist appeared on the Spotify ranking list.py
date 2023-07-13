Find how many times each artist appeared on the Spotify ranking list

Find how many times each artist appeared on the Spotify ranking list
Output the artist name along with the corresponding number of occurrences.
Order records by the number of occurrences in descending order.

DataFrame: spotify_worldwide_daily_song_ranking
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking.head()

df = spotify_worldwide_daily_song_ranking.copy()
df.head()

# group by
df_g = df.groupby(['artist','position']).size().reset_index(name = 'count')
# sum
df_g = df_g.groupby(['artist']).agg({'count' : 'sum'}).reset_index()

# rename
df_g.rename(columns = {'count' : 'n_occurences'}, inplace = True)

# sort descending
df_g.sort_values('n_occurences', ascending = False)

Penjelasan :
nanti

