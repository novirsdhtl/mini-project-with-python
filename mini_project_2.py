# -*- coding: utf-8 -*-
"""Mini_Project_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sxvt93mF2FhkM11IDKbHfnLl1aL5a5Rq

# **Program Sederhana Perhitungan Nilai**
"""

print("Seleksi Penerimaan Calon Karyawan")
print("=================================")

nama = input("Masukkan Nama Karyawan : ")
tes_CAT = int(input("Masukkan nilai tes CAT : "))
wawancara = input("Masukkan nilai tes wawancara : ")

if tes_CAT >= 85 and wawancara == "Bagus":
  print(f"\nSelamat {nama}, Anda berhasil LOLOS SELEKSI")
else:
  print(f"\nMohon maaf {nama}, Anda BELUM BERHASIL LOLOS SELEKSI")