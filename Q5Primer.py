number = int(input("Please enter a positive integer:"))

#if  number > 0:
#	for x in range(2, number):
#		if number % x == 0:
#			print("This number is not prime")
#			break
#	print( "That is a prime.")		

if number <= 0:
	print(" This is invalid number")
elif number == 1:
	print(" One is not the prime number")
else:
	for x in range (2, number):
		if number % x == 0:
			print("This number is not prime")
			break
	print("That is a prime.")	
	
	