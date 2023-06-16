1. Find all wineries which produce wines by possessing aromas of plum, cherry, rose, or hazelnut

# Import your libraries
import pandas as pd
# Start writing code
winemag_p1.head()

# groupby
wine = winemag_p1.groupby(['winery','description']).size().reset_index(name="count")

# convert description to lower
wine['description'] = wine['description'].str.lower()
# check word contains plum, cherry, rose, or hazelnut
word_check = wine['description'].str.contains('cherry|plum|rose|hazelnut', case=True, na=False) 
wine_check = wine[word_check].drop_duplicates()

# selected column only
selected_wine = wine_check[['winery']]

Penjelasan :
  winemag_p1 = dataaset
  wine = groupping sehingga tersisa 2 kolom sebelum melakukan analisa lebih jauh
  .str.lower() = mengubah konten / isi dari kolom ['description'] menjadi lower case(karena agar case = True, match case insensitive)
  .str.contains() = mengecek apakah dalam kolom ['description'] mengandung kata tertentu yaitu 'cherry|plum|roze|hazelnut'
  | = OR
  .drop_duplicates = hanya menampilkan semua unique value
