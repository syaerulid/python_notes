Number Of Units Per Nationality

Find the number of apartments per nationality that are owned by people under 30 years old.


Output the nationality along with the number of apartments.


Sort records by the apartments count in descending order.

DataFrames: airbnb_hosts, airbnb_units
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
airbnb_hosts.head()
airbnb_units.head()

df = airbnb_units.merge(
    airbnb_hosts, how = 'right', right_on = 'host_id', left_on = 'host_id')
df.head()

# filter conditions
df_f = df[(df['unit_type'] == 'Apartment') & (df['age'] < 30)]

# group
df_f = df_f[['nationality','unit_id','unit_type']]
df_f = df_f.drop_duplicates()

# output
df_f.groupby(['nationality']).size().reset_index(name = "apartment_count")

Penjelasan :
nanti
