# Enter number and base and result tells you if number is happy :) or sad :(h

# returns sum of squares of all digits in the argument `arr`
def sumOfSquares(arr):
	return sum([x**2 for x in arr])

# returns an array of the correct base `b` taking in the base_10 `num`
def returnDigits(num, b):
	arr = []
	dvnd = 0
	while True:
		rem = num % b
		num = int((num - rem)/b)
		arr.append(rem)
		if num == 0:
			break
	return arr[::-1]

# returns whether or not the number passed in is happy
def isHappy(num, b):
	# options: either `num` is number 
	# 1. base_10, or 
	# 2. base_`b`
	n = [int(x) for x in list(num)] #1
	# n = returnDigits(int(num), b) #2

	slow = fast = n
	while True:
		slow = returnDigits(sumOfSquares(slow), b)
		fast = returnDigits(sumOfSquares(returnDigits(sumOfSquares(fast), b)), b)
		if sumOfSquares(slow) == 1 or sumOfSquares(fast) == 1:
			return True
		if sumOfSquares(slow) == sumOfSquares(fast):
			return False
	return True

def main():
	#assuming inputs are correct
	num = input('Enter number: ')
	base = input('Enter base: ')
	#print(num, base, isHappy(str(num), int(base)))
	count = 0
	for i in range(1,10001):
		if isHappy(str(i), 5):
			count+=1
	print(count)
	return

main()

'''
References:
1. http://mathworld.wolfram.com/HappyNumber.html
2. http://math.bard.edu/student/pdfs/alison-mutter.pdf
3. https://en.wikipedia.org/wiki/Happy_number#Happy_numbers_in_other_bases
4. http://oeis.org/A039943
5. http://extraconversion.com/base-number/base-5
6. https://rosettacode.org/wiki/Happy_numbers
'''
