# nama = ["celio", "shandy", "farel", "ghazali", "vito"]

#membuat dan menampilkan list
# print("sebelum: ")
# print(nama)
# print("")
# print("sesudah: ")

#menimpa list
# nama.insert(2,"afrizal")
# print(nama)
# nama[4]= "fufufafa"

#menghapus list
# del nama[2]

#memindahkan list
# hapus= nama.pop(2)
# print(nama)
# print(hapus)

#slice list
# print(nama(2:4))

# slicing list2
# nama = [
#     "",
#     "",
# ]
# start stop step
# print(nama[1:9:2])

# operasi list
# matkul = ["jarkom", "apd", "apl", "jarkom"]
# data = nama+matkul
# print(data)

#nested list
# data = ["farel", "celio", [1,2,["halo",23,2.3,True]]]
# print(data[2][2][::-1])

# matkul = [1,2,3,4[5,6,7[8,9]]]
# print ([4][3][1])

#perulangan dalam nested list
# matkul = [1,2,3,4,5,6,7,8,9]
# for i in matkul:
#     print(i,end="")

# matkul = [[1,2,3],[4,5,6],[7,8,9]]

# for i in matkul:
#     # print(i)
#     for j in i:
#         print(j)

#tuple
# nama = ('farel', 'vito', 'shandy', 'rijal')
# print(nama[1])

#tuple berurut
# mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")
# absen, prodi, nim, nama = mahasiswa
# print(nim)

print(
"""
======================
|   DATA MAHASISWA   |
======================
|   1. TAMBAH DATA   |
|   2. TAMPILKAN DATA|
|   3. UBAH DATA     |
|   4. HAPUS DATA    |
|   5. KELUAR        |
"""
)
data_mahasiswa = []
while True:
    pilih = int(input("PILIH : "))
    if pilih == 1:
        nama = input("NAMA : ")
        nim = input("NIM : ")
        kelas = input("KELAS : ")
        data_mahasiswa.append([nama,nim,kelas])
    elif pilih == 2:
        for data in data_mahasiswa:
            for i in range(len(data)):
                print(f"\n Data Mahasiswa ke-{i+1}\nNama : {data[i]}\nNIM{data[i+1]}\KELAS : {data[i+2]}")
    elif pilih == 3:
        nama_lama = input("Nama Baru")
        for i in rangr(len(data_mahasiswa)):
            if
    elif pilih == 4:
        nama_lama
    elif pilih == 5: