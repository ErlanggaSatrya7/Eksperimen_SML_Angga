import pandas as pd
import os

# Membaca dataset mentah
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# --- CONTOH PROSES PREPROCESSING ---
# 1. Drop baris yang kosong (misal)
df = df.dropna()

# 2. Simpan hasilnya menjadi data_siap_latih.csv
output_path = 'preprocessing/data_siap_latih.csv'
df.to_csv(output_path, index=False)

print(f"Preprocessing selesai! File disimpan di: {output_path}")