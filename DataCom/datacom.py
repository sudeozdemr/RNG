import csv
import random


veriler = []
with open('data_com_list.csv', 'r') as dosya:
    csv_okuyucu = csv.reader(dosya)
    for satir in csv_okuyucu:
        veriler.append(satir)


random.shuffle(veriler)


for veri in veriler:
    print(*veri)  
    tus = input("  ")
    if tus == 'q':
        break
