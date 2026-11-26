def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def volume_persegi_panjang(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def luas_lingkaran(jari_jari):
    return 3.14 * (jari_jari ** 2)

def volume_bola(jari_jari):
    return (4 / 3) * 3.14 * (jari_jari ** 3)

print("a. Luas Persegi Panjang")
p = float(input("Masukkan panjang: "))
l = float(input("Masukkan lebar: "))
print(f"Luas persegi panjang = {luas_persegi_panjang(p, l)}\n")

print("b. Volume Persegi Panjang")
p_balok = float(input("Masukkan panjang: "))
l_balok = float(input("Masukkan lebar: "))
t_balok = float(input("Masukkan tinggi: "))
print(f"Volume persegi panjang = {volume_persegi_panjang(p_balok, l_balok, t_balok)}\n")

print("c. Luas Lingkaran")
r_lingkaran = float(input("Masukkan jari-jari: "))
print(f"Luas lingkaran = {luas_lingkaran(r_lingkaran)}\n")

print("d. Volume Bola")
r_bola = float(input("Masukkan jari-jari: "))
print(f"Volume bola = {volume_bola(r_bola)}")