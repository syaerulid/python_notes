Average Salaries

Compare each employee's salary with the average salary of the corresponding department.
Output the department, first name, and salary of employees along with the average salary of that department.

DataFrame: employee
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
employee.head()
# head
df = employee.copy()
df.head()

# group by
grup = df.groupby(['department','first_name','salary']).size().reset_index()

# selected column only
grup = grup[['department','first_name','salary']]

# average
avg_salary = grup.groupby(['department']).agg({'salary':'mean'}).reset_index()
avg_salary.rename(columns = {'salary' : 'avg_salary'}, inplace = True)

avg_salary

# concat / merge / join
dfg = grup.merge(
    avg_salary, how = 'left', left_on = 'department', right_on = 'department')
dfg.drop_duplicates()

Penjelasan :
nanti
