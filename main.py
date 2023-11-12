import csv
import random

try:
    
    dosya_yolu = input("Lütfen bir CSV dosyası yolunu girin: ")

    with open(dosya_yolu, 'r', newline='', encoding='utf-8') as dosya:
        csv_okuyucu = csv.reader(dosya)
        
        veriler = [satir for satir in csv_okuyucu]

    random.shuffle(veriler)

    for veri in veriler:
        print(*veri, sep='', end='')  
        tus = input("")
        if tus.lower() == 'q':
            break

except FileNotFoundError:
    print(f"Dosya bulunamadı: {dosya_yolu}. Lütfen geçerli bir dosya yolunu kontrol edin.")
except Exception as hata:
    print(f"Bir hata oluştu: {hata}")
