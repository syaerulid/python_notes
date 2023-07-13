Churro Activity Date

Find the activity date and the pe_description of facilities with the name 'STREET CHURROS' and with a score of less than 95 points.

DataFrame: los_angeles_restaurant_health_inspections
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
los_angeles_restaurant_health_inspections.head()

df = los_angeles_restaurant_health_inspections.copy()
df.head()

# filter condition
df_filter = df[(df['facility_name'] == 'STREET CHURROS') & (df['score'] < 95)]

## select some column only
selected_df = df_filter[['activity_date','pe_description']]

Penjelasan nanti :
