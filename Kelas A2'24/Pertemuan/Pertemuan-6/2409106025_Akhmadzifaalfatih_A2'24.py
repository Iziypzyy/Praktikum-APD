#contoh 1
#  daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])
#value boleh sama tapi key ga boleh sama, kalau key sama ketimpa

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#     "Instagram" : "@aldyrmdhns_",
#     "Discord" : "\'Izanami#6848"
#     }
# }

# print(Biodata["KRS"][1])
# #dictinory of list
# print(Biodata["Social Media"])
# #dictinary...
# print(Biodata.get('KRS'))

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
#     }

# #tanpa menggunakan items
# for i in Nilai:
#     print(i)
# print("")
# #menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

#MENAMBAH ITEM
# print["Fisika"] = 100
# # contoh 1
# daftar_buku = {
#     "Buku1" : "Harry Potter",
#     "Buku2" : "Percy Jackson",
#     "Buku3" : "Twillight"
# }

# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# # contoh 2
# daftar_buku = {}

# daftar_buku["Buku1"] = "Harry Potter"
# daftar_buku["Buku2"] = "Percy Jackson"
# daftar_buku["Buku3"] = "Twillight"

# print(daftar_buku)

# # contoh 3
# musik = {
#     "judul" : "All we Know",
#     "judu2" : "Something Just Like This"
# }

# print(musik["judul"])
# print(musik["judu2"])

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#     }
# }

# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"NIM Saya adalah {Biodata['NIM']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#     }
# }

# print(Biodata.get('Nama'))
# print(Biodata.get('Alamat'))
# print(Biodata.get('Alamat', 'Key tersebut tidak ada'))

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# # #tanpa menggunakan items
# # for i in Nilai:
# #     print(i)
# # print("")
# #menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }

# #Sebelum Ditambah
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})

# #Setelah Ditambah
# print(Film)

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Diubah
# print(Film)
# Film["Sherlock Holmes"] = "Action"
# Film.update({"The Conjuring" : "Tragedy"})
# #Setelah diubah
# print(Film)

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }
# print(Nilai)

# Nilai.update({"Matematika" : 90})
# print(Nilai)

# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# cache = data.pop("Nama")
# #Setelah dihapus
# print(data)
# #memanggil data yang telah dihapus pada dictionary
# print(data.get("Nama"))
# #memanggil data yang telah dihapus pada variabel cache
# print(cache)

# data = {
#     "Nama" : "Aldy",
#     "Umur" : 19,
#     "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# data.clear()
# #Setelah dihapus
# print(data)

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# print("jumlah data = ", len(Nilai))

# Buku = {
#     "No Longer Human" : "Osamu Dazai",
#     "Harry Potter" : "J.K. Rowlings",
#     "Hamlet" : "William Shakespeare"
# }

# pinjam = Buku.copy()
# print("Dictionary yang Telah Disalin : ", pinjam)

# key = "apel", "jeruk", "mangga"
# value = 1

# buah = dict.fromkeys(key, value)

# print(buah)

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# #menggunakan keys
# for i in Nilai.keys():
#     print(i)

# print("")
# #menggunakan value
# for i in Nilai.values():
#     print(i)

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")

# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")

# #setelah menggunakan setdefault
# print(Nilai)

# Musik = {
#     "The Chainsmoker" : ["All we Know", "TheParis"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
# for song in j:
#     print(song)
# print("")

# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
#     print("")

# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# #Sebelum Dilakukan Perubahan
# print(mahasiswa)

# #Menambahkan Item pada Nested Dictionary
# mahasiswa[101]["Angkatan"] = 2023
# print(mahasiswa)

# #Mengubah Item pada Nested Dictionary
# mahasiswa[101]["Nama"] = "Rizal"
# print(mahasiswa)

# #Menghapus Item pada Nested Dictionary
# del mahasiswa[101]["Umur"]
# print(mahasiswa)

# mahasiswa = {
# 25 : {"Nama" : "Rasyid",  "Umur" : 19, "Nim" : 25, "Jurusan" : "Informatika", "Angkatan" : 34},
# }
#Menambahkan Item pada Nested Dictionary
# mahasiswa[25]["Jenis Kelamin"] = "Pria"
# print(mahasiswa)

#Mengubah Item pada Nested Dictionary
# mahasiswa[25]["Nama"] = "Zifa"
# print(mahasiswa)

#Menghapus Item pada Nested Dictionary
# del mahasiswa[25]["Angkatan"]
# print(mahasiswa)
#Studkas 1

# batagor = {
#     'Matematika' : 90,
#     'Fisika' : 80,
#     'Biologi': 80,
#     'Kimia' : 70
# }

# total = sum(batagor.values())
# print("Nilai total : ", total)
# rata = total / len(batagor)
# print("Nilai rata-rata : ",rata)
#Studkas 2