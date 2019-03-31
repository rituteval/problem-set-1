import sys

file_name = sys.argv[1]
file = open(file_name,"r")
lines = file.readlines()
counter = 0
for line in lines:	
	if counter %2 == 0:
		print(line)
	#same as counter = counter +1
	counter += 1	


	