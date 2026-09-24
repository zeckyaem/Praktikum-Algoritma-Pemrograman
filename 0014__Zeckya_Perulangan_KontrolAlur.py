print("Bilangan Ganjil dari 1 sampai 10")
for i in range(1, 51):
    if i % 2 == 1:
        print(i)

print("Bilangan Genap dari 1 sampai 10")
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

print("Bilangan Prima dari 1 sampai 100")
for angka in range(2, 101):
    for i in range(2, angka):
        if angka % i == 0:
            break
    else:
        print(angka)
    
