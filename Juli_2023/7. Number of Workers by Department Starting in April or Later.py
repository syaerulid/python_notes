Number of Workers by Department Starting in April or Later

Find the number of workers by department who joined in or after April.


Output the department name along with the corresponding number of workers.


Sort records based on the number of workers in descending order.

DataFrame: workerExpected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
worker.head()

df = worker.copy()
df.head()

# filter condition after april
after_apr = df[df['joining_date'] >= '2014-04-01']

# group by
grup_apr = after_apr.groupby(['department','first_name','worker_id']).size().reset_index(name = "num_workers")

# sum the count based on deparment
grup_april = grup_apr.groupby('department').sum().reset_index()

# select column tertentu doang
grup_april = grup_april[['department','num_workers']]

#sorting descending
grup_april.sort_values('num_workers', ascending = False)

Penjelasan nanti :

