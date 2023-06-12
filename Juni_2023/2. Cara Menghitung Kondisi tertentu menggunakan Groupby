Disini kita akan menentukan 
"Find the review count for one-star businesses from yelp"

# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()

# groupby
df = yelp_business.groupby(['business_id','stars','review_count']).size().reset_index(name = "count")
df

count_low_rating = df[df['stars'] == 1]
count_low_rating

Penjelasan:
groupby:
yelp_business = nama dataframe
groupby = grouping dataframe agar lebih ringkas
size() = aggregate function (groupby wajib menggunakan aggregate function) <- return a Series data
reset_index = mengkonversi hasil menjadi dataframe type
name = "count" <- membuat kolom baru untuk menghitung occurence dari business_id, (jika tanpa name maka kolom memiliki nama 0)

penjelasan kedua:
[df['stars'] == 1] = filter condition
df[df['stars'] == 1] = dataframe di depan filter condition
count_low_rating = nama variable
