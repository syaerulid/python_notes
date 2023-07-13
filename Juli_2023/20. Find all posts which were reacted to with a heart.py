Find all posts which were reacted to with a heart. For such posts output all columns from facebook_posts table.

DataFrames: facebook_reactions, facebook_posts
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
facebook_reactions.head()
facebook_posts.head()

# merge
df = facebook_reactions.merge(
    facebook_posts, how = 'left', left_on = 'post_id', right_on = 'post_id')
    
# filter condition
df_h = df[df['reaction'] == 'heart']
# sel column
df_h[['post_id','poster_y','post_text','post_keywords','post_date']].drop_duplicates()

Penjelasan :
nanti
