def make_reverse (my_string:str='Hello 	world'):
	a=''
	for i in range(len(my_string),0,-1):
		a+=my_string[i-1]
	return a	
