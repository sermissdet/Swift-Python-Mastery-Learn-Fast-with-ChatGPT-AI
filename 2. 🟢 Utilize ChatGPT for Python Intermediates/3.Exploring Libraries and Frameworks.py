#If you want to learn about libraries or frameworks, ask for recommendations based on your project needs.
#Ask ChatGPT:  “How can I use the Pandas library for data analysis?”
#Example: Using Pandas for Data Analysis

import pandas as pd

# Load a CSV file
data = pd.read_csv('data.csv')

# Display the first 5 rows
print(data.head())

# Calculate the average of a column
average = data['column_name'].mean()
print("Average:", average)
