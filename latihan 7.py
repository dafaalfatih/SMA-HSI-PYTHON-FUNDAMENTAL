# latihan 1

while True:
    data_input = input ("> ")

    if (data_input == "selesai"):
        break

x = 10

while x >= 1:
    print(x)
    x-= 1
print("perulangan selesai")    
print("Blastoff!")


# latihan 2

angka_rahasia = 7

while True:
    tebakan = int(input("tebak angka (1-10):"))
    if tebakan == angka_rahasia:
        print("asikk benar!")
        break # keluar dari loop kalau benar
    else:
        print("salah coba lagi!")

print("makasih ya sudah bermain")  




# # cuma coba coba
# import random

# # Bisa random atau tetap, ini random biar makin seru
# angka_rahasia = random.randint(1, 10)

# while True:
#     try:
#         tebakan = int(input("Tebak angka (1-10): "))  # input user
#         if tebakan == angka_rahasia:
#             print("🎉 Selamat, tebakan Anda benar!")
#             break
#         else:
#             print("❌ salah coba lagi!")
#     except ValueError:
#         print("⚠️ Masukkan angka yang valid dong!")

# print("🙏 Terima kasih sudah bermain!")





# # latihan 3

total = 0       # buat nyimpen total penjumlahan semua angka
count = 0       # buat ngitung berapa angka yang berhasil dimasukin

while True:
    user_input = input("Masukkan angka (atau ketik 'done' untuk selesai): ")

    if user_input.lower() == 'done':  # kalau user ketik done
        break  # keluar dari loop

    try:
        angka = float(user_input)  # coba konversi input ke float
        total += angka             # tambahin ke total
        count += 1                 # tambahin jumlah angka
    except ValueError:
        print("Input tidak valid")  # kalau input bukan angka, kasih pesan error
        continue                    # langsung lanjut ke input berikutnya

# Setelah loop selesai:
if count > 0:
    rata_rata = total / count
    print(f"\nTotal: {total}")
    print(f"Jumlah angka yang dimasukkan: {count}")
    print(f"Rata-rata: {rata_rata}")
else:
    print("\nBelum ada angka yang valid dimasukkan.")

    