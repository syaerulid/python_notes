Admin Department Employees Beginning in April or Later (Judul Nanti Ganti)

# Import your libraries
import pandas as pd

# Start writing code
worker.head()

df = worker.copy()
df.head()

# filter condition april
filter_df = df.loc[(df['joining_date'] >= '2014-04-01') & (df['department'] == 'Admin')]

# count number employee
count_df = filter_df.groupby(['first_name']).size().sum()

Penjelasan Nanti
