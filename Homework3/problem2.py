num = int(input("Enter a positive integer: "))

def get_primes(number):
	primes = []
	for i in range(2, number+1):
		isPrime = True
		for number in range(2, i):
			if i % number == 0:
				isPrime = False
		if isPrime:
			primes.append(i)
		else: i+=1
	return primes

print(get_primes(num))

