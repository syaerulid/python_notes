Find wine varieties tasted by 'Roger Voss' and with a value in the 'region_1' column of the dataset. Output unique variety names only.

# Import your libraries
import pandas as pd

# Start writing code
winemag_p2.head()

df_grouped = winemag_p2.groupby(['variety','taster_name','region_1']).size().reset_index()

# filter condition
grouped_voss = df_grouped[df_grouped['taster_name'] == 'Roger Voss']

# unique_value
unique_var = pd.DataFrame({'variety' : grouped_voss['variety'].unique()}).reset_index(drop=True)

Penjelasan:
 Group By:
  df_grouped = variable groupby df
  size() = aggregate value
  reset_index() = membentuk dataframe
  [df_grouped['taster_name'] == 'Roger Voss'] <- filter condition
 Unique_Value:
  grouped_voss['variety'].unique() = mengeluarkan unique value ['variety'] dari dataframe yang sudah difilter sebelumnya
  {'variety': grouped_voss['variety'].unique()} = membuat dictionary dimana key:variety, dan value:unique values dalam bentuk numpy array
  pd.DataFrame = membuat dataframe baru berdasarkan dictionary sebelumnya (ingat case insensitive)
  drop=True <- drop index yang lama
  
  
