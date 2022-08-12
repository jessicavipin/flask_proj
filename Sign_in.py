
file1 = open("credentials.txt", "r")
flag = 0
index = 0
for line in file1:  
    index += 1 
    if name in line:
        
      flag = 1
      break 
if flag == 0: 
   print('String', string1 , 'Not Found') 
else: 
   print('String', string1, 'Found In Line', index)  
file1.close() 