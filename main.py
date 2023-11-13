import csv
import random

try:
   
    file_path = input("Lütfen bir CSV dosyası yolunu girin: ")

    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        datas = [line for line in csv_reader]

    random.shuffle(datas)

    for data in datas:
        print(*data, sep='', end='')  
        tus = input("")
        if tus.lower() == 'q':
            break

except FileNotFoundError:
    print(f"Dosya bulunamadı: {file_path}. Lütfen geçerli bir dosya yolunu kontrol edin.")
except Exception as eror:
    print(f"Bir hata oluştu: {eror}") 