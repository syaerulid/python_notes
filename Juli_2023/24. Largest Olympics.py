Largest Olympics

Find the Olympics with the highest number of athletes. The Olympics game is a combination of the year and the season, and is found in the 'games' column. Output the Olympics along with the corresponding number of athletes.

DataFrame: olympics_athletes_events
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
olympics_athletes_events.head()

# df
df = olympics_athletes_events.copy()
df.head()
df.drop_duplicates()

# group by
grup = df.groupby(['games','name']).size().reset_index(name = "count")
# replace so all is unique
grup['count'] = grup['count'].replace([2,3], [1,1])

# count athletes
grup = grup.groupby(['games'])['count'].sum().reset_index()
grup = grup.drop_duplicates()

grup.sort_values('count', ascending = False).head(1)
