def make_reverse (my_string:str='Hello World'):
	a=''
	print(range(len(my_string)-1,0,-1))
	for i in range(len(my_string),0,-1):
		a+=my_string[i-1]
	return a

print(make_reverse('Saipoacoapias'))
