#kalkulator sederhana by bang sandy
fitur = int(input("pilih fitur : "))
match fitur :
    case 1:
        a = int(input("Masukkan angka 1 : "))
        b = int(input("Masukkan angka 2 : "))
        c = a + b 
        print (f"hasil penjumlahan angka 1 dan angka 2 adalah {c}")
    case 2:
        a = int(input("Masukkan angka 1 : "))
        b = int(input("Masukkan angka 2 : "))
        c = a - b 
        print (f"hasil pengurangan angka 1 dan angka 2 adalah {c}")
    case 3:
        a = int(input("Masukkan angka 1 : "))
        b = int(input("Masukkan angka 2 : "))
        c = a * b 
        print (f"hasil perkalian angka 1 dan angka 2 adalah {c}")
    case 4:
        a = int(input("Masukkan angka 1 : "))
        b = int(input("Masukkan angka 2 : "))
        c = a / b 
        print (f"hasil pembagian angka 1 dan angka 2 adalah {c}")

#studi kasus 1
harga = int(input("Masukkan harga barang = "))
jumlah = int(input("Masukkan jumlah barang = "))
diskon = 0.20
harga_total = harga * jumlah


if harga_total > 100000 and jumlah >= 5:
    diskon_barang = harga_total* diskon
    harga_diskon = harga_total - diskon_barang
    print(f"{harga_diskon:.0f}")
else: 
    print("Anda tidak mendapat diskon")

#studi kasus 2
jenis_kelamin = input("Masukkan jenis kelamin anda (L/P) :")

hasil = "Jenis Kelamin Laki-Laki" if jenis_kelamin == "L" else "Jenis Kelamin Perempuan" if jenis_kelamin == "P" else "Jenis Kelamin Tidak Diketahui"

print(hasil)

#Nested If
Nilai = int(input("Masukkan Nilai="))
if Nilai > 100 :
    print("kondisi tidak memenuhi syarat")
if Nilai >= 80 : 
    if Nilai >= 90 and Nilai <= 100 :
        print("Nilai anda A+")
    if Nilai >= 80 and Nilai <= 89 :
        print("Nilai anda A-")
if Nilai >= 70 : 
    if Nilai >= 75 and Nilai <= 79 :
        print("Nilai anda B+")
    if Nilai >= 70 and Nilai <= 74 :
        print("Nilai anda B-")
else :
    print("kondisi tidak memenuhi syarat")


