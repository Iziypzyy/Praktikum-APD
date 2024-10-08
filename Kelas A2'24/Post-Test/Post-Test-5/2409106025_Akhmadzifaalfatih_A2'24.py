print(
"""
==============================
|  Data Penjualan Ikan Hias  |
==============================
|   1. TAMBAH IKAN HIAS      |
|   2. TAMPILKAN SEMUA IKAN  |      
|   3. UPDATE IKAN HIAS      |
|   4. HAPUS DATA IKAN HIAS  |
|   5. KELUAR                |
==============================
"""
)

penjualan_ikanhias = []
while True:
    pilih = int(input("\npilih menu data (1-5): "))
    
    if pilih == 1:
        jenis_ikanhias = input("Jenis Ikan Hias: ")
        harga_ikanhias = int(input("Harga Ikan Hias: "))
        stok_ikanhias = int(input("Stok yang tersedia: "))
        penjualan_ikanhias.append([jenis_ikanhias,harga_ikanhias,stok_ikanhias])
        print("\nIkan Hias Telah Ditambahkan.")

    elif pilih == 2:
        if not penjualan_ikanhias:
            print("Data Ikan Hias tidak ditemukan.")
        else:
            print("\nData Ikan Hias.")
            for i in range(len(penjualan_ikanhias)):
                print(f"\nData Ikan Hias: {i+1}\nJENIS: {penjualan_ikanhias[i][0]}\nHARGA: {penjualan_ikanhias[i][1]}\nSTOK: {penjualan_ikanhias[i][2]}")

    elif pilih == 3:
        if not penjualan_ikanhias:
            print("Tidak ada data Ikan Hias yang diupdate.")

        else:
            print("\nData Ikan Hias:")
            ikanlama = input("Jenis Ikan Yang Ingin Diupdate: ")
            for i in range(len(penjualan_ikanhias)):
                print(f"Data Ikan Hias: {i+1}, NAMA: {penjualan_ikanhias[0]}")
            if penjualan_ikanhias[i][0] == ikanlama:
                jenis_ikanbaru = input("Jenis Baru: ")
                harga_ikanbaru = input("Harga Baru: ")
                stok_ikanbaru = input("Stok baru: ")
                penjualan_ikanhias[i][0] = jenis_ikanbaru
                penjualan_ikanhias[i][1] = harga_ikanbaru
                penjualan_ikanhias[i][2] = stok_ikanbaru

    elif pilih == 4:
        ikanlama = input("\nJenis Ikan Yang Ingin dihapus: ")
        if not penjualan_ikanhias:
            print("Tidak ada Data Ikan Hias yang dihapus.")
        else:
            print("\nData Ikan Hias:")
            for i in range(len(penjualan_ikanhias)):
                print(f"Data Ikan Hias: {i+1}, NAMA: {penjualan_ikanhias[0]}") 
            if penjualan_ikanhias[i][0] == ikanlama:
                penjualan_ikanhias.pop[ikanlama]

    elif pilih == 5:
        print("Terima Kasih telah mengakses Data Penjualan Ikan Hias")
        break

    else:
        print("Anda Salah Input.")