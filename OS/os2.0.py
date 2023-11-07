import csv
import random

dosya_adi = "ornek.csv"  
N = 8 


with open(dosya_adi, "r", newline='') as csvfile:
    csv_reader = csv.reader(csvfile)

    veri_listesi = list(csv_reader)

    rastgele_veriler = random.sample(veri_listesi, N)

    for veri in rastgele_veriler:
        print(''.join(veri))



