import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io

# --- Main Program Starts Here ---

try:
    # Load the dataset from the CSV file
    # The script will first try to read 'cleaned_data.csv'.
    df = pd.read_csv('cleaned_data.csv')
    print("Successfully loaded 'cleaned_data.csv'.")

    # Select only the numerical columns to check for outliers
    numerical_cols = df.select_dtypes(include=np.number).columns.tolist()

    print("\n--- Outlier Detection Report ---")

    # Iterate over each numerical column to find and display outliers
    for col in numerical_cols:
        # Drop missing values for calculation to avoid errors
        col_data = df[col].dropna()

        print(f"\nAnalyzing column: '{col}'")
        
        # Calculate Q1 (25th percentile) and Q3 (75th percentile)
        Q1 = col_data.quantile(0.25)
        Q3 = col_data.quantile(0.75)
        
        # Calculate the Interquartile Range (IQR)
        IQR = Q3 - Q1
        
        # Define the lower and upper bounds for outlier detection
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Identify outliers
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        
        if not outliers.empty:
            print(f"Found {len(outliers)} outliers in '{col}':")
            # Display the rows containing outliers
            print(outliers[[col]]) # Show only the relevant column for clarity
        else:
            print(f"No outliers detected in '{col}'.")

    # --- Visualization with Boxplots ---
    if numerical_cols:
        print("\nGenerating boxplots for visualization...")
        # Create a boxplot for each numerical column
        plt.figure(figsize=(20, 10)) # Increased figure size for better readability
        df[numerical_cols].plot(kind='box', subplots=True, layout=(-1, 5),
                               sharey=False, patch_artist=True, figsize=(20, 10))
        plt.suptitle("Boxplot for Each Numerical Feature to Visualize Outliers", fontsize=16)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        
        # *** CHANGE: Save the plot to a file instead of showing it ***
        output_filename = 'outlier_boxplots.png'
        plt.savefig(output_filename)
        
        print(f"\nBoxplots saved successfully to '{output_filename}'")
        # plt.show() # This line is commented out to prevent the Tcl/Tk error

    else:
        print("\nNo numerical columns found to create boxplots.")

except FileNotFoundError:
    print("Error: 'cleaned_data.csv' not found. Please ensure the file is in the same directory as the script.")
except Exception as e:
    print(f"An error occurred: {e}")