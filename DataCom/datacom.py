import csv
import random

# CSV dosyasından verileri oku
veriler = []
with open('data_com_list.csv', 'r') as dosya:
    csv_okuyucu = csv.reader(dosya)
    for satir in csv_okuyucu:
        veriler.append(satir)

# Verileri rastgele sırayla karıştır
random.shuffle(veriler)

# Döngü içinde verileri göster
for veri in veriler:
    print(*veri)  # * operatörü ile köşeli parantezleri ve tek tırnakları çıkarır
    tus = input("  ")
    if tus == 'q':
        break
