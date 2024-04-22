
import pandas as pd
import matplotlib.pyplot as plt

def load_and_clean_data(filepath):
    # Load the Excel file
    data = pd.read_excel(filepath)
    
    # Drop columns with many missing values or unnamed
    columns_to_drop = [col for col in data.columns if 'Unnamed' in col]
    cleaned_data = data.drop(columns=columns_to_drop)
    
    # Fill missing numerical values with zeros or forward fill method depending on the context of the data
    cleaned_data.fillna(method='ffill', inplace=True)  # forward fill to maintain consistency in time series data
    cleaned_data.fillna(0, inplace=True)  # fill remaining NaNs with 0 which could be initial states
    
    # Ensure the Date column is in datetime format
    cleaned_data['Date'] = pd.to_datetime(cleaned_data['Date'])
    
    return cleaned_data

def plot_time_series_data(cleaned_data, columns_to_plot):
    # Create a figure and set of subplots
    fig, axes = plt.subplots(nrows=len(columns_to_plot), ncols=1, figsize=(12, 16))

    # Plotting time series data
    for i, col in enumerate(columns_to_plot):
        axes[i].plot(cleaned_data['Date'], cleaned_data[col], label=col)
        axes[i].set_title(col)
        axes[i].set_xlabel('Date')
        axes[i].set_ylabel('Count')
        axes[i].legend()

    plt.tight_layout()
    plt.show()

def main():
    filepath = 'data_excel.xlsx'  # Update this path as needed
    cleaned_data = load_and_clean_data(filepath)
    columns_to_plot = ['Russia_Destroyed', 'Ukraine_Destroyed', 'Russia_Damaged', 'Ukraine_Damaged']
    plot_time_series_data(cleaned_data, columns_to_plot)

if __name__ == '__main__':
    main()
