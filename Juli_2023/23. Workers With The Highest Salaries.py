23. Workers With The Highest Salaries

You have been asked to find the job titles of the highest-paid employees.


Your output should include the highest-paid title or multiple titles with the same salary.

DataFrames: worker, title
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
worker.head()
title.head()

# merge
df = worker.merge(
    title, how = 'left', left_on = 'worker_id', right_on = 'worker_ref_id')
df_s = df[['salary','worker_title']]

# max salary
df_max = df_s.groupby(['worker_title']).agg({'salary' : 'max'}).reset_index()
df_max_dua = df_max.sort_values('salary', ascending = False)

# rename
df_max_dua.rename(columns = {'worker_title' : 'best_paid_title'}, inplace = True)
df_max_dua[['best_paid_title']].head(2)

Penjelasan :
nanti
