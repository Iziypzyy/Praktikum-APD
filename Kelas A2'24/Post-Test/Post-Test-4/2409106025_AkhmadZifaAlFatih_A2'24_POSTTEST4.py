#Menambah fitur login, user menginput username atau password
#pertama saya menggunakan tipe list data dictionary untuk memanggil kembali.




username = "zifa"
password = "25" 
percobaan = 0
max_percobaan = 3

print("=== Silakan untuk Login terlebih dahulu ===")
masukkan_username = input("Masukkan username: ")
masukkan_password = input("Masukkan password: ")

while percobaan > max_percobaan:
    if masukkan_username == username:
        print("Login berhasil! Selamat datang.") 
    if masukkan_password == password :
        print("Login berhasil! Selamat datang.")
        break 
    else:
        percobaan += 1
        print(f"Username atau Password anda salah!, silakan coba lagi, kesempatan anda tersisa {percobaan - max_percobaan}") 

if percobaan == max_percobaan:
    print("Anda sudah mencoba sebanyak 3 kali, periksa kembali Username dan Password anda!")