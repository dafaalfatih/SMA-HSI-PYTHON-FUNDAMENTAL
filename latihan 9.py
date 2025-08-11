s = "Belajar Python itu Menyenangkan"

# Karakter pertama
print("Karakter pertama:", s[0])  # 'B'

# Karakter terakhir menggunakan indexing negatif
print("Karakter terakhir:", s[-1])  # 'n'

# Karakter spasi pertama (di indeks 7)
print("Spasi pertama:", s[7])  # ' '


# latihan 2

s = "Belajar Python itu Menyenangkan"

# "Python"
print("Python:", s[8:14])

# "Menyenangkan"
print("Menyenangkan:", s[19:])  # dari indeks 19 sampai akhir

# "Belajar"
print("Belajar:", s[0:7])


# latihan 3

kata = input("Masukkan sebuah kata: ")

kata_terbalik = kata[::-1]
print("Kata terbalik:", kata_terbalik)

if kata == kata_terbalik:
    print("Ini adalah palindrom!")
else:
    print("Ini bukan palindrom.")

    # latihan 4

    kalimat = "BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"

# Ambil setiap karakter ketiga
kode_rahasia = kalimat[::3]
print("Kode Rahasia:", kode_rahasia)


# latihan 5

nama_salah = "dUDI sANTOSO"

# Ambil huruf 'd', ubah ke 'B', lalu ambil 'UDI' jadi 'udi'
nama_baru = "B" + nama_salah[1:4].lower()  # 'Budi'

# Ambil 'sANTOSO', ubah ke 'S' + 'antoso'
nama_baru += " " + nama_salah[5].upper() + nama_salah[6:].lower()  # 'Santoso'

print("Nama benar:", nama_baru)