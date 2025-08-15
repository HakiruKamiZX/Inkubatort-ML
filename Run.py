import pandas as pd
import io

file_path = 'cleaned_data.csv'

try:
    df = pd.read_csv(file_path, encoding='utf-8')

    print("Successfully loaded the CSV file. Here are the first 5 rows:")
    print(df.head())
  
    print("\nDataFrame Information:")
    df.info()

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    print("Please make sure the CSV file is in the same directory as this script.")
except Exception as e:
    print(f"An error occurred: {e}")

