import csv

dosya_adi = "veriler.csv"

veriler = [
    "200101025 Volkan Acar", "190101043 Yunus Emre Çiçek", "210101098 Zal İbrahim Solmuş", "170101043 Zeyd Kadir Şen"]

with open(dosya_adi, mode='w', newline='') as dosya:
    yazici = csv.writer(dosya, )
    for veri in veriler:
        yazici.writerow([veri])

print(veriler)