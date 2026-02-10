import pandas as pd

# Create a dataframe with one column containing incremental values from 1 to 100
df = pd.DataFrame({'value': range(1, 101)})

# Display the first 10 rows
print("First 10 rows of the dataframe:")
print(df.head(10))
