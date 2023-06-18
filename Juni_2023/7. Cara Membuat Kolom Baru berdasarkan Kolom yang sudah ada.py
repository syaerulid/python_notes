1. Advertising Channel Effectiveness

Find the effectiveness of each advertising channel in the period from 2017 to 2018 (both included). 
The effectiveness is calculated as the ratio of total money spent to total customers aquired.
Output the advertising channel along with corresponding effectiveness. Sort records by the effectiveness in ascending order.

# Import your libraries
import pandas as pd
# Start writing code
uber_advertising.head()
# df
df = uber_advertising
# filter condition year
df = df[(df['year'] >= 2017) & (df['year'] <= 2018)]
# create new column name effectivenes with condition
df['effectivenes'] = df['money_spent'] / df['customers_acquired']
df.head()
# sort the effectivenes
df.sort_values('effectivenes')

