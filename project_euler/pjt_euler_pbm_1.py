''' Add all the natural numbers below 1000 that are multiple of 3 0r 5 '''
sum = 0
for i in xrange(1000):
	if (i % 3)==0 or (i%5)==0:
		sum = sum + i

print sum
