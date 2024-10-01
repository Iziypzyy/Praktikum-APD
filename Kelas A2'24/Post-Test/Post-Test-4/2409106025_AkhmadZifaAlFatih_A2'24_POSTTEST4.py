username = "zifa"
password = "25" 
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    print("=== Silakan untuk Login terlebih dahulu ===")
    masukkan_username = input("Masukkan username: ")
    masukkan_password = input("Masukkan password: ")

    if masukkan_username == username and masukkan_password == password:
        print("Login berhasil! Selamat datang.")
        while True:
            print("===masukkan data pinjaman===")
            Nama = input("Masukkan Nama = ")
            Nim = int(input("Masukkan Nim = "))
            Jumlah_Pinjaman = int(input("Masukkan Jumlah Pinjaman = "))
            tahun_cicilan = int(input("Masukkan lama cicilan (1/2/3) = "))

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

            print(f"""{Nama} dengan NIM {Nim} 
                harus membayar cicilan sebesar Rp.{cicilan_bulan:.0f} 
                setiap bulan setelah ditambahkan dengan bunga""")

            angka = int(input("Masukkan angka positif jika ingin lanjut (input negatif untuk berhenti): "))
            if angka < 0:
                exit()
    else:
        percobaan += 1
        print(f"Username atau Password anda salah!, silakan coba lagi, kesempatan anda tersisa {percobaan - max_percobaan}") 
        if percobaan == max_percobaan:
            print("Anda sudah mencoba sebanyak 3 kali, periksa kembali Username dan Password anda!")