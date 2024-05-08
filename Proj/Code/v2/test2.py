import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_and_clean_data(filepath):
    # Load the Excel file
    data = pd.read_excel(filepath)

    # Drop columns with many missing values or unnamed
    columns_to_drop = [col for col in data.columns if 'Unnamed' in col]
    cleaned_data = data.drop(columns=columns_to_drop)

    # Fill missing numerical values with zeros or forward fill method depending on the context of the data
    cleaned_data.ffill(inplace=True)
  # forward fill to maintain consistency in time series data
    cleaned_data.fillna(0, inplace=True)  # fill remaining NaNs with 0 which could be initial states

    # Ensure the Date column is in datetime format
    cleaned_data['Date'] = pd.to_datetime(cleaned_data['Date'])

    return cleaned_data


def numerical_derivative(data, column_name):
    differences = data[column_name].diff().fillna(0)
    time_diff = data['Date'].diff().dt.days.fillna(1)  # Avoid division by zero
    derivative = differences / time_diff
    return derivative


def numerical_integration(data, column_name):
    differences = data[column_name].diff().fillna(0)
    time_diff = data['Date'].diff().dt.days.fillna(1)
    trapezoids = 0.5 * (data[column_name].shift(1).fillna(0) + data[column_name]) * time_diff
    integral = trapezoids.cumsum()
    return integral


def prepare_reported_data():
    # Reported data from Russian and Ukrainian media
    reported_data_russia = {"Russia": {"Tanks": 1180, "AFV": np.nan, "IFV": 2470, "APC": 2470}}
    reported_data_ukraine = {
        "Personnel": 447510, "Tanks": 7074, "AFVs": 13551, "Artillery": 11316, "MLRS": 1036,
        "AntiAir": 749, "Aircraft": 347, "Helicopters": 325, "UAVs": 8956, "CruiseMissiles": 2064,
        "Ships": 26, "Submarines": 1, "Vehicles": 15071, "SpecialEquipment": 1864,
    }

    df_reported_russia_flat = pd.DataFrame.from_dict({k: v for k, v in reported_data_russia['Russia'].items()},
                                                     orient='index', columns=['Russia Reported (Russian Media)'])
    df_reported_ukraine_flat = pd.DataFrame.from_dict(reported_data_ukraine, orient='index',
                                                      columns=['Ukraine Reported (Ukrainian Media)'])

    all_categories = set(df_reported_russia_flat.index).union(set(df_reported_ukraine_flat.index))
    df_reported_russia_flat = df_reported_russia_flat.reindex(all_categories).fillna('No data')
    df_reported_ukraine_flat = df_reported_ukraine_flat.reindex(all_categories).fillna('No data')

    df_reported_combined = pd.concat([df_reported_russia_flat, df_reported_ukraine_flat], axis=1)
    return df_reported_combined


def main():
    filepath = 'data_excel.xlsx'  # Update this path as needed
    cleaned_data = load_and_clean_data(filepath)
    russia_derivative = numerical_derivative(cleaned_data, 'Russia_Destroyed')
    ukraine_derivative = numerical_derivative(cleaned_data, 'Ukraine_Destroyed')
    russia_integral = numerical_integration(cleaned_data, 'Russia_Destroyed')
    ukraine_integral = numerical_integration(cleaned_data, 'Ukraine_Destroyed')

    df_reported_combined = prepare_reported_data()
    print(df_reported_combined.head())


if __name__ == '__main__':
    main()
