# latihan1_uppercase.py

# Meminta nama file dari pengguna
# nama_file = input("Masukkan nama file: ")

# try:
#     with open(nama_file, 'r', encoding='utf-8') as file:
#         for baris in file:
#             print(baris.strip().upper())
# except FileNotFoundError:
#     print(f"File '{nama_file}' tidak ditemukan.")

    
# latihan2_spam_confidence.py

# nama_file = input("Masukkan nama file: ")

# try:
#     with open(nama_file, 'r', encoding='utf-8') as file:
#         total = 0
#         hitung = 0

#         for baris in file:
#             if baris.startswith("X-DSPAM-Confidence:"):
#                 # Ambil bagian angka setelah tanda :
#                 angka = float(baris.split(":")[1].strip())
#                 total += angka
#                 hitung += 1

#         if hitung > 0:
#             print("Rata-rata spam confidence:", total / hitung)
#         else:
#             print("Tidak ditemukan baris dengan X-DSPAM-Confidence.")
# except FileNotFoundError:
#     print(f"File '{nama_file}' tidak ditemukan.")    



# latihan3_easter_egg.py

nama_file = input("Masukkan nama file: ")

if nama_file.lower() == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            for baris in file:
                print(baris.strip().upper())
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")


        