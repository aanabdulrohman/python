print ("hello")
print (1)

#aritmatika
angka_1 = (1)
angka_2 = (2)
print (angka_1 + angka_2)

# input1
print("Masukan nama depan kamu!")
namaDepan = input()
print("Masukan nama belakang!")
namaBelakang = input()
print (f"ini nama saya {namaDepan} {namaBelakang}")

# input2
print("Masukan angka pertama")
angkaPertama = int(input())
print("Masukan angka kedua")
angkaKedua = int(input())
hasil = angkaPertama + angkaKedua
print(f"Hasil penjumlahan {angkaPertama} dan {angkaKedua} adalah {hasil}")

# if
cewe = 2
cowo = 2
if cewe < cowo:
    print("cewenya kurang nih")
if cewe > cowo:
    print("cewenya kebanyakan nih")
if cewe == cowo:
    print("cewenya pas nih")
if cowo < cewe:
    print("cowonya kurang nih")
if cowo > cewe:
    print("cowonya kebanyakan nih")
if cowo == cewe:
    print("cowonya pas nih")

# if else
juara = True  

if juara:
    print("Selamat, anda menang!")
else:
    print("Maaf, anda kalah!")

pilihKendaraan = input("Silahkan pilih mobil, motor atau sepeda :")
if pilihKendaraan == "mobil":
    print("Anda memilih mobil!")
elif pilihKendaraan == "motor":
    print("Anda memilih motor!")
elif pilihKendaraan == "sepeda":
    print("Anda memilih sepeda!")
else:
    print("Jenis kendaraan yang anda pilih salah!")