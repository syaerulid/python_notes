Find libraries who haven't provided the email address in circulation year 2016 but their notice preference definition is set to email

Find libraries who haven't provided the email address in circulation year 2016 but their notice preference definition is set to email.
Output the library code.

DataFrame: library_usage
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
library_usage.head()

df = library_usage.copy()
df.head()

# filtering condition
df_f = df[(df['circulation_active_year'] == 2016) & (df['notice_preference_definition'] == 'email')]

# filtering condition 2
false_email = df_f.loc[~df.provided_email_address]

# selected column
selected_col = false_email[['home_library_code']]

selected_col['home_library_code'].unique()

Penjelasan annti :
