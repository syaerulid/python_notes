Number of Shipments Per Month

Write a query that will calculate the number of shipments per month. 
The unique key for one shipment is a combination of shipment_id and sub_id. 
  Output the year_month in format YYYY-MM and the number of shipments in that month.

DataFrame: amazon_shipment
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
amazon_shipment.head()

df = amazon_shipment.copy()

df['sub_id'].unique()
# replace value
df['sub_id'] = df['sub_id'].replace(
    to_replace=[1,2,3],
    value = ['A', 'B', 'C'])

# shipment_id to str
df['shipment_id'] = df['shipment_id'].astype(str)

# combine
df['ship_sub'] = df['shipment_id'] + df['sub_id']

selected = df[['shipment_date','ship_sub']]

# extract yyyy-mm
selected['shipment_date'] = selected['shipment_date'].dt.strftime('%Y-%m')

selected.head()

# count
selected.groupby(['shipment_date']).size().reset_index(name = 'count')

Penjelasan : nanti
