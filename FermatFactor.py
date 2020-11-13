# Author: Alex King
# Fermat Factorization
# Use $python3 to compile

import math

#This function will be used to the factorization

def Factorize(n):
	
	#We need to determine if n is odd to determine
	#if we can use fermat's factorization
	

	#first one is clear we determine if 
	# a  is a perfect factor of n
	a = math.ceil( math.sqrt(n)) 

	if( a * a == n) :
		print("Pure factor so Fermat does not work ")
		return [a,a]

	#case of n is even
	if(n & 1) == 0:
		a = n /2
		return [ a, 2]
	
	#Use a bool flag to break our loop
	flag = False
 
	while(flag == False):
		count = a * a - n  #  a^2 - N
		b = math.isqrt(count) #make sure it is an interger
		if ( b * b == count):
			flag == True 
		else:
			a += 1

		return [a-b, a + b]

print("Enter your number below:")
n = int(input())
print("The factors of n  are " , Factorize(n))	
