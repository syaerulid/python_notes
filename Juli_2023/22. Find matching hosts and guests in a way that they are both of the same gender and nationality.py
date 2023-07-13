Find matching hosts and guests pairs in a way that they are both of the same gender and nationality.
Output the host id and the guest id of matched pair.

DataFrames: airbnb_hosts, airbnb_guests
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
airbnb_hosts.head()

airbnb_guests.head()

df = airbnb_hosts.merge(
    airbnb_guests, how = 'left', left_on = ['nationality','gender'], right_on = ['nationality','gender'])
df.head()

# selected column
df[['host_id','guest_id']].drop_duplicates()

Penjelasan :
nanti





