

import csv
import random
import sys

iteration_counter = 0
default_iteration_count = 16

if len(sys.argv) < 3 :
    iteration_count = default_iteration_count
    print(f"No iteration count provided, using default: {iteration_count}")
else:
    iteration_count = int(sys.argv[2])
        
file_path = sys.argv[1] 
'''if file_path file path boş ise hata file path boş yazsın.'''


with open(file_path, 'r', newline='', encoding='utf-8') as file: 
    csv_readed = (csv.reader(file))
    datas = [line for line in csv_readed]

random.shuffle(datas)

for return_values in datas: 
    iteration_counter += 1
    print(*return_values, end='')
    press_this = input()

    if press_this == '0' or press_this == 'q': 
        break 
          
    if iteration_counter == iteration_count :  
        break

    previous_names = []
    previous_names.append(return_values)

    previous_names_filepath = "text.txt"
    #print(*previous_names) 

with open(previous_names_filepath, "w") as previous_names_file:
    for variable in previous_names:
        string = ",".join(variable) + "\n"  
        previous_names_file.write(string)

       
        
   
    
    





