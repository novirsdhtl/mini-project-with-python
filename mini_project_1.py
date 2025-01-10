# **Program sederhana terkait perhitungan kasir dalam penjualan buah**

print("PROGRAM PENJUALAN BUAH")
print("----------------------")

# Buat menu yang ditawarkan
print("Daftar Harga Buah")

nama_buah = ["Mangga", "Apel", "Anggur", "Jeruk"]
harga_buah = [15000, 30000, 25000, 10000] # Harga dalam satu kilogram
for nama in nama_buah:
  print(f"Buah", nama, "\t: Rp.",harga_buah[nama_buah.index(nama)])

def beli_buah():
  total_harga = 0
  while True:
    pilihan = input("\nBuah apa yang ingin dibeli : ")
    if pilihan in nama_buah:
      jumlah = float(input("Masukkan jumlah Kg yang Anda inginkan : "))
      harga = nama_buah.index(pilihan)
      total_harga += harga_buah[harga] * jumlah
    else:
      print("Buah yang Anda inginkan tidak tersedia.")
      continue

    lanjut = input("\nApakah Anda ingin membeli buah yang lain? (y/n) : ").lower()
    if lanjut == "y":
      continue
    else:
      print(f"\nTotal harga yang harus Anda bayarkan sejumlah Rp.{int(total_harga)}")
      break

beli_buah()
