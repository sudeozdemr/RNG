import csv
import random
import sys

default_iteration_count = 16
iteration_counter = 0

if len(sys.argv) < 3 :
    iteration_count = default_iteration_count
    print(f"No iteration count provided, using default: {iteration_count}")
else:
    iteration_count = int(sys.argv[2])
        
file_path = sys.argv[1] 

previous_names = []

with open(file_path, 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    datas = [line for line in csv_reader]

random.shuffle(datas)

for data in datas:
    data_list= data

    iteration_counter += 1

 
    if data_list not in previous_names:
    
        print(*data_list, end = '')
        previous_names.append(data)
        press_this = input()
    
        if press_this == '0' or press_this == 'q': 
            break      
       
        if iteration_counter == iteration_count :  
                break

                  