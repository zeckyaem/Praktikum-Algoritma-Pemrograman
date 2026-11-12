# 1. 
# mahasiswa = ("Zeckya Eliya Muhammad", 2605060014, "Teknologi Informasi")
# print(mahasiswa[1])
# print(mahasiswa[2])
# mahasiswa[2] = "Teknologi Informasi"  
# nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
# print(nilai_angka) 

# 2.
# data_mahasiswa = {
#     "nim": 2605060014,
#     "nama": "Zeckya Eliya Muhammad",
#     "prodi": "Teknologi Informasi"
# }

# data_mahasiswa["prodi"] = "Sastra Mesin"
# data_mahasiswa.update({"angkatan": 2026})
# print(data_mahasiswa)

# 3.
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}

total_belanja = 0
for buah, harga in keranjang.items():
    print(f"Harga {buah}: Rp {harga}")
    total_belanja += harga

print(f"Total belanja: Rp {total_belanja}")