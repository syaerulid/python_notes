Count the number of cancelled flights by American Airlines (AA).

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
