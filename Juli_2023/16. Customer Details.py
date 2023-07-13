Find the details of each customer regardless of whether the customer made an order. 
Output the customer's first name, last name, and the city along with the order details.
You may have duplicate rows in your results due to a customer ordering several of the same items. 
Sort records based on the customer's first name and the order details in ascending order.

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

# selected column
selected_df = df[['first_name','last_name','city','order_details']]
selected_df.sort_values(by = ['first_name', 'order_details'], ascending = [True, True])

Penjelasan : nanti
