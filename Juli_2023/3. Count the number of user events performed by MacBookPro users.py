Count the number of user events performed by MacBookPro users.
Output the result along with the event name.
Sort the result based on the event count in the descending order.

DataFrame: playbook_events
Expected Output Type: pandas.DataFrame

# Import your libraries
import pandas as pd

# Start writing code
playbook_events.head()
df = playbook_events.copy()
df.head()

# filter condition macbook
macbook = df[df['device'] == 'macbook pro']

grup = macbook.groupby(['event_name','device']).size().reset_index(name = "event_count")

column_count = grup[['event_name','event_count']]

Penjelasan nanti
