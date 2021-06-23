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
        self.jmlMenang = 0
    
    def menang(self, nilai):
        self.jmlMenang += nilai
    
    def aksi(self):
        self.aksiDipilih = Jari()

    # def kalah():
    #     self.jmlMenang +=0

def langkahPemain():
    jariTersedia = [f"{i.name}[{i.value}]" for i in Jari]
    pilihan = ", ".join(jariTersedia)
    ambilPilihan = int(input(f"Pilih salah satu ({pilihan}): "))
    if ambilPilihan in Jari._value2member_map_:
      pilihanPemain = Jari(ambilPilihan)
      return pilihanPemain 
    print("Angka salah")
    # pilihanPemain = Jari(ambilPilihan)
    return pilihanPemain

def langkahBot():
    ambilPilihan = random.randint(0,len(Jari)-1)
    pilihanBot = Jari(ambilPilihan)
    return pilihanBot

def suit(pemain_1,pemain_2):
    if pemain_1 == pemain_2:
        print ("Hasilnya seriiii....!!!")
    elif pemain_1 == Jari.gunting:
        if pemain_2 == Jari.kertas:
            print ("Pemain 1 menang ")
        else:
            print ("Pemain 2 menang")
    elif pemain_1 == Jari.batu:
        if pemain_2 == Jari.gunting:
            print ("Pemain 1 menang ")
        else:
            print ("Pemain 2 menang")
    elif pemain_1 == Jari.kertas:
        if pemain_2 == Jari.batu:
            print ("Pemain 1 menang ")
        else:
            print ("Pemain 2 menang")

babak = int(input("Berapa babak yang diinginkan? " ))
tipe = int(input("Pemain tunggal[0] atau ganda[1] ? "))

if tipe == 0:
    inputPemain_1 = str(input("Masukkan nama pemain: "))
    pemain_1 = Pemain(inputPemain_1)
    pemain_2 = Pemain()
    for a in range (babak):
        print("Babak : ", a+1)
        print(pemain_1.nama)
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
        print(pemain_1.nama)
        pemain_1.aksi = langkahPemain()
        print(pemain_2.nama)
        pemain_2.aksi = langkahPemain()
        suit(pemain_1.aksi,pemain_2.aksi)
else:
    print("Anda salah memasukkan input")


    
    
