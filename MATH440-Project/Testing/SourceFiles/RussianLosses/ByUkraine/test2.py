import pandas as pd

# Assuming the data is in a CSV-like format with appropriate separators
df = pd.read_csv('Fixed_russian_losses_by_ukraine.csv', delimiter=',')  # Adjust delimiter if necessary
print(df.head())  # Display the first few rows to confirm successful loading
