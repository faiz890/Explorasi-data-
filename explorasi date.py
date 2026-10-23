import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
# ==========================================
# 1. DATA LOADING
# ==========================================
print('=== 1. MEMUAT DATASET RETAIL SALES ===')
file_path = 'retail sales.csv'
df = pd.read_csv(file_path)

# Menampilkan 5 baris pertama
print(df.head())

# ==========================================
# 2. INFORMASI & STRUKTUR DATA
# ==========================================
print('\n=== 2. INFORMASI & STRUKTUR DATA (INFO) ===')
df.info()

print('\n=== 3. STATISTIK DESKRIPTIF ===')
print(df.describe())

# ==========================================
# 3. PENGECEKAN DATA KOSONG (NULL) & DUPLIKAT
# ==========================================
print('\n=== 4. PENGECEKAN NULL & DUPLIKAT ===')
print('Jumlah data null/kosong tiap kolom:')
print(df.isnull().sum())

print(f'\nTotal baris duplikat: {df.duplicated().sum()}')

# Penanganan data kosong & duplikat (jika ada)
df = df.dropna()
df = df.drop_duplicates()

# ==========================================
# 4. PEMBAGIAN JENIS DATA (KATEGORIKAL & NUMERIKAL)
# ==========================================
print('\n=== 5. KLASIFIKASI JENIS DATA ===')
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
numerical_cols = df.select_dtypes(include=['number']).columns.tolist()

print(f'Data Kategorikal (Objek/Teks): {categorical_cols}')
print(f'Data Numerikal (Angka): {numerical_cols}')

# ==========================================
# 5. EKSPLORASI DATA LANJUTAN & VISUALISASI
# ==========================================
print('\n=== 6. MENAMPILKAN EKSPLORASI & VISUALISASI DATA ===')

# Distribusi kategori produk
print('\nDistribusi Berdasarkan Kategori Produk:')
print(df['Category'].value_counts())

# Visualisasi 1: Jumlah Transaksi Berdasarkan Kategori Produk
plt.figure(figsize=(10, 5))
sns.countplot(
    data=df, x='Category', order=df['Category'].value_counts().index, palette='crest'
)
plt.title('Jumlah Transaksi Berdasarkan Kategori Produk')
plt.xlabel('Kategori')
plt.ylabel('Jumlah Transaksi')
plt.tight_layout()
plt.show()

# Visualisasi 2: Total Pendapatan (*Total Amount*) Berdasarkan Kategori
category_sales = df.groupby('Category')['Total_Amount'].sum().reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(
    data=category_sales,
    x='Category',
    y='Total_Amount',
    order=category_sales.sort_values('Total_Amount', ascending=False)[
        'Category'
    ],
    palette='viridis',
)
plt.title('Total Pendapatan (Revenue) Berdasarkan Kategori Produk')
plt.xlabel('Kategori')
plt.ylabel('Total Pendapatan')
plt.tight_layout()
plt.show()

# Visualisasi 3: Korelasi Antar Fitur Numerikal
plt.figure(figsize=(8, 6))
sns.heatmap(
    df.select_dtypes(include=[np.number]).corr(),
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
)
plt.title('Korelasi Antar Fitur Numerikal')
plt.tight_layout()
plt.show()

print('=== EKSPLORASI DATA SELESAI ===')