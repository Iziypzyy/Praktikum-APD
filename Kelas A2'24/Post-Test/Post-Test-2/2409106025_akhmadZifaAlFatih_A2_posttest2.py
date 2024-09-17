nama = input("Masukkan Nama = ")
nim = input("Masukkan Nim = ")
harga_beras = int(input("Masukkan harga beras = "))
diskon = {
    "diskon1" : 0.11,
    "diskon2" : 0.14,
    "diskon3" : 0.17
}
diskon_mawar = harga_beras * diskon["diskon1"]
diskon_sania = harga_beras * diskon["diskon2"]
diskon_maknyus = harga_beras * diskon["diskon3"]

mawar = harga_beras - diskon_mawar
sania = harga_beras - diskon_sania
maknyus = harga_beras - diskon_maknyus

print(f"{nama} dengan nim {nim} ingin membeli beras seharga {harga_beras} " "\n"
f" Jika dia membeli beras Mawar ia harus membayar {mawar} Setelah mendapat diskon 11%." "\n"
f" Jika dia membeli beras sania ia harus membayar {sania} Setelah mendapat diskon 14%." "\n"
f" Jika dia membeli beras maknyus ia harus membayar {maknyus} Setelah mendapat diskon 17%.")

