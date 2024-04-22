
import pandas as pd

def numerical_derivative(data, column_name):
    # Calculate differences and time differences
    differences = data[column_name].diff().fillna(0)
    time_diff = data['Date'].diff().dt.days.fillna(1)  # Avoid division by zero
    derivative = differences / time_diff
    return derivative

def numerical_integration(data, column_name):
    # Differences for trapezoidal rule and time differences
    differences = data[column_name].diff().fillna(0)
    time_diff = data['Date'].diff().dt.days.fillna(1)
    trapezoids = 0.5 * (data[column_name].shift(1).fillna(0) + data[column_name]) * time_diff
    integral = trapezoids.cumsum()
    return integral

def load_and_prepare_data(filepath):
    data = pd.read_excel(filepath)
    data['Date'] = pd.to_datetime(data['Date'])
    return data

def main():
    filepath = 'data_excel.xlsx'  # Update the path to your data file
    data = load_and_prepare_data(filepath)
    derivative = numerical_derivative(data, 'Russia_Destroyed')
    integral = numerical_integration(data, 'Russia_Destroyed')
    print('Derivative head:', derivative.head())
    print('Integral head:', integral.head())

if __name__ == '__main__':
    main()
