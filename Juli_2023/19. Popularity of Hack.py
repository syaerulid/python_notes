Meta/Facebook has developed a new programing language called Hack.To measure the popularity of Hack they ran a survey with their employees. The survey included data on previous programing familiarity as well as the number of years of experience, age, gender and most importantly satisfaction with Hack. Due to an error location data was not collected, but your supervisor demands a report showing average popularity of Hack by office location. Luckily the user IDs of employees completing the surveys were stored.
Based on the above, find the average popularity of the Hack per office location.
Output the location along with the average popularity.

DataFrames: facebook_employees, facebook_hack_survey
Expected Output Type: pandas.Series

# Import your libraries
import pandas as pd

# Start writing code
facebook_employees.head()

facebook_hack_survey.head()

# merge
df = facebook_employees.merge(
    facebook_hack_survey, how = 'left', left_on = 'id', right_on = 'employee_id')
df.head()

## selected column
df_sel = df[['location','popularity']]

# average
df_sel.groupby(['location']).agg({'popularity' : 'mean'}).reset_index()

Penjelasan :
nanti
