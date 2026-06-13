# program python sederhana -kalkulator 
# membuat program kalkulator dasar 

def tambah(x, y):
    """fungsi untuk menambahkan dua angka"""
    return x + y

def kurang(x, y):
    """fungsi untuk mengurangi dua angka"""
    return x - y

def kali(x, y):
    """fungsi untuk mengkalikan dua angka"""
    return x * y

def bagi(x, y):
    """fungsi untuk membagi untuk dua angka"""
    if y == 0:
        return "error: pembagian dengan nol tidak diperbolehkan"
    return x / y

#program utama
print("=" * 40)
print("KALKULATOR SEDERHANA")
print("=" * 40)

angka1 = float(input("Masukan angka pertama: "))
angka2 = float(input("masukan angka kedua:  "))

print("\nPilih operasi yang diinginkan :")
print("1. tambah (+)")
print("2. kurang (-)")
print("3. kali (*)")
print("4. bagi (/)")

pilihan = input("masukan pilihan (1/2/3/4): ")

if pilihan == '1':
     hasil = tambah(angka1, angka2)
     print(f"\n{angka1} + {angka2} = {hasil}")
elif pilihan == '2':
    hasil  = kurang(angka1, angka2)
    print(f"\n{angka1} - {angka2} = {hasil}")
elif pilihan == '3':
    hasil = kali(angka1, angka2)
    print(f"\n{angka1} * {angka2} = {hasil}")
elif pilihan == '4':
    hasil = bagi(angka1, angka2)
    print(f"\n{angka1} / {angka2} = {hasil}")

else:  print("pilihan tidak valid, silakan pilih 1, 2, 3, 4")
print("\nTerima kasih telah menggunakan kalkulator sederhana ini!")

