import pandas as pd

# Nama file CSV yang akan dianalisis
file_name = "Parameter_Bayi_Inkubator_NICU.csv"

try:
    # Membaca file CSV ke dalam DataFrame pandas
    df = pd.read_csv(file_name)

    # Mendapatkan daftar nama kolom
    column_names = df.columns.tolist()

    # Menghitung jumlah kolom
    num_columns = len(column_names)

    # Mengambil 3 kolom pertama
    first_columns = column_names[:3]

    # Mengambil 3 kolom terakhir
    last_columns = column_names[-3:]

    # Menampilkan output sesuai format yang diminta
    print(f"Berikut adalah daftar beberapa kolom dalam file '{file_name}':\n")

    for i, col in enumerate(first_columns):
        print(f"[{i+1}] {col}")

    # Indikasi skip jika ada banyak kolom di antaranya
    if num_columns > (len(first_columns) + len(last_columns)):
        print("\n...\n")

    # Menampilkan kolom-kolom terakhir dengan penomoran yang benar
    start_index_last_columns = num_columns - len(last_columns)
    for i, col in enumerate(last_columns):
        print(f"[{start_index_last_columns + i + 1}] {col}")

    print(f"\nTotal jumlah kolom: {num_columns}")

except FileNotFoundError:
    print(f"Error: File '{file_name}' tidak ditemukan. Pastikan file berada di direktori yang sama dengan skrip Python.")
except Exception as e:
    print(f"Terjadi kesalahan saat membaca file: {e}")