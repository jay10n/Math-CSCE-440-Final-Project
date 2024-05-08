import pandas as pd

# Initialize lists to store the data
data = []
current_date = None
current_dict = {}

# Open and read the file
with open('Data/SourceFiles/RussianLosses/ByUkraine/russian_losses_by_ukraine.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue  # Skip empty lines
        if line == '---':
            if current_dict:
                data.append(current_dict)
                current_dict = {}  # Reset for the next block of data
        elif line.count('-') == 2:  # Likely a date line
            current_date = line  # Set the current date
            current_dict['Date'] = current_date
        else:  # Data line
            parts = line.split(',')
            if len(parts) >= 2:
                equipment = parts[0].strip()
                total = parts[1].strip()
                change = parts[2].strip(' (+)') if len(parts) > 2 else '0'  # Handle missing changes
                current_dict[equipment] = {'Total': total, 'Change': change}

# Add the last entry if file does not end with separator
if current_dict:
    data.append(current_dict)

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(data)
print(df.head())  # Display the first few entries
