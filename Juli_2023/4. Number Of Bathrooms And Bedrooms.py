Find the average number of bathrooms and bedrooms for each city’s property types. 
Output the result along with the city name and the property type.

DataFrame: airbnb_search_details
Expected Output Type: pandas.DataFrame


# Import your libraries
import pandas as pd

# Start writing code
airbnb_search_details.head()

df = airbnb_search_details.copy()
df.head()

# find mean average 
df.groupby(['city','property_type']).agg({'bedrooms':'mean','bathrooms':'mean'}).reset_index()

# Penjelasan nanti
