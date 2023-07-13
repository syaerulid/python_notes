Order Details

Find order details made by Jill and Eva.
Consider the Jill and Eva as first names of customers.
Output the order date, details and cost along with the first name.
Order records based on the customer id in ascending order.

DataFrames: customers, orders
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
customers.head()
orders.head()

df = customers.merge(
    orders, how = 'left', left_on = 'id', right_on = 'cust_id')
df.head()

# filtering conditions
df_f = df[(df['first_name'] == 'Jill') | (df['first_name'] == 'Eva')]

# output
df_f[['first_name','order_date','order_details','total_order_cost']]

Penjelasan : nanti

