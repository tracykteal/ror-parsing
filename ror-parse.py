# Python program to convert 
# JSON file to CSV 
  
  
import json 
import csv 
  
  
# Opening JSON file and loading the data 
# into the variable data 
with open('ror.json') as json_file: 
    ror_data = json.load(json_file) 
  
#ror_data = data[''] 
  
# now we will open a file for writing 
data_file = open('ror_data.csv', 'w') 
  
# create the csv writer object 
csv_writer = csv.writer(data_file) 
  
# Counter variable used for writing  
# headers to the CSV file 
count = 0
  
for ror in ror_data: 
    if count == 0: 
  
        # Writing headers of CSV file 
        header = ror.keys() 
        csv_writer.writerow(header) 
        count += 1
  
    # Writing data of CSV file 
    csv_writer.writerow(ror.values()) 
  
data_file.close()
