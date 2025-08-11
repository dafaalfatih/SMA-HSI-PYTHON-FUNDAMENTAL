# # latihan 1

# judul = input("Masukkan judul buku: ")
# judul_bersih = judul.strip().title()
# print("Judul yang distandarisasi:", judul_bersih)

# #latihan 2

# email = input("Masukkan email: ")

# if "@" in email and (email.endswith(".com") or email.endswith(".co.id")):
#     print("Email valid")
# else:
#     print("Email tidak valid")

#     # latihan 3

#     kalimat = input("Masukkan kalimat: ")
# kata_sensor = input("Masukkan kata yang ingin disensor: ")

# kalimat_sensored = kalimat.replace(kata_sensor, "***")
# print("Hasil setelah disensor:", kalimat_sensored)


# # latihan 4

# organisasi = input("Masukkan nama organisasi: ")
# kata_kata = organisasi.split()
# akronim = ''.join(kata[0] for kata in kata_kata).upper()
# print("Akronim:", akronim)


# #latian 5

import re

judul = input("Masukkan judul artikel: ")
judul_kecil = judul.lower()
slug = re.sub(r'[^a-z0-9\s-]', '', judul_kecil)  # Hapus karakter selain huruf, angka, spasi
slug = slug.replace(' ', '-')
print("Slug URL:", slug)