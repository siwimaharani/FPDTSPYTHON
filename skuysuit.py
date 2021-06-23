import random
from enum import IntEnum

print("Selamat Datang di Skuy Suit \nMari Kita Suit")

class Jari(IntEnum):
    gunting = 1
    batu = 2
    kertas = 3

class Pemain():
    def __init__(self, nama = "komputer"):
        self.nama = nama
        self.__jmlMenang = 0
    
    def menang(self, nilai):
        self.__jmlMenang += nilai
    
    def totalMenang(self):
        return self.__jmlMenang
    
    def aksi(self):
        self.aksiDipilih = Jari()

def langkahPemain():
    jariTersedia = [f"{i.name}[{i.value}]" for i in Jari]
    pilihan = ", ".join(jariTersedia)
    ambilPilihan = int(input(f"Pilih salah satu ({pilihan}): "))
    if ambilPilihan in range(1,4):
      pilihanPemain = Jari(ambilPilihan)
      return pilihanPemain 
    print("Angka salah")
    return langkahPemain()

def langkahBot():
    ambilPilihan = random.randint(1,len(Jari))
    pilihanBot = Jari(ambilPilihan)
    return pilihanBot

def suit(suit_1,suit_2):
    if suit_1 == suit_2:
        print(pemain_1.nama,pemain_2.nama,sep=" dan ")
        print ("Hasilnya seriiii....!!!")
    elif suit_1 == Jari.gunting:
        if suit_2 == Jari.kertas:
            pemain_1.menang(1)
            print ("Yang menang : ",pemain_1.nama)
        else:
            pemain_2.menang(1)
            print ("Yang menang : ",pemain_2.nama)
    elif suit_1 == Jari.batu:
        if suit_2 == Jari.gunting:
            pemain_1.menang(1)
            print ("Yang menang : ",pemain_1.nama)
        else:
            pemain_2.menang(1)
            print ("Yang menang : ",pemain_2.nama)
    elif suit_1 == Jari.kertas:
        if suit_2 == Jari.batu:
            pemain_1.menang(1)
            print ("Yang menang : ",pemain_1.nama)
        else:
            pemain_2.menang(1)
            print ("Yang menang : ",pemain_2.nama)

babak = int(input("Berapa babak yang diinginkan? " ))
tipe = int(input("Pemain tunggal[0] atau ganda[1] ? "))

if tipe == 0:
    inputPemain_1 = str(input("Masukkan nama pemain: "))
    pemain_1 = Pemain(inputPemain_1)
    pemain_2 = Pemain()
    for a in range (babak):
        print("Babak : ", a+1)
        print(pemain_1.nama, end=" ")
        pemain_1.aksi = langkahPemain()
        pemain_2.aksi = langkahBot()
        suit(pemain_1.aksi,pemain_2.aksi)
elif tipe == 1:
    inputPemain_1 = str(input("Masukkan nama pemain 1: "))
    inputPemain_2 = str(input("Masukkan nama pemain 2: "))
    pemain_1 = Pemain(inputPemain_1)
    pemain_2 = Pemain(inputPemain_2)
    for b in range(babak):
        print("Babak : ", b+1)
        print(pemain_1.nama, end=" ")
        pemain_1.aksi = langkahPemain()
        print(pemain_2.nama, end=" ")
        pemain_2.aksi = langkahPemain()
        suit(pemain_1.aksi,pemain_2.aksi)
else:
    print("Anda salah memasukkan input")

print("\n\n")
print("======= TOTAL MENANG =======")
print("total menang ({pemain_1.nama}) : ",pemain_1.totalMenang())
print("total menang ({pemain_2.nama}) : ",pemain_2.totalMenang())
print("\n")
print("======= PEMENANG AKHIR =======")
if pemain_1.totalMenang() > pemain_2.totalMenang():
    pemenang = pemain_1.nama
    print(pemenang.upper())
else:
    pemenang = pemain_2.nama
    print(pemenang.upper())


    
    
