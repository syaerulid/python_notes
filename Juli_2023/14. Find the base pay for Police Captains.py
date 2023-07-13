Find the base pay for Police Captains

Find the base pay for Police Captains.
Output the employee name along with the corresponding base pay.

DataFrame: sf_public_salaries
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
sf_public_salaries.head()

df = sf_public_salaries.copy()
df.head()

# to lower jobtitle
df['jobtitle'] = df['jobtitle'].str.lower()

# filtering condition contain police and captain
df_f = df[(df['jobtitle'].str.contains('police')) & (df['jobtitle'].str.contains('captain'))]
# output
grup = df_f.groupby(['employeename','basepay']).size().reset_index()

# sorted ascending
grup = grup[['employeename','basepay']]
grup.sort_values('basepay', ascending = True)
