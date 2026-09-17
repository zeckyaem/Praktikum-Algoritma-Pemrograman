masukkan = int(input("Masukkan Usia Anda: "))

if masukkan >= 0 and masukkan <= 12:
    print("Anak-anak")
elif masukkan >= 13 and masukkan <= 17:
    print("Remaja")
elif masukkan >= 18 and masukkan <= 59:
    print("Dewasa")
else:
    print("Lansia")
