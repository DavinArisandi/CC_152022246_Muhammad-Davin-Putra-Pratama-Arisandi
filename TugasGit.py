import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.

# Fungsi lambda untuk menghitung gaji setelah peningkatan 5%
peningkatan_5persen = lambda gaji: gaji + (gaji * 0.05)

# Loop for untuk menghitung dan menyimpan gaji setelah peningkatan 5%
for index, row in df.iterrows():
    df.at[index, 'Gaji_5%'] = peningkatan_5persen(row['Gaji'])

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.

# DataFrame Setelah Perubahan
print(f"==================================================")
print(f"DataFrame Setelah Peningkatan Gaji Sebesar 5%")
print(df)
print(f"==================================================")

# Ringkasan perubahan
print(f"Ringkasan Perubahan:")
print(f"Kolom 'Gaji_5%' adalah peningkatan gaji sebesar 5% dari gaji utama.")
print(f"==================================================")

# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

# Fungsi lambda untuk menghitung gaji setelah peningkatan tambahan 2% jika usia di atas 30 tahun
peningkatan_2persen = lambda gaji: gaji + (gaji * 0.02) if row['Usia'] > 30 else gaji

# Loop for untuk mengevaluasi karyawan yang usianya di atas 30 tahun
for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji_tambahan_2%'] = peningkatan_2persen(row['Gaji_5%'])
    else:
        df.at[index, 'Gaji_tambahan_2%'] = 0

# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
# DataFrame Setelah Perubahan
print(f"\n==================================================")
print(f"DataFrame Setelah Peningkatan 2% untuk usia diatas 30 tahun")
print(df)
print(f"==================================================")

# Ringkasan perubahan
print(f"Ringkasan Perubahan:")
print(f"Kolom 'Gaji_tambahan_2%' adalah peningkatan gaji sebesar 2% dari kolom 'Gaji_5%' untuk yang usianya diatas 30 tahun.")
print(f"==================================================")

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.