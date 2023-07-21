10. Finding Updated Records

We have a table with employees and their salaries, however, 
some of the records are old and contain outdated salary information. 
Find the current salary of each employee assuming that salaries increase each year. Output their id, first name, last name, department ID, and current salary. 
Order your list by employee ID in ascending order.

DataFrame: ms_employee_salary
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
ms_employee_salary.head()

df = ms_employee_salary.copy()
df.head()

# group by
grup = df.groupby(['id','first_name','last_name','department_id']).agg({'salary' : 'max'}).reset_index()

# rename column name
grup.rename(columns = {'salary' : 'current_salary'}, inplace = True)

# sorting values
sorting = grup.sort_values('id')


Penjelasannya nanti:
