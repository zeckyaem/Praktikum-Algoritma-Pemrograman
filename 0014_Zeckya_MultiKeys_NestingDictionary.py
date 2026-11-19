import datetime
import os
import string
import random

# Template dictionary buku
buku_template = {
    'judul': 'judul buku',
    'penulis': 'nama penulis',
    'tahun_terbit': 0000,
    'tanggal_pinjam': datetime.datetime(1111, 1, 11),
    'status': 'TERSEDIA'
}

data_buku = {}

while True:
    os.system("cls")  # Menggunakan cls untuk Windows
    print(f"{'SELAMAT DATANG':^30}")
    print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^30}")
    print("-" * 30)

    # Membuat dictionary buku baru dari template
    buku = dict.fromkeys(buku_template.keys())
    buku['judul'] = input("Judul Buku: ")
    buku['penulis'] = input("Penulis: ")
    buku['tahun_terbit'] = int(input("Tahun Terbit (YYYY): "))
    
    print("Masukkan Tanggal Terakhir Pinjam:")
    TAHUN_PINJAM = int(input("  Tahun (YYYY): "))
    BULAN_PINJAM = int(input("  Bulan (1-12): "))
    TANGGAL_PINJAM = int(input("  Tanggal (1-31): "))
    buku['tanggal_pinjam'] = datetime.datetime(TAHUN_PINJAM, BULAN_PINJAM, TANGGAL_PINJAM)
    
    buku['status'] = input("Status (TERSEDIA / TIDAK): ").upper()

    # Membuat 6 huruf kapital acak sebagai KEYS
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_buku.update({KEY: buku})

    # Menampilkan Header Tabel
    print(f"\n{'KEYS':<8} {'JUDUL BUKU':<22} {'PENULIS':<18} {'TAHUN':<8} {'TGL PINJAM':<14} {'STATUS':<10}")
    print('-' * 85)

    # Menampilkan isi data_buku ke dalam tabel
    for buku_key in data_buku:
        KEY = buku_key

        JUDUL = data_buku[KEY]['judul']
        PENULIS = data_buku[KEY]['penulis']
        TAHUN = data_buku[KEY]['tahun_terbit']
        TGL_PINJAM = data_buku[KEY]['tanggal_pinjam'].strftime("%x")
        STATUS = data_buku[KEY]['status']

        print(f"{KEY:<8} {JUDUL:<22} {PENULIS:<18} {TAHUN:^8} {TGL_PINJAM:^14} {STATUS:<10}")

    print("\n")
    is_done = input("Mau tambah buku lagi (y/n)? ").lower()
    if is_done == "n":
        break

print("\nProgram selesai, terima kasih!")