Find all Lyft drivers who earn either equal to or less than 30k USD or equal to or more than 70k USD.
Output all details related to retrieved records.

DataFrame: lyft_drivers
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
lyft_drivers.head()

df = lyft_drivers.copy()
df.head()

# filter condition
df[(df['yearly_salary'] <= 30000) | (df['yearly_salary'] >= 70000)]

Penjelasan : nanti
