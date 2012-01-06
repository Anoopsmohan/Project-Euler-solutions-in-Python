''' palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers. '''


p=0
for m in xrange(999, 100, -1):
    for n in xrange(m, 100, -1):
	x = m * n
	if x > p:
	    s  = str (m * n)
	    if s == s[::-1]:
	       p = m * n
				

print p 
		
