def make_small (mystring: str) -> str:
    """pass a string as only parameter

    Returns the lower-cased string
    """
    return mystring.lower()

def make_reverse (my_string:str):
	a=''
	for i in range(len(my_string),0,-1):
		a+=my_string[i-1]
	return a	

def make_string_big(string: str): 
	"""This function turns any string into a BIG uppercase string."""
	return(string.upper())

