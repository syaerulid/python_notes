Count the number of movies that Abigail Breslin nominated for oscar

Count the number of movies that Abigail Breslin was nominated for an oscar.

DataFrame: oscar_nominees

# Import your libraries
import pandas as pd

# Start writing code
oscar_nominees.head()

df = oscar_nominees.copy()
df.head()

# filter condition
df_f = df[df['nominee'] == 'Abigail Breslin']
df_f.groupby(['movie']).size().sum()

Penjelasan nanti :
