def digits_sum(s):
	curstr = 0
	result = s
	while len(result) > 1:
		print result
		for num in result:
			curstr += int(num)
		result = str(curstr)
		curstr = 0
	print result


digits_sum('12345')
    