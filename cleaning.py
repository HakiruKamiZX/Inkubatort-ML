import pandas as pd

file_path = 'Parameter_Bayi_Inkubator_NICU.csv'
df = pd.read_csv(file_path)

missing_values_all_columns = df.isnull().sum()

print("Total missing values in each column:")
print(missing_values_all_columns)