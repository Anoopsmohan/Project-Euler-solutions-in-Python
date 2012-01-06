'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
 that the 6th prime is 13.

What is the 10001st prime number? '''

def prime(n):
	primes = [2]
	num = 3
	while len(primes) < n:
		isPrime = True
		for prime in primes:
			if num % prime == 0:
				isPrime = False
				break
			if (prime * prime > num):
				break
		if isPrime:
			primes.append(num)
		num += 2
	return primes[n -1]
			


print prime(10001)			
