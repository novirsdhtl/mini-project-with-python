# **Program Sederhana Perhitungan Nilai**

print("Seleksi Penerimaan Calon Karyawan")
print("=================================")

nama = input("Masukkan Nama Karyawan : ")
tes_CAT = int(input("Masukkan nilai tes CAT : "))
wawancara = input("Masukkan nilai tes wawancara : ")

if tes_CAT >= 85 and wawancara == "Bagus":
  print(f"\nSelamat {nama}, Anda berhasil LOLOS SELEKSI")
else:
  print(f"\nMohon maaf {nama}, Anda BELUM BERHASIL LOLOS SELEKSI")
