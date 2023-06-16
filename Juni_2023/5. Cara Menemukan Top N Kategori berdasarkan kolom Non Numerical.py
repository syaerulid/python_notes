1. Find the top business categories based on the total number of reviews

# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()

# groupby
grup = yelp_business.groupby(['categories','review_count']).size().reset_index()

# split category
grup_baru = grup['categories'] = grup['categories'].str.split(';')

# exploded the categories list
grup_explode = grup_baru.explode('categories')

# re-assign review_count back
grup_explode = df.assign(review_count = df['review_count'])

# sum the review_count
df_new = grup_explode.groupby('categories')['review_count'].sum().reset_index()

# reorder
df_new.sort_values('review_count', ascending = False)

Penjelasan :
  grup = nama variable dataframe yang di groupby
  str.split(';') mensplit kategori yang memiliki separator ';'
  explode = memisahkan multiple kategori yang telah di split menjadi single kategori
  assign = memasukan kembali kolom ['review_count'] kedalam dataframe
  sum = menjumlahkan review_count
  reorder = mengurutkan dataframe berdasarkan review_count dari yang terbesar (descending)



