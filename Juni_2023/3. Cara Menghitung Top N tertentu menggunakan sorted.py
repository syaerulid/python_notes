1. Disini kita menghitung Top 5 Business dengan review terbanyak

# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()

grouped_name = yelp_business.groupby(['name','review_count']).size().reset_index(name="count")

# sort by descending
sorted_list = grouped_name.sort_values('review_count', ascending = False)
sorted_list.head()

# select only desired column
sorted_list = sorted_list[['name','review_count']]
sorted_list.head()

Penjelasan:
yelp_business = dataframe
grouped_name = variable untuk groupby
sorted_list = variable untuk mengurutkan data
sort_values = mengurutkan data
review_count = kolom yang dipakai acuan untuk mengurutkan data
ascending = False <- hasil yang diinginkan adalah descending 
sorted_list.head() = menampilkan 5 terbesar saja

2. Disini kita menghitung Top 5 States dengan jumlah 5 Stars terbanyak

# Start writing code
yelp_business.head()
# grouping by
yb_group = yelp_business.groupby(['state','stars']).size().reset_index(name = "n_business") ## grouping + convert series to dataframe type
yb_group

yb_group[yb_group['stars'] == 5] ## conditional_formatting

# sort by count
ya_group = yb_group[yb_group['stars'] == 5].sort_values('n_business', ascending = False) ## conditional_formatting + sorting

# select only desired column
ya_selected = ya_group[['state','n_business']]
ya_selected.head(6)
