def M(n):
	if n == 91:
		print n
		return n
	elif n > 100:
		print 'M({}) since {} is greater than 100'.format(n, str(n))
		return M(n-10)
	elif n <= 100:
		print 'M(M({})) since {} is less or equal than 100'.format(n, str(n))
		return M(M(n+11))

M(99)