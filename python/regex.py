
import re

def remove_first_last:
	string = "THIS Not this THIS"
    rm_first = string.split(' ', 1)
    rm_last = rm_first[1].rsplit(' ', 1)
    result = rm_last[0].strip('"')
    return result


def case_insensitive:
	string = "copy something"
	if re.match(r'^copy', string, re.IGNORECASE):
	    print(string)