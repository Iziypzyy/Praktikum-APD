Nama = input("Masukkan Nama = ")
Nim = int(input("Masukkan Nim = "))
Jumlah_Pinjaman = int(input("Masukkan Jumlah Pinjaman = "))
tahun_cicilan = int(input("Masukkan lama cicilan = "))

jumlah_bulan = tahun_cicilan * 12
Bunga = {
    "Bunga1" : 0.7,
    "Bunga2" : 0.13,
    "Bunga3" : 0.19
}

if tahun_cicilan == 1:
    bunga = (Bunga["Bunga1"]/12) * Jumlah_Pinjaman
    cicilan_bulan = (Jumlah_Pinjaman + bunga) / jumlah_bulan
elif tahun_cicilan == 2:
    bunga = (Bunga["Bunga2"]/12) * Jumlah_Pinjaman
    cicilan_bulan = (Jumlah_Pinjaman + bunga) / jumlah_bulan
elif tahun_cicilan == 3:
    bunga = (Bunga["Bunga2"]/12) * Jumlah_Pinjaman
    cicilan_bulan = (Jumlah_Pinjaman + bunga) / jumlah_bulan
else:
    print("Input tidak sesuai dengan persyaratan yang ditentukan!")

print(f"{Nama} dengan NIM {Nim} harus membayar cicilan sebesar Rp.{cicilan_bulan:.0f} setiap bulan setelah ditambahkan dengan bunga")

