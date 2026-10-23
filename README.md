📊 Retail Sales Exploratory Data Analysis (EDA)

Proyek ini berfokus pada Eksplorasi dan Analisis Data Penjualan Ritel (Retail Sales) menggunakan Python. Proyek ini bertujuan untuk mengidentifikasi pola penjualan, persebaran transaksi antar kategori produk, total pendapatan (revenue), serta korelasi antar variabel numerik dalam dataset.

🚀 Fitur Utama & Alur Analisis

Pemuatan & Pemeriksaan Data (Data Loading & Inspection):

Menampilkan sampel data awal (df.head()).

Memeriksa tipe data, struktur kolom, dan informasi memori (df.info()).

Menganalisis ringkasan statistik deskriptif (df.describe()).

Pembersihan Data (Data Cleaning):

Pengecekan dan penanganan nilai kosong/hilang (missing values/null).

Deteksi dan penghapusan data duplikat untuk menjaga integritas data.

Klasifikasi Tipe Data:

Pemisahan otomatis antara kolom Kategorikal (teks/objek) dan Numerikal (angka).

Visualisasi Data Interaktif:

Jumlah Transaksi per Kategori: Mengukur popularitas/volume transaksi berdasarkan kategori produk.

Total Pendapatan (Revenue) per Kategori: Mengidentifikasi kategori produk yang menyumbang pendapatan tertinggi.

Heatmap Korelasi: Menganalisis tingkat hubungan antar variabel numerik (seperti Quantity, Price per Unit, dan Total Amount).

📁 Struktur Repositori

retail-sales-eda/
├── retail sales.csv        # Dataset utama transaksi ritel
├── eda_retail_sales.py     # Script Python untuk EDA dan Visualisasi
├── requirements.txt        # Daftar library/dependensi yang dibutuhkan
└── README.md               # Dokumentasi proyek


🛠️ Prasyarat & Instalasi

1. Library yang Dibutuhkan

Pastikan Python 3.x telah terinstal di komputer Anda. Library yang digunakan meliputi:

pandas

numpy

matplotlib

seaborn

2. Cara Menginstal Dependensi

Buka Terminal / Command Prompt, lalu jalankan perintah berikut:

pip install pandas numpy matplotlib seaborn


💻 Cara Menjalankan Program

Clone / Download Repositori Ini:

git clone https://github.com/username/retail-sales-eda.git
cd retail-sales-eda


Pastikan File Dataset Berada di Folder yang Sama:
Pastikan file retail sales.csv berada di direktori yang sama dengan skrip Python Anda.

Jalankan Skrip Python:

python eda_retail_sales.py


📊 Hasil & Visualisasi

Skrip akan secara otomatis menampilkan 3 grafik visualisasi utama:

Countplot: Distribusi frekuensi transaksi tiap kategori produk.

Barplot: Total pendapatan (Total Amount) berdasarkan kategori produk terlaris.

Correlation Heatmap: Peta korelasi variabel numerik.

👨‍💻 Kontribusi & Lisensi

Proyek ini terbuka untuk pengembangan lebih lanjut. Anda bebas melakukan fork, menambahkan teknik pemodelan (Predictive Analytics / Machine Learning), atau memperbaiki visualisasi.

Dikembangkan untuk keperluan Analisis Data & Exploratory Data Analysis (EDA).
