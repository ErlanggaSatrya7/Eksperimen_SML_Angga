import pandas as pd
import os

# Membaca dataset mentah yang ada di folder luar (satu tingkat di atas)
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Contoh preprocessing sederhana: drop baris yang kosong
df = df.dropna()

# Menyimpan hasil ke folder preprocessing/data_siap_latih.csv
output_path = 'preprocessing/data_siap_latih.csv'
df.to_csv(output_path, index=False)

print(f"Berhasil! File {output_path} sudah dibuat.")