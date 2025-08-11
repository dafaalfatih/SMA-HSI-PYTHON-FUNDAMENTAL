# --------------------
# Latihan 1: Membuat Log Sederhana
# --------------------
def log_kegiatan():
    with open("log_kegiatan.txt", "a", encoding="utf-8") as file:
        kegiatan = input("Masukkan kegiatan yang baru saja dilakukan: ")
        file.write(kegiatan + "\n")
    print(" Kegiatan berhasil dicatat di log_kegiatan.txt")

# --------------------
# Latihan 2: Salin File
# --------------------
def salin_file():
    sumber = "sumber.txt"
    tujuan = "salinan.txt"

    # Pastikan sumber.txt ada dulu
    if not os.path.exists(sumber):
        print(f" File {sumber} tidak ditemukan! Silakan buat file tersebut terlebih dahulu.")
        return

    with open(sumber, "r", encoding="utf-8") as file_sumber:
        isi = file_sumber.read()

    with open(tujuan, "w", encoding="utf-8") as file_tujuan:
        file_tujuan.write(isi)

    print(f" Isi file '{sumber}' berhasil disalin ke '{tujuan}'.")

# --------------------
# Latihan 3: Hapus File dengan Aman
# --------------------
def hapus_file():
    nama_file = input("Masukkan nama file yang ingin dihapus: ")

    if os.path.exists(nama_file):
        konfirmasi = input(f"Anda yakin ingin menghapus '{nama_file}'? (y/n): ").lower()
        if konfirmasi == "y":
            os.remove(nama_file)
            print(f" File '{nama_file}' berhasil dihapus.")
        else:
            print(" Penghapusan dibatalkan.")
    else:
        print(f" File '{nama_file}' tidak ditemukan.")

# --------------------
# Menu Program
# --------------------
while True:
    print("\n=== MENU PROGRAM ===")
    print("1. Tambah log kegiatan")
    print("2. Salin file")
    print("3. Hapus file dengan aman")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        log_kegiatan()
    elif pilihan == "2":
        salin_file()
    elif pilihan == "3":
        hapus_file()
    elif pilihan == "4":
        print(" Program selesai.")
        break
    else:
        print(" Pilihan tidak valid, coba lagi!")