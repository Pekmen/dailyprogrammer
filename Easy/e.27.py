
def is_leap_year(year):
    if year % 4 != 0:
    	return False
    elif year % 100 != 0:
    	return True
    elif year % 400 != 0:
    	return False
    else:
    	return True

def get_century(year):
	return (year - 1) // 100 + 1

def main():
	year = int(input("Enter Year: "))
	print("Century: {}".format(get_century(year)))
	print("Leap Year: {}".format("Yes" if is_leap_year(year) else "No"))

main()