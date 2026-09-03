nama = "Zeckya Eliya Muhammad"
umur = 18
berat = 35.15

print("Nama\t:\t", nama)
print("Umur\t:\t", umur, "tahun")
print("Berat\t:\t", berat, "Kg")

angka_str = "123"
angka_float = 45.67
angka_int = 89

konversi_1 = int(angka_str)
konversi_2 = int(angka_float)
konversi_3 = float(angka_int)
konversi_4 = str(angka_int)

print(konversi_1, type(konversi_1))
print(konversi_2, type(konversi_2))
print(konversi_3, type(konversi_3))
print(konversi_4, type(konversi_4))

usia = int(input("Masukkan usia :"))
tinggi_badan = float(input("Masukkan tinggi badan :"))
nama = input("Masukkan nama :")

print("Nama\t\t:", nama, "type =", type(nama))
print("Usia\t\t:", usia, "type =", type(usia))
print("Tinggi Badan\t:", tinggi_badan, "type =", type(tinggi_badan))