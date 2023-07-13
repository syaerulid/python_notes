Unique Users Per Client Per Month

Write a query that returns the number of unique users per client per month

DataFrame: fact_events
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
fact_events.head()

df = fact_events.copy()
df.head()

# groupby first
grup = df[['client_id','time_id','user_id']]

# extract time_id
grup['time_id'] = grup['time_id'].dt.strftime("%-m")
grup = grup.drop_duplicates()

grupby = grup.groupby(['client_id','time_id','user_id']).size().reset_index(name = 'count_user_id')
grupby = grupby[['client_id','time_id','count_user_id']]

# sum
grupby.groupby(['client_id','time_id']).size().reset_index(name = "user_id")

Penjelasan :
nanti
