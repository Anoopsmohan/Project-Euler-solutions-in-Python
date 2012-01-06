''' sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

def primes_list(num):
    primes, number = [2], 3
    while number < num:
	isPrime = True
	for prime in primes:
	    if number % prime ==0:
		isPrime = False
		break
	    if (prime * prime > number):
		break
	if isPrime:
	    primes.append(number)
	number += 2
    return primes

#print sum(primes_list(2000000))

primes = primes_list(2000000)
print sum(primes)
