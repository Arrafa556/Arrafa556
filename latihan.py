def tampilkan_menu():
    """Menampilkan menu pilihan pengguna."""
    print("\n=== APLIKASI TO-DO LIST ===")
    print("1. Tambah tugas")
    print("2. Lihat semua tugas")
    print("3. Hapus tugas")
    print("4. Alasan tugas")
    print("5. Keluar")

def tambah_tugas(tugas_list):
    """Menambahkan tugas baru ke daftar."""
    tugas = input("Masukkan tugas baru: ").strip()
    if tugas:
        tugas_list.append(tugas)
        print(f"Tugas '{tugas}' berhasil ditambahkan.")
    else:
        print("Tugas tidak boleh kosong.")

def lihat_tugas(tugas_list):
    """Menampilkan semua tugas yang tersimpan."""
    if not tugas_list:
        print("Belum ada tugas.")
    else:
        print("\nDaftar Tugas:")
        for index, tugas in enumerate(tugas_list, start=1):
            print(f"{index}. {tugas}")

def hapus_tugas(tugas_list):
    """Menghapus tugas berdasarkan nomor."""
    if not tugas_list:
        print("Tidak ada tugas untuk dihapus.")
        return

def alasan_tugas(tugas_list):
    """menampilkan alasan tugas."""
    print("\nAlasan Tugas:")
    print("Alasan mengapa tugas penting:")
    for i in range(1, 6):
        print(f"{i}. Alasan tugas {i}")

    lihat_tugas(tugas_list)
    angka = input("Masukkan nomor tugas yang ingin dihapus: ").strip()
    if not angka.isdigit():
        print("Masukkan angka yang valid.")
        return

    nomor = int(angka)
    if 1 <= nomor <= len(tugas_list):
        tugas_terhapus = tugas_list.pop(nomor - 1)
        print(f"Tugas '{tugas_terhapus}' berhasil dihapus.")
    else:
        print("Nomor tugas tidak valid.")

def alasan_tugas(tugas_list):
    """Menampilkan alasan tugas."""
    print("\nAlasan Tugas:")
    for i in range(1, 6):
        print(f"{i}. Alasan tugas {i}")

def main():
    """Fungsi utama yang menjalankan aplikasi."""
    tugas_list = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu [1-5]: ").strip()

        if pilihan == "1":
            tambah_tugas(tugas_list)
        elif pilihan == "2":
            lihat_tugas(tugas_list)
        elif pilihan == "3":
            hapus_tugas(tugas_list)
        elif pilihan == "4":
            alasan_tugas(tugas_list)
        elif pilihan == "5":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak dikenal. Silakan pilih 1-5.")

if __name__ == "__main__":
    main()