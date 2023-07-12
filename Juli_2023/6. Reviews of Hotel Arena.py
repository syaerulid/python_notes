Reviews of Hotel Arena

Find the number of rows for each review score earned by 'Hotel Arena'. Output the hotel name (which should be 'Hotel Arena'), review score along with the corresponding number of rows with that score for the specified hotel.

DataFrame: hotel_reviews
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
hotel_reviews.head()

df = hotel_reviews.copy()
df.head()

# filter condition hotel arena
df_filter = df[df['hotel_name'] == 'Hotel Arena']

# coba group by
grup_filter = df_filter.groupby(['reviewer_score','hotel_name']).size().reset_index(name = 'n_reviews')

