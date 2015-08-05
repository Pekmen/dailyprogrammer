def str_manip (case, str1):
    if case == 0:
        return reversed(str1)
    elif case == 1:
    	return str1.upper()

def test_str (case, str1, str2):
    if str2 == str_manip(case, str1):
        print "Good test data"
    else:
        print "Mismatch! Bad test data"


