# output yang diharapkan pandas.Series

# Import your libraries
import pandas as pd
from datetime import datetime

# Start writing code
fb_searches.head()
df = fb_searches

# check column type
column_type = df['date'].dtype
print(column_type) # check column type

# change type of column date
df['date'] = pd.to_datetime(df['date'])

# extract format datetime
df['date'] = df['date'].dt.strftime("%Y-%m")
df.head()
# groupby
df_baru = df.groupby(['date','search_id','user_id']).size().reset_index(name = "count")
df_baru

# filtering condition
august_df = df_baru[df_baru['date'] == '2021-08']
august_df

# count search id >= 5 by user id
count_distinct = df[df['search_id'] >= 5].groupby('user_id').size().rename('occurrences')
print(count_distinct)
type(count_distinct)

Penjelasan :
  pd.to_datetime = mengubah format dari menjadi datetime sehingga bisa diekstrak menggunakan strftime
  strftime = fungsi dari library datetime untuk mengekstrak data tertentu (mirip extract pada SQL)
  groupby = menggrouping kolom tertentu
  df[df['search_id'] >= 5] <- conditional filter dimana search_id lebih dari 5
  .groupby('user_id') <- di grouping berdasarkan unique user id
  size() = untuk membuat output mejadi pandas.Series
  rename('occurences') = mengubah nama kolom agar tidak 0
