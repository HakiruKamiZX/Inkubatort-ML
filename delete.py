import pandas as pd

# Define the path to your CSV file
file_path = 'Parameter_Bayi_Inkubator_NICU.csv'

try:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path, encoding='utf-8')
    print("File loaded successfully.")
    print("-" * 30)

    # --- Verify the column exists before deleting ---
    print("Original columns in the DataFrame:")
    print(df.columns.to_list())
    print("-" * 30)


    # --- Delete the specified column ---
    column_to_delete = 'Umur'

    # Check if the column exists before trying to drop it
    if column_to_delete in df.columns:
        # The drop() method removes the specified column.
        # 'axis=1' tells pandas to drop a column (axis=0 would be for a row).
        # 'inplace=True' modifies the DataFrame directly without needing to reassign it.
        df.drop(column_to_delete, axis=1, inplace=True)
        print(f"Successfully deleted the '{column_to_delete}' column.")
    else:
        print(f"Column '{column_to_delete}' not found in the DataFrame.")

    print("-" * 30)

    # --- Verify the column has been deleted ---
    print("Updated columns in the DataFrame:")
    print(df.columns.to_list())
    print("-" * 30)

    # Display the first 5 rows of the modified DataFrame
    print("Here is a preview of the data with the column removed:")
    print(df.head())


except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

df.to_csv('cleaned_data.csv', index=False)