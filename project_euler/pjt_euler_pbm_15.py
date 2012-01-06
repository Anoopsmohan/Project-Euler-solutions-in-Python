'''Starting in the top left corner of a 2 * 2 grid, there are 6 routes (without
 backtracking) to the bottom right corner.

How many routes are there through a 2020 grid?'''

def fact(n):
    if n == 0:
	return 1
    else:
	return n * fact(n-1)

rows, cols = 20, 20
print fact(rows+cols) / (fact(rows) * fact(cols))
