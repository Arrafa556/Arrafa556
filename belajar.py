
# Program Python Sederhana - Kalkulator
# Membuat program kalkulator dasar

def tambah(a, b):
    """Fungsi untuk menambah dua angka"""
    return a + b

def kurang(a, b):
    """Fungsi untuk mengurangi dua angka"""
    return a - b

def kali(a, b):
    """Fungsi untuk mengalikan dua angka"""
    return a * b

def bagi(a, b):
    """Fungsi untuk membagi dua angka"""
    if b == 0:
        return "Error: Tidak bisa dibagi dengan 0"
    return a / b

# Program utama
print("=" * 40)
print("    KALKULATOR SEDERHANA")
print("=" * 40)

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("\nPilih operasi:")
print("1. Tambah (+)")
print("2. Kurang (-)")
print("3. Kali (*)")
print("4. Bagi (/)")
print("5. Persen (%)")

pilihan = input("\nMasukkan pilihan (1/2/3/4/5): ")

if pilihan == "1":
    hasil = tambah(angka1, angka2)
    print(f"\n{angka1} + {angka2} = {hasil}")
elif pilihan == "2":
    hasil = kurang(angka1, angka2)
    print(f"\n{angka1} - {angka2} = {hasil}")
elif pilihan == "3":
    hasil = kali(angka1, angka2)
    print(f"\n{angka1} * {angka2} = {hasil}")
elif pilihan == "4":
    hasil = bagi(angka1, angka2)
    print(f"\n{angka1} / {angka2} = {hasil}")
elif pilihan == "5":
    hasil = persen(angka1, angka2)
    print(f"\n{angka1} % {angka2} = {hasil}")
    
else:print("\nPilihan tidak valid sialahkan pilih 1, 2, 3, 4")
print("\nTerima kasih telah menggunakan kalkulator sederhana ini! ")


    