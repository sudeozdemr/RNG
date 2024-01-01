import csv
import random
import sys
import logging

if len(sys.argv) < 2 :
        print("ERROR! You didn't enter a file path.")
        sys.exit(1)
        
file_path = sys.argv[1] 

previous_names = []

with open(file_path, 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    datas = [line for line in csv_reader]

random.shuffle(datas)

iteration_count = 0

for data in datas:
    data_list= [data]
 
    
    if data_list not in previous_names:
    
        print(*data_list, end='')
        previous_names.append(data)
        sude = input("")
    
        if sude == '0' or sude == 'q': 
            break      
        
        iteration_count += 1
        if iteration_count >=15 :  
             break
             