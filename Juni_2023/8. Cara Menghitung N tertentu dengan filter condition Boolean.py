1. Count the number of cancelled flights by American Airlines (AA).

# Import your libraries
import pandas as pd

# Start writing code
us_flights.head()

df = us_flights

# group by
groupby_df = df.groupby(['unique_carrier','flight_num','cancelled']).size().reset_index(name = "count")

# filtering by AA & Canceled
AA_df = groupby_df[(groupby_df['unique_carrier'] == 'AA') & (groupby_df['cancelled'] == 1)]

# add all column number
AA_df['count'].sum()

Penjelasan :
  groupby_df = groupping
  AA_df = filtering condition menggunakan bitwise operator & / AND
  .sum() = menjumlah berapa banyak yang memenuhi kondisi tersebut
  

2. Win-to-Nomination Ratio
# Import your libraries
import pandas as pd

# Start writing code
oscar_nominees.head()

# df
df = oscar_nominees
# convert column boolean winner to int
df['winner'] = df['winner'].astype('int')

# groupby
group_winner = df.groupby(['nominee','winner']).size().reset_index(name = "n_count")

agg_data = group_winner.groupby('nominee').agg({'n_count': 'sum', 'winner': 'max'}).reset_index()
agg_data

# create new column name win_to_n_ratio
agg_data['win_to_n_ratio'] = agg_data['winner'] / agg_data['n_count']
agg_data

# sorted the column
agg_data.sort_values('win_to_n_ratio', ascending = False)

Penjelasannya nanti : 
  df = nama variable dataframe
  astype = mengubah type data column, tapi untuk yang simple, jika rumit menggunakan pd.to
  group_by = grouping data
  .agg = aggregation data, jadi n_count dijumlah semua, baik itu mereka dinominasikan winner atau tidak menggunakan n_count : sum
    winner : max, dengan menggunakan max, kita melihat maximal value dari winner, karena winner ini boolean, dan apabila nominee pernah berstatus winner == 1 / True, maka hasil max akan menunjukan 1
      selengkapnya buka dokumentasi official pandas: https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html
  selebihnya sudah pernah dibahas dan cukup jelas

