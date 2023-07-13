Find the top 10 ranked songs in 2010

What were the top 10 ranked songs in 2010?
Output the rank, group name, and song name but do not show the same song twice.
Sort the result based on the year_rank in ascending order.

DataFrame: billboard_top_100_year_end
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
billboard_top_100_year_end.head()

df = billboard_top_100_year_end.copy()
df.head()

# filter condition
dua_sepuluh = df[df['year'] == 2010]

# grupby
dua_x = dua_sepuluh[['year','year_rank','group_name','song_name']]
dua_y = dua_x.drop_duplicates()

# selected column
dua_y[['year_rank','group_name','song_name']].head(10)

Penjelasan nanti :

