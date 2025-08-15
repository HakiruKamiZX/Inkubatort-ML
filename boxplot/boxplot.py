import pandas as pd
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import numpy as np

try:
    # Load the dataset from the CSV file
    df = pd.read_csv('cleaned_data.csv')
    print("Successfully loaded 'cleaned_data.csv'.")

    col_to_analyze = 'Tanda Vital: Suhu'

    print(f"\n--- Outlier Detection Report for '{col_to_analyze}' ---")
    if col_to_analyze in df.columns:

        col_data = df[col_to_analyze].dropna()

        if col_data.empty:
            print(f"\nColumn '{col_to_analyze}' contains no numerical data.")
        else:
            Q1 = col_data.quantile(0.25)
            Q3 = col_data.quantile(0.75)
            
            IQR = Q3 - Q1
            
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = df[(df[col_to_analyze] < lower_bound) | (df[col_to_analyze] > upper_bound)]
            
            if not outliers.empty:
                print(f"Found {len(outliers)} outliers in '{col_to_analyze}':")

                print(outliers[[col_to_analyze]]) 
            else:
                print(f"No outliers detected in '{col_to_analyze}'.")

            print(f"\nGenerating a boxplot for '{col_to_analyze}'...")
            plt.figure(figsize=(8, 6)) 
            df[[col_to_analyze]].plot(kind='box', patch_artist=True)
            plt.title(f"Boxplot for {col_to_analyze}", fontsize=16)
            plt.ylabel("Values")
            
            output_filename = 'suhu_outlier_boxplot.png'
            plt.savefig(output_filename)
            
            print(f"\nBoxplot saved successfully to '{output_filename}'")
    else:
        print(f"Error: Column '{col_to_analyze}' not found in the CSV file.")


except FileNotFoundError:
    print("Error: 'cleaned_data.csv' not found. Please ensure the file is in the same directory as the script.")
except Exception as e:
    print(f"An error occurred: {e}")

