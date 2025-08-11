# latihan 1
 
 for i in range (0, 71, 7):
    print(i)


    # latihan 2

    kalimat = "python"
    kalimat_terbalik = ""

    for huruf in kalimat:
        kalimat_terbalik = huruf + kalimat_terbalik

        print(kalimat_terbalik)

        #latihan 3

jumlah = 0

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        jumlah += 1

print("jumlah angka yang habis di bagi 3 dan 5 adalah", jumlah)        


#latihan 4


for i in range(5, 0, -1):  # loop dari 5 ke 1 (mundur)
    for j in range(i):     # mencetak '*' sebanyak i kali
        print('*', end='') # cetak tanpa newline
    print()               

    

# latihan 5

angka = int(input("masukkan angka bulat positif"))

faktorial = 1

for i in range(1, angka + 1):
    faktorial *= i

print(f"Faktorial dari {angka} adalah {faktorial}")   


