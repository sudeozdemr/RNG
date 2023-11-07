import csv
import random

# CSV dosyasından verileri oku
veriler = []
with open('ornek.csv', 'r') as dosya:
    csv_okuyucu = csv.reader(dosya)
    for satir in csv_okuyucu:
        veriler.append(satir)

# Verileri rastgele sırayla karıştır
random.shuffle(veriler)

# Döngü içinde verileri göster
for veri in veriler:
    print(*veri, sep='')  # Boşluğu kaldırmak için sep='' kullanılır
    tus = input(" ")
    if tus == 'q':
        break

