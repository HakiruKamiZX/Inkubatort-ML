import pandas as pd

# Load the generated CSV file
file_name = "Generated_Parameter_Bayi_Inkubator_NICU_V2.csv"
df = pd.read_csv(file_name)

# Get the number of rows
num_entries = df.shape[0]

print(f"Jumlah entries (baris) dalam file '{file_name}' adalah: {num_entries}")