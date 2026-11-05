# 1
kendaraan = ["motor", "mobil", "sepeda", "bus"]
# menambahkan 'truk' di akhir list
kendaraan.append("truk")
print(kendaraan)
# sisipkan 'becak' di index ke 1
kendaraan.insert(1, "becak")
print(kendaraan)
# hapus data yang berada di paling akhir list
kendaraan.pop()
print(kendaraan)
# ubah elemen 'sepeda' menjadi 'skuter'
kendaraan[3] = "skuter"
print(kendaraan)
# Tampilkan informasi jumlah total data yang ada di list kendaraan
print("Jumlah data dalam list kendaraan:", len(kendaraan))

# 2
angka = [75, 80, 90, 75, 85, 100, 65]
# Cari tahu di indeks berapa skor 100 berada
index_100 = angka.index(100)
print("Indeks skor 100:", index_100)
# hitung ada  berapa banyak siswa yang mendapatkan skor 75
jumlah_75 = angka.count(75)
print("Jumlah siswa dengan skor 75:", jumlah_75)
# Urutkan skor dari yang terkecil ke yang terbesar
angka.sort()
print("Skor setelah diurutkan:", angka)
# Balikkan urutaan skor yang sudah diurutkan sehingga menjadi dari yang terbesar ke yang terkecil
angka.sort(reverse=True)
print("Skor setelah dibalik:", angka)

# 3
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

# Gabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi, kemudian tampilkan hasil dari gabungan tersebut
menu_utama.extend(menu_tambahan)
print("Menu utama setelah ditambahkan menu tambahan:", menu_utama)

# 4
data_barang = [ ["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000] ]
# a
print("Harga Pensil:", data_barang[1][1])
# b
for barang in data_barang:
    nama = barang[0]
    harga = barang[1]
    print(f"Nama: {nama}\t\tHarga: {harga}")