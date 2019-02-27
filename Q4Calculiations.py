userInput = int(input("Add positive integer:"))
#end =" " makes the end of the line have a space
print(userInput, end=" ")
while(userInput > 1):
	if userInput % 2 == 0:
		userInput = userInput/2
	else : 
		userInput = userInput * 3 + 1
	print(int(userInput), end=" ")	
	