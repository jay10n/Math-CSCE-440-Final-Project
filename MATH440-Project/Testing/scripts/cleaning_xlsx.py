import pandas as pd
df = pd.read_excel('Data/SourceFiles/Documented/documented_losses.xlsx')
print(df.isnull().sum())
print(df.dtypes)

# Clean Column Names
# This removes any spaces, converts all characters to lower case, and handles repetitive naming patterns
df.columns = [col.strip().replace(' ', '_').lower().replace('.1', '_change') for col in df.columns]

# Drop Unnecessary Columns
# Identify and drop columns that are entirely empty or not relevant
columns_to_drop = [col for col in df.columns if 'unnamed' in col]
df.drop(columns=columns_to_drop, inplace=True)

# Convert Date Format
# Converts the 'date' column from string to datetime format for better manipulation
df['date'] = pd.to_datetime(df['date'])

# Handle Missing Values
# Fills missing values with zeros for demonstration; adjust this based on your analysis requirements
df.fillna(0, inplace=True)

# Display the DataFrame information and the first few rows to verify the changes
print(df.info())
print(df.head())


# Statistical summary of numerical columns
print(df.describe())

# Check unique values and their counts for a specific column, e.g., 'date'
print(df['date'].value_counts())

# Range checks for a numerical column, e.g., 'russia_total'
print(df[df['russia_total'] < 0])  # This should return an empty DataFrame if all values are valid

# Check date consistency and order
print(df['date'].min(), df['date'].max())  # Check the range of dates
print(df['date'].is_monotonic_increasing)  # Check if dates are in chronological order

# Recheck for any null values
print(df.isnull().sum().sum())  # This should return 0 if there are no null values left
