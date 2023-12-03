import csv
import random
import sys
import logging

if len(sys.argv) < 2 :
        print("ERROR! You didn't enter a file path.")
        sys.exit()
        
file_path = sys.argv[1] 

previous_names = []

with open(file_path, 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    datas = [line for line in csv_reader]

random.shuffle(datas)

try:
    for data in datas:
        print(*data, end='')  
        sude = input("")
        if sude == '0'or sude=='q' :
            break


except FileNotFoundError:
    print(f"File not found: {file_path}. Please enter a valid file path.")
except Exception as error:
    print(f"An error occurred: {error}")

 