#Program Perhitungan Nilai Siswa
print("===Program Perhitungan Nilai Siswa===")

#  1. input Data Siswa Dan Nilai 
nama = input("Masukan Nama Siswa:")
tugas = float(input("Mausukan nilai tugas (0-100): "))
uts = float(input("Masukan Nilai uts (0-100): "))
uas = float(input("Masukan  Nilai uas (0-100): "))

# 2. Perhitungan Nilai Akhir (Rata-Rata Berbobot)
#Bobot : Tugas 30%, UTS 35%, UAS 35%
Nilai_Akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

# 3. Menentukan Predikat/grade Mengunakan Percabangan
if Nilai_Akhir >= 85:
    grade = "A"
    keterangan = "Lulus Dengan Nilai Sempurna"
elif Nilai_Akhir >= 70:
    grade = "B"
    keterangan = "Lulus"
elif Nilai_Akhir >= 60:
    grade = "C"
    keterangan = "Lulus ,Dan Butuh Perbaikan"
else :
    grade = "D"
    keterangan = "Tidak Lulus"

# 4. Menampilkan Hasil 
print("\n--- Hasil Akhir  ---")
print(f"Nama Siswa  :  {nama}")
print(f"Nilai Akhir : {Nilai_Akhir:.2f}")
print(f"grade       :  {grade}")
print(f"keterangan  :  {keterangan}")
    

