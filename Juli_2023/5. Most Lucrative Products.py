You have been asked to find the 5 most lucrative products in terms of total revenue for the first half of 2022 (from January to June inclusive).


Output their IDs and the total revenue.

DataFrame: online_ordersExpected 
Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
online_orders.head()

df = online_orders.copy()
df.head()

# create new column name total
df['total'] = df['cost_in_dollars'] * df['units_sold']

# group by product karena di sum 
total = df.groupby('product_id')['total'].sum().reset_index()

# sorting descending
descend_total = total.sort_values('total', ascending = False)

# Top 5
descend_total.head()

Penjelasan nanti :
