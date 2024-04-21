import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'CuFt (y)': [55, 68, 60, 40, 45, 49, 62, 56, 93, 76, 94, 82, 86, 55, 71, 67, 73, 87, 80, 77, 64, 60, 65, 65, 83, 67, 61, 51],
    'BA/ac (x1)': [51, 100, 63, 52, 67, 42, 81, 70, 108, 90, 110, 111, 94, 82, 65, 87, 108, 105, 100, 103, 55, 60, 70, 78, 85, 92, 82, 56],
    '%Bspruce (x2)': [79, 48, 67, 52, 52, 82, 80, 65, 96, 81, 78, 59, 84, 48, 93, 68, 51, 82, 70, 61, 96, 80, 76, 74, 96, 58, 58, 69],
    'SI (x3)': [45, 53, 44, 31, 29, 43, 42, 36, 63, 60, 56, 48, 53, 40, 35, 41, 54, 51, 45, 43, 51, 47, 40, 46, 55, 50, 38, 35]
}
df = pd.DataFrame(data)

correlation_matrix = df.corr()
print("Correlation Matrix:\n", correlation_matrix)


X = df[['BA/ac (x1)', '%Bspruce (x2)', 'SI (x3)']].values
y = df['CuFt (y)'].values

model = LinearRegression().fit(X, y)

coefficients = model.coef_
intercept = model.intercept_

print("Coefficients:", coefficients)
print("Intercept:", intercept)
