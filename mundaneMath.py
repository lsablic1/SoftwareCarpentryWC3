'''
Write a python script called mundaneMath.py that adds together all
the even numbers between 1 and 100, and prints to the terminal
'''

if __name__ == "__main__":

	s = 0

	for i in range(100):
		rem = i%2
		
		if rem == 0:
			s = s+i
		else: 
			s = s


	print(s)
